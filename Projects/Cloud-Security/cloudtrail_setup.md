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

![Screenshot of the S3 bucket creation page, showing the unique name and blocked public access.](screenshots/step1-s3-bucket-creation.png)

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

![Screenshot of the CloudTrail configuration, highlighting the trail name and the selection of the existing S3 bucket.](screenshots/step2-cloudtrail-config.png)

*   **Verification:** After clicking "Create", AWS confirmed the trail was successfully created. The trail will now automatically start recording API activity and delivering log files to my S3 bucket.

![Screenshot of the success message after creating the CloudTrail trail.](screenshots/step2-cloudtrail-success.png)

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
