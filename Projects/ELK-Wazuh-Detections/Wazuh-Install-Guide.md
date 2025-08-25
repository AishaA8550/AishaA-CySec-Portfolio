# Wazuh SIEM Deployment on Ubuntu via WSL 2

## Overview
This project documents the successful deployment of a **Wazuh SIEM** (Security Information and Event Management) system in a **single-node, all-in-one** configuration. Built on an Ubuntu instance running through **Windows Subsystem for Linux (WSL 2)**, this setup provides a full-featured, open-source security monitoring platform perfect for labs, learning, and small-scale environments.

## Prerequisites
- **Host OS:** Windows 10 or 11 with WSL2 enabled
- **WSL Distro:** Ubuntu 22.04 LTS
- **Resource Allocation:** Configured via `%USERPROFILE%\.wslconfig`
    ```ini
    [wsl2]
    memory=6GB
    processors=4
    swap=2GB
    localhostForwarding=true
    ```

## Installation & Configuration Steps

### 1. System Preparation
Update the system package lists and upgrade all existing packages to ensure a stable foundation.
```bash
sudo apt update && sudo apt upgrade -y
```

> <img width="1366" height="768" alt="Screenshot 2025-08-24 224433" src="https://github.com/user-attachments/assets/1c3bd6e4-bf74-4365-b0c3-98dc5766870b" />


### 2. Download the Wazuh Installation Assets
Download the official installation script and its configuration template.
```bash
curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh
sudo chmod +x wazuh-install.sh
```

### 3. Resolve Pre-Installation Conflicts
A pre-existing `docker-elk` stack was identified, occupying the required ports (5601, 9200). It was gracefully shut down to free the environment without data loss.
```bash
# Identify and stop the conflicting stack
docker ps --filter "name=elk" --filter "name=kibana"
cd ~/docker-elk
docker-compose down
```

### 4. Execute the Installation
Run the installer with the flags for an all-in-one deployment, specifying the dashboard port and forcing an overwrite to clean any previous partial installations.
```bash
sudo bash ./wazuh-install.sh -a -p 5601 -o
```

> <img width="1366" height="768" alt="Screenshot 2025-08-25 070407" src="https://github.com/user-attachments/assets/7f4e8388-b9a2-428c-887a-69be51e2f935" />


## Outcome
Upon completion, the script provided admin credentials for the dashboard. All core services (`wazuh-indexer`, `wazuh-manager`, `wazuh-dashboard`) were verified to be running correctly.

> <img width="1366" height="768" alt="Screenshot 2025-08-25 021621" src="https://github.com/user-attachments/assets/4decab4d-a42f-41ce-8242-a2c23c4abee4" />

**Access the Dashboard:** `https://localhost:5601`

## Verification
The successful installation was confirmed by accessing the Wazuh dashboard through a web browser on the Windows host. The dashboard provides a comprehensive overview of security events, agent status, and potential threats.

> <img width="1366" height="768" alt="Screenshot 2025-08-25 070322" src="https://github.com/user-attachments/assets/e898cf88-3271-4d92-b187-43d52d683603" />
*The Wazuh main dashboard interface, showing security events and agent status.*

## Key Lessons & Demonstrated Skills
- **Troubleshooting:** Diagnosed and resolved port conflicts and pre-existing software interference.
- **Environmental Management:** Configured WSL2 resources and managed containerized services.
- **Security Mindset:** Understood the architecture of a primary security tool used for intrusion detection and log analysis.
- **Persistence:** Navigated installation errors to achieve a fully functional outcome.

This deployment serves as a robust foundation for exploring SIEM capabilities, threat detection, and security analytics.
