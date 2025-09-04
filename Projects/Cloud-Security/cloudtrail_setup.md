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

![Create Access Keys](https://via.placeholder.com/800x400.png?text=Create+Access+Keys)


