# Wazuh Installation & Setup Guide on Ubuntu via WSL 2

## Overview
This guide provides step-by-step instructions for installing and configuring Wazuh SIEM (Single-Node All-in-One Deployment) on Ubuntu running via WSL 2 on Windows.

## Prerequisites
- **Host OS**: Windows 11
- **WSL Distro**: Ubuntu 22.04 LTS
- **WSL Resource Allocation**: Configured via `.wslconfig`

```ini
[wsl2]
memory=6GB
processors=4
swap=2GB
```

## Installation Steps

### 1. System Preparation
Update the Ubuntu package lists and upgrade existing packages:

```bash
sudo apt update && sudo apt upgrade -y
```
### Screenshot:
> <img width="1366" height="768" alt="Screenshot 2025-08-24 224433" src="https://github.com/user-attachments/assets/10340910-1c01-4397-a424-94f490162537" />

---

### **2. Downloading the Wazuh Installer**

**Task:** Download the official Wazuh installation script and configuration file.

**Commands Used:**
```bash
curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh
curl -sO https://packages.wazuh.com/4.7/config.yml
```

### 🚨 **Problem 1: Silent Download Failure & Empty Config File**

**Error:** After running the installation script, the process failed with the error:
`ERROR: Invalid IP or DNS <indexer-node-ip>`

**Cause & Investigation:**
1.  The initial download of the `config.yml` file had a typo (`wazah.com` instead of `wazuh.com`), causing a silent failure and resulting in an empty file.
2.  The installation script could not proceed because the mandatory IP address fields were blank.

**Solution:**
1.  **Re-downloaded the config file** with the correct URL:
    ```bash
    curl -sO https://packages.wazuh.com/4.7/config.yml
    ```
2.  **Verified the download** by checking the file size:
    ```bash
    ls -l config.yml
    # Correct output: -rw------- 1 root root 636 Aug 24 22:56 config.yml
    ```

**Lesson Learned:** Always verify critical downloaded files using `ls -l` to confirm they are not empty before proceeding.

---

### **3. Configuring the Installation**

**Task:** Modify the `config.yml` file with the correct IP address for the WSL instance.

**Step 1: Find the WSL IP Address**
```bash
ip addr show eth0 | grep inet
# Output: inet 172.20.175.70/20 ... This is was My WSL IP.
```

**Step 2: Edit the Configuration File**
```bash
sudo nano config.yml
```

**Changes Made:** Located and modified **three** separate IP address fields in the `config.yml` file:
*   **Indexer Node IP:** Changed from `ip: "<indexer-node-ip>"` to `ip: "172.20.175.70"`
*   **Wazuh Server IP:** Changed from `ip: "<wazuh-manager-ip>"` to `ip: "172.20.175.70"`
*   **Dashboard Node IP:** Changed from `ip: "<dashboard-node-ip>"` to `ip: "172.20.175.70"`

**Screenshot:**
> <img width="1366" height="768" alt="Screenshot 2025-08-24 225939" src="https://github.com/user-attachments/assets/efd6479f-d9d7-4885-aab0-bf79f5e38a84" />

---

### **4. Running the Installation Script**

**Task:** Execute the installation script with the corrected configuration.

**Command Used:**
```bash
sudo bash ./wazuh-install.sh --generate-config-files
```

**Progress:**
The script successfully passed the configuration stage. The terminal output showed:
```
INFO: Created wazuh-install-files.tar. It contains the Wazuh cluster key, certificates, and passwords necessary for installation.
```
> <img width="1366" height="768" alt="Screenshot 2025-08-24 230602" src="https://github.com/user-attachments/assets/ea597654-115e-4fcf-8d0f-1f5cc9bbfd99" />
