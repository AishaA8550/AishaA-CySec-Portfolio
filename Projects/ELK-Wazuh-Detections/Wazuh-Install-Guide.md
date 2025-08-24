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
