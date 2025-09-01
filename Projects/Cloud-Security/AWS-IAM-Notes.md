#  AWS IAM - Theoretical Foundations

## Overview
Today's focus was on understanding the core theoretical concepts of AWS Identity and Access Management (IAM) before any practical implementation. Mastering these fundamentals is critical for building a secure cloud environment.

## Core IAM Concepts

| Concept | Description | Analogy |
| :--- | :--- | :--- |
| **Root User** | The super-administrative identity created with the AWS account. Has complete, unrestricted access. | The master key to the entire building. Used only for emergencies and initial setup. |
| **IAM User** | An identity for a person or service that needs to interact with AWS resources. | A personalized keycard for an employee. |
| **IAM Group** | A collection of IAM users. Permissions applied to the group apply to all users within it. | A department (e.g., "Development"). Easier to manage permissions for a team. |
| **IAM Policy** | A JSON document that defines permissions by specifying **Actions**, **Resources**, and **Effect** (Allow/Deny). | A rulebook that states what your keycard allows you to do (e.g., "Enter the server room, but only between 9-5"). |
| **Principle of Least Privilege** | A security best practice of granting only the permissions necessary to perform a specific task. | An employee in the mailroom doesn't need access to the financial records. |

## Why IAM is the Cornerstone of AWS Security

*   **Centralized Control:** Manage access to all AWS services and resources from a single point.
*   **Granular Permissions:** Policies allow for extremely specific permissions, far beyond simple "admin" or "user" roles.
*   **Shared Access:** Enable multiple users to work on a single AWS account without sharing passwords.
*   **Identity Federation:** Allow existing identities (e.g., from a corporate network) to access AWS resources.
*   **Compliance:** Detailed access logging via **AWS CloudTrail** provides an audit trail of who did what and when.
---
##  Practical Implementation & Steps Taken

### 1. Securing the Root Account with MFA
**What I Did:**
Logged into the AWS Console as the root user and enabled Multi-Factor Authentication (MFA) using a virtual device (Google Authenticator app).

**Why This Step is Crucial:**
The root account is the biggest target for attackers. **MFA adds a critical second layer of security.** This is the single most important security action for any cloud account.

**Screenshot:**
> *(Screenshot of the IAM Credentials page showing the "Virtual" MFA device assigned.)*
![Root MFA Setup](images/day10-root-mfa.png)

---

### 2. Activating IAM User Billing Access
**What I Did:**
As the root user, I activated **IAM User and Role Access to Billing Information** in the Account Settings.

**Why This Step is Crucial:**
This setting must be enabled to allow IAM users to access billing data via IAM policies, adhering to the Principle of Least Privilege.

**Screenshot:**
> *(Screenshot of the Account page showing "Activate IAM Access" checked.)*
![Activate IAM Billing Access](images/day10-billing-access.png)

---

### 3. Creating an IAM Group with a Policy
**What I Did:**
Created a new IAM group named `Admin-ReadOnly` and attached the AWS managed policy `ReadOnlyAccess`.

**Why This Step is Crucial:**
- **Groups are a best practice for assigning permissions** (as defined in the theory), making management scalable.
- The `ReadOnlyAccess` policy is a perfect implementation of the **Principle of Least Privilege**, allowing a user to view resources but not make changes.

**Screenshot:**
> *(Screenshot showing the group name and the attached `ReadOnlyAccess` policy.)*
![ReadOnly Group](images/day10-readonly-group.png)

---

### 4. Creating a Non-Root IAM User
**What I Did:**
Created a new IAM user named `Aisha-Admin` with both Programmatic and Console access. I added the user to the `Admin-ReadOnly` group.

**Why This Step is Crucial:**
This puts the theory into practice: **never use the root user for daily tasks.** Creating a separate IAM user for daily operations is a fundamental security practice.

**Screenshot:**
> *(Screenshot of the user creation page, showing the user being added to the `Admin-ReadOnly` group.)*
![Add User to Group](images/day10-user-to-group.png)

---

### 5. Securely Storing Credentials
**What I Did:**
Downloaded the CSV file containing the new user's credentials.

**Why This Step is Crucial:**
The secret access key is **only available once**. This file must be stored with the highest level of security and never shared or committed to a public repository.

**Screenshot:**
> *(Screenshot of the success message that says "Download .csv file".)*
![Download CSV](images/day10-download-csv.png)

---

### 6. Testing the New IAM User
**What I Did:**
Signed out of the root account and signed back in using the IAM user's sign-in URL and credentials. Verified permissions worked correctly.

**Why This Step is Crucial:**
This validates the practical setup. An "Access Denied" error when trying to create a resource confirms the `ReadOnlyAccess` policy is actively enforcing least privilege.

**Screenshot:**
> *(Screenshot of the IAM dashboard URL, showing the unique sign-in link.)*
![IAM User Signed In](images/day10-iam-signin-url.png)

## Key Takeaways
- **Theory Informs Practice:** Understanding IAM concepts is critical before implementation.
- **Root User is for Setup Only:** Its only jobs are initial setup and specific account-level tasks. It must be locked down with MFA.
- **Principle of Least Privilege in Action:** The `ReadOnlyAccess` policy is a secure and practical starting point.
- **Manage Permissions via Groups:** This is the efficient and consistent way to manage user access, as learned in the theoretical foundations.
- **Guard Secrets:** Credentials are the keys to your kingdom; they must be protected accordingly.

---
