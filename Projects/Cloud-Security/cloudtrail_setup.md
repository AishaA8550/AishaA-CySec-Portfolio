# Connecting AWS CloudTrail to Wazuh

This is my documentation for my project where I built a pipeline to send security logs from my AWS account to my self-hosted Wazuh SIEM for monitoring.

## Architecture Overview

The goal is to automatically get logs from AWS to Wazuh. Here is the flow I set up:

1.  **AWS CloudTrail:** Records every API call (like creating or deleting resources) in my AWS account.
2.  **Amazon S3:** CloudTrail automatically saves these logs as compressed JSON files in a private S3 bucket every 5 minutes.
3.  **Amazon SQS:** This is a message queue. When a new log file lands in the S3 bucket, it sends a notification message to this queue saying, "Hey, a new file is here!"
4.  **Wazuh Filebeat:** A lightweight agent on my Wazuh server constantly checks the SQS queue for new messages. When it sees one, it reads the log file from S3 and forwards it to the **Wazuh Manager** for analysis.

This way, I don't have to manually check for logs; everything is automated and secure.

## Prerequisites

*   An AWS Account (using the Free Tier).
*   A Wazuh Manager already installed on a windows.

## Implementation Steps

### Step 1: Creating the S3 Bucket (The Secure Storage Box)

I started by creating a bucket in Amazon S3. Think of this as a private, secure storage box in the cloud where our logs will be saved. It's important to make sure this box is locked down.

*   **What I did:**
    1.  I went to the AWS S3 console and clicked "Create bucket".
    2.  I named my bucket **`wazuh-cloudtrail-logs-aisha`** to make it easy to identify.
    3.  I chose the **`eu-north-1`** region to keep everything close for better performance.
    4.  **Most importantly:** I left **"Block all public access"** ENABLED. This is a critical security step that ensures no one on the internet can access my logs.

*   **Why this step is important:** This bucket is the foundation. All our sensitive AWS logs will be stored here, so it must be secure from the start.

<img width="1366" height="768" alt="Screenshot 2025-09-03 081412" src="https://github.com/user-attachments/assets/58f19672-c371-4537-8989-e91e9c6e7237" />

---

### Step 2: Creating the CloudTrail Trail (The Logger)

Next, I needed to tell AWS *what* to log and *where* to send those logs. This is done by creating a "trail" in AWS CloudTrail.

*   **What I did:**
    1.  I went to the AWS CloudTrail service and clicked "Create trail".
    2.  I named my trail **`wazuh-management-events-trail`**.
    3.  Under "Storage location", I selected **"Use an existing S3 bucket"** and chose the bucket I made in Step 1.
    4.  For "Log events", I selected **Management events**. This means it will log all the important actions that change things in my account (like launching an EC2 instance or creating a user).
    5.  I ensured **Data events** and **Insights** were disabled to avoid extra costs, as this is a student project.

*   **Why this step is important:** The trail is like turning on the security camera and pointing it at the right place. Without this, no logs are generated or saved to our bucket.

[Screenshot of the CloudTrail configuration, highlighting the trail name and the selection of the existing S3 bucket.]<img width="1366" height="768" alt="Screenshot 2025-09-03 082726" src="https://github.com/user-attachments/assets/5a29d5f7-48a4-4ddb-aafb-c1e6b79cb905" />


*   **Verification:** After clicking "Create", AWS confirmed the trail was successfully created. The trail will now automatically start recording API activity and delivering log files to my S3 bucket.

[Screenshot of the success message after creating the CloudTrail trail.]<img width="1366" height="768" alt="Screenshot 2025-09-03 083504" src="https://github.com/user-attachments/assets/34a4ae19-b52a-4a4d-a62f-7308b9e4407f" />
)

---

## Cost & Security Notes

*   **Cost:** This setup is designed to be **free**.
    *   The first CloudTrail trail (for management events) is free.
    *   The amount of log data from a student account is tiny and fits easily within the 5GB S3 Free Tier.
    *   The number of SQS messages will be low and also fit within Free Tier limits.
*   **Security:**
    *   The S3 bucket is private by default.
    *   The IAM user I create will follow the **Principle of Least Privilege**, meaning it will only get the absolute minimum permissions needed to read the logs and check the queue (`s3:GetObject`, `sqs:ReceiveMessage`).

---
## Step 3: Creating an IAM User for S3 Access

This step creates a dedicated IAM user with minimal permissions to read from your S3 bucket, following the principle of least privilege.

### 1. Navigate to IAM Console
- Go to the AWS Management Console
- Search for "IAM" in the services search bar
- Click on "IAM" to open the Identity and Access Management console

### 2. Create New User
- In the IAM left sidebar, click "Users"
- Click the "Create user" button

### 3. Set User Details
- Enter the user name: `wazuh-s3-reader`
- Click "Next"
- 
> <img width="1366" height="768" alt="Screenshot 2025-09-04 231232" src="https://github.com/user-attachments/assets/785cef58-e429-44bf-b141-c74ae9dffeea" />



### 4. Set Permissions
- Select "Attach policies directly"
- Click "Create policy" (this opens a new tab)

### 5. Create Policy (New Tab)
- In the policy editor, click the "JSON" tab
- Delete any existing text
- Copy and paste the following policy, replacing `YOUR_BUCKET_NAME` with your actual bucket name (`wazuh-cloudtrail-logs-aisha`):

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::wazuh-cloudtrail-logs-aisha",
                "arn:aws:s3:::wazuh-cloudtrail-logs-aisha/*"
            ]
        }
    ]
}
```

> <img width="1366" height="768" alt="Screenshot 2025-09-04 231642" src="https://github.com/user-attachments/assets/2c391dab-3605-480b-a2dc-2feee735ceb3" />


### 6. Complete Policy Creation
- Click "Next"
- Add a description: "Grants read-only access to the specific S3 bucket used for Wazuh CloudTrail logs."
- Name the policy: `WazuhS3ReadAccess`
- Click "Create policy"

### 7. Attach Policy to User
- Return to the original tab where you're creating the user
- Click the refresh button (🔄) next to the policy list
- Search for `WazuhS3ReadAccess`
- Check the box next to your policy
- Click "Next"

> <img width="1366" height="768" alt="Screenshot 2025-09-04 232355" src="https://github.com/user-attachments/assets/42ad83d4-37f5-4657-8b2c-d953cbadedca" />


### 8. Review and Create User
- Review the user details
- Click "Create user"

><img width="1366" height="768" alt="Screenshot 2025-09-04 232422" src="https://github.com/user-attachments/assets/7e039bea-c128-4cde-b643-fdfc5bbea333" />


### 9. Create Access Keys
- After user creation, you'll see a success message
- Click on the user name `wazuh-s3-reader` in the list
- Go to the "Security credentials" tab
- Click "Create access key"
- Select "Application running outside AWS"
- Click "Create access key"

> <img width="1366" height="768" alt="Screenshot 2025-09-05 074313" src="https://github.com/user-attachments/assets/949a3787-8a83-4c2c-b4d5-7218f89b39ac" />


---

### **Step 4: Creating the SQS Queue (The Message Notifier)**

To enable real-time notifications of new log files, I set up an Amazon Simple Queue Service (SQS) queue. This queue will act as a communication channel between my S3 bucket and the Wazuh server.

**What I did:**

1.  I navigated to the **Amazon SQS** service in the AWS Management Console.
2.  I clicked the **"Create queue"** button.
3.  I selected the **"Standard"** queue type for maximum throughput and to avoid potential duplication issues, which is acceptable for log processing.
4.  I named my queue **`CloudTrail-s3-queue`** for clear identification.
5.  I left all other settings at their defaults and clicked **"Create queue"**.

**Why this step is important:** The SQS queue is the critical link that enables automation. Without it, my Wazuh server would have to constantly poll the S3 bucket to check for new files, which is inefficient. SQS allows S3 to actively push a notification, making the pipeline event-driven and near real-time.

*(Screenshot of the SQS queue creation page, highlighting the queue name and type, would be placed here)*
> <img width="1366" height="768" alt="Screenshot 2025-09-05 075411" src="https://github.com/user-attachments/assets/57286075-f9b3-482b-b124-e457948b8d21" />

---
### **Step 5: Configuring S3 Bucket Events**

With the SQS queue created, I needed to configure my S3 bucket to send a message to this queue whenever a new CloudTrail log file is written.

**What I did:**

1.  I returned to the **Amazon S3** console and selected my bucket, **`wazuh-cloudtrail-logs-aisha`**.
2.  I navigated to the **"Properties"** tab.
3.  I scrolled down to the **"Event notifications"** section and clicked **"Create event notification"**.
4.  I configured the event:
    *   **Event name:** `NotifySQS`
    *   **Event types:** Selected **"All object create events"**. This ensures that every time CloudTrail delivers a new log file, an event is triggered.
    *   **Destination:** Selected **"SQS Queue"** and from the dropdown, chose my queue, **`CloudTrail-s3-queue`**.
5.  I clicked **"Save changes"**.

**Initial Error & Resolution:**
Upon saving, I encountered an error: `Unable to validate the following destination configurations`. This is a common error indicating that the S3 service does not have permission to send messages to my SQS queue.

**To resolve this, I modified the SQS queue's access policy:**

1.  I went back to the **SQS Console**, selected my **`CloudTrail-s3-queue`**, and went to the **"Access policy"** tab.
2.  I clicked **"Edit"** and replaced the default policy with the following JSON, ensuring I used the correct ARNs for my S3 bucket and SQS queue:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Action": "sqs:SendMessage",
      "Resource": "arn:aws:sqs:eu-north-1:029377893931:CloudTrail-s3-queue",
      "Condition": {
        "ArnLike": {
          "aws:SourceArn": "arn:aws:s3:::wazuh-cloudtrail-logs-aisha"
        }
      }
    }
  ]
}
```

3.  After saving the policy, I retried creating the event notification in the S3 bucket. The operation completed successfully.

**Why this step is important:** This configuration automates the entire trigger mechanism. The pipeline is now active: a new log file in S3 generates an SQS message, which will signal Filebeat to process the file.

*(Screenshot of the successful S3 event notification configuration would be placed here)*
> <img width="1366" height="768" alt="Screenshot 2025-09-05 080414" src="https://github.com/user-attachments/assets/c4dd0054-2ff2-4a40-a55c-18b1d6de54b9" />

---
yettttt
### **Step 6: Securing the IAM User for SQS Access**

My initial IAM policy for the `wazuh-s3-reader` user only granted permissions for S3. For the user to read messages from the SQS queue, I needed to extend its permissions.

**What I did:**

1.  I navigated to the **IAM Console** > **Policies**.
2.  I located the policy I created earlier, **`WazuhS3ReadAccess`**, and clicked **"Edit"**.
3.  I selected the **"JSON"** tab and updated the policy to include the necessary SQS actions, ensuring least privilege by specifying only the required actions and the exact ARN of my queue.

**Final IAM Policy:**

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::wazuh-cloudtrail-logs-aisha",
                "arn:aws:s3:::wazuh-cloudtrail-logs-aisha/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:GetQueueUrl",
                "sqs:DeleteMessage",
                "sqs:ReceiveMessage"
            ],
            "Resource": "arn:aws:sqs:eu-north-1:029377893931:CloudTrail-s3-queue"
        }
    ]
}
```

4.  I reviewed the policy and saved the changes.

**Why this step is important:** This adheres to the core security principle of least privilege. The Wazuh server's identity now has the exact permissions it needs—and nothing more—to read log files from S3 and check for messages in SQS, minimizing the attack surface.

*(Screenshot of the updated IAM policy JSON would be placed here)*

---

### **Step 7: Configuring Filebeat on the Wazuh Server**

With the AWS infrastructure fully built and configured, the final step was to configure the Wazuh server to connect to this pipeline. This involves configuring the Filebeat agent to use the **`aws-s3`** input.

**What I did:**

1.  I accessed my Wazuh server via SSH.
2.  I created a dedicated configuration file to avoid interfering with the existing Wazuh-managed Filebeat installation: `sudo nano /etc/filebeat-aws.yml`
3.  I added the following configuration, using the IAM user's access keys and the SQS queue URL:

```yaml
filebeat.inputs:
  - type: aws-s3
    queue_url: "https://sqs.eu-north-1.amazonaws.com/029377893931:CloudTrail-s3-queue"
    access_key_id: 'XXXXXXXXXXXX'
    secret_access_key: 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
    region: eu-north-1

output.console:
  pretty: true
```

4.  I initially set the output to `console` to test the AWS connection without affecting my Wazuh indexer.

**Verification Test:**
I ran Filebeat with this test configuration to validate the AWS connection:
```bash
sudo /usr/share/filebeat/bin/filebeat -c /etc/filebeat-aws.yml -e
```
The command successfully connected to the SQS queue, retrieved a CloudTrail log file from S3, and printed the parsed JSON events to the console. This confirmed that the AWS credentials, permissions, and network connectivity were all correctly configured.

**Why this step is important:** This test is a crucial troubleshooting step. It verifies the entire AWS-side configuration independently before integrating with the more complex Wazuh Elasticsearch output, isolating any potential issues.

*Screenshot of the terminal showing Filebeat successfully processing and printing AWS events would be placed here*
><img width="1366" height="768" alt="Screenshot 2025-09-22 151018" src="https://github.com/user-attachments/assets/de5fc4bd-9cc4-4b5f-a41e-148d0c58a31f" />

---
 **AWS CloudTrail → Wazuh Integration - COMPLETED**

### **✅ What Works:**
- AWS S3 bucket + CloudTrail trail configured
- SQS queue + IAM permissions functional  
- Filebeat successfully connects to AWS and retrieves CloudTrail logs
- **Proof:** Filebeat console output shows real CloudTrail events

### **⚠️ Technical Note:**
Filebeat 8.15.0 successfully collects logs but cannot forward to Wazuh 4.7's Elasticsearch 7.10.2 due to version incompatibility. The AWS pipeline architecture is fully validated.
