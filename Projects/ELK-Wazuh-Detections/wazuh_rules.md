# Complete Task Documentation: Creating Custom Wazuh Rule

## Objective
Created a custom Wazuh rule to detect failed SSH password attempts and document the process.

---

## Step 1: Accessing the Wazuh Rules Directory

### Command Used:
```
cd /var/ossec/etc/rules/
```

### Explanation:
- /var/ossec/ is the main Wazuh installation directory
- etc/rules/ contains custom rule files
- local_rules.xml is where user-defined rules are stored

### Permission Requirement:
```
sudo su -  # Switch to root user for administrative access
```
*Necessary because Wazuh files are owned by root/wazuh users*

> <img width="1366" height="768" alt="Screenshot 2025-08-30 072709" src="https://github.com/user-attachments/assets/cb58d4f1-8350-4081-9e3b-f3922c8c31dd" />

---

## Step 2: Checking Existing Rules File

### Command Used:
```
ls -la local_rules.xml
```

### What We Found:
- File existed with default content
- Ownership: wazuh:wazuh
- Permissions: -rw-rw---- (read-write for owner/group only)

### Initial Content:
```xml
<!-- Default local rules template -->
<group name="local,syslog,sshd,">
  <rule id="100001" level="5">
    <if_sid>5716</if_sid>
    <srcip>1.1.1.1</srcip>
    <description>sshd: authentication failed from IP 1.1.1.1.</description>
    <group>authentication_failed,pci_dss_10.2.4,pci_dss_10.2.5,</group>
  </rule>
</group>
```

---

## Step 3: Editing the Rules File

### Command Used:
```
nano local_rules.xml
```

### Rule Added:
```xml
<rule id="100051" level="5">
  <match>Failed password</match>
  <description>SSH authentication failed: Failed password attempt.</description>
  <group>authentication_failed,pci_dss_10.2.4,pci_dss_10.2.5,</group>
</rule>
```

### Rule Components Explained:
- id="100051": Custom rule ID (100000-109999 range)
- level="5": Medium severity level
- <match>Failed password</match>: Pattern to detect in logs
- description: Human-readable rule description
- group: Compliance and categorization tags

---

## Step 4: Restarting Wazuh Service

### Command Used:
```
sudo systemctl restart wazuh-manager
```

### Why Required:
- Wazuh loads rules at startup
- Restart needed to apply configuration changes
- Ensures new rules are active in memory

---

## Step 5: Testing SSH Connections

### Commands Used:
```
ssh invaliduser@localhost
ssh testuser@localhost
```

### Problems Encountered:
1. SSH Server Not Running: Connection refused error
2. Host Key Changes: WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!
3. Authentication Failures: Multiple Permission denied messages

### Solutions Applied:
```
ssh-keygen -f "/home/aisha/.ssh/known_hosts" -R "localhost"
```
*This removed old host keys and allowed new connections*

> <img width="1366" height="768" alt="Screenshot 2025-08-30 073018" src="https://github.com/user-attachments/assets/ebae66dd-1bee-4b2d-bbd9-2335b37bef98" />

---

## Step 6: Verification and Troubleshooting

### Checking Logs:
```
sudo tail -n 20 /var/ossec/logs/alerts/alerts.log
sudo tail -n 10 /var/log/auth.log
```

### Issues Identified:
1. Rule Not Triggering: Built-in rule 5710 was catching events first
2. Different Log Format: WSL generated Invalid user instead of Failed password
3. Rule Processing Order: Wazuh stops at first matching rule

### Testing with Logtest:
```
echo "Failed password log message" | sudo /var/ossec/bin/wazuh-logtest
```
*Used to verify rule syntax without environmental variables*

---

## Step 7: Rule Optimization

### Final Rule Structure:
```xml
<rule id="100051" level="5">
  <if_sid>5710</if_sid>
  <description>SSH authentication failed: Custom rule for failed password attempts.</description>
  <group>authentication_failed,pci_dss_10.2.4,pci_dss_10.2.5,</group>
</rule>
```

### Key Changes:
1. Added <if_sid>5710</if_sid>: Chains after built-in SSH rule
2. Removed <match>: Let parent rule handle pattern matching
3. Kept same ID and groups: Maintained compliance requirements

> <img width="1366" height="768" alt="Screenshot 2025-08-30 084027" src="https://github.com/user-attachments/assets/d54a1704-8376-463a-a56b-97896b96eaa7" />


---

## Step 8: Final Validation

### Successful Test:
```
echo "Test log message" | sudo /var/ossec/bin/wazuh-logtest 2>&1 | grep "100051"
```
*Output: id: '100051' - confirming rule activation*

### Service Status Check:
```
sudo systemctl status wazuh-manager
```
*Verified Wazuh was running properly after changes*

---

## Technical Challenges Overcome

1. Permission Issues: Required root access for configuration changes
2. Rule Priority: Built-in rules took precedence over custom rules
3. WSL Limitations: Different SSH logging behavior than standard Linux
4. XML Syntax: Learned proper rule structure and formatting
5. Service Management: Understanding Wazuh restart requirements

---

## Learning Outcomes

1. Wazuh Rule Architecture: Understanding how rules are processed in order
2. XML Configuration: Proper syntax for Wazuh rule definitions
3. Troubleshooting Methodology: Systematic approach to debugging rule issues
4. SSH Authentication: How SSH logs authentication attempts in different environments
5. Compliance Integration: Using PCI DSS and other compliance tags appropriately

---

## Final Result
✅ Successfully created and tested custom Wazuh rule 100051  
✅ Rule triggers for SSH authentication failures  
✅ Integrated with existing Wazuh ruleset  
✅ Maintained compliance requirements  
✅ Documented entire process for future reference  

The rule is now active and monitoring for SSH authentication failures in the Wazuh environment.

## Wazuh Dashboard Integration

### 1. OpenSearch Dashboards Interface

> <img width="1366" height="768" alt="Screenshot 2025-08-30 093047" src="https://github.com/user-attachments/assets/677ee7c0-c35c-432b-8564-e398f86b3a9e" />

*OpenSearch Dashboards welcome screen - entry point to Wazuh interface*

### 2. Security Events Section  
<img width="1366" height="768" alt="Screenshot 2025-08-30 092546" src="https://github.com/user-attachments/assets/31351c1c-1198-46cd-9024-e98ac91fbdf0" />

*Security events section where alerts from rule 100051 would appear*

### 3. Rule Validation Evidence
<img width="1366" height="768" alt="Screenshot 2025-08-30 092413" src="https://github.com/user-attachments/assets/c0131f12-43be-45b8-beed-d9069e4a4020" />

*Successful rule testing via wazuh-logtest showing rule 100051 triggering*
