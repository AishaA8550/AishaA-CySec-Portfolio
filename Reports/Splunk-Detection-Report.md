# Splunk Detection Report: SSH Brute Force Attack

## Overview
This report details a simulated detection of an SSH brute force attack using Splunk SPL queries against a sample `secure.log` file.

## Detection Details
- **Data Source:** `linux:audit` / `secure.log`
- **Attack Technique:** T1110 - Brute Force
- **Splunk Query:**
  ```splunk
  source="secure.log" "Failed password" 
  | stats count as failed_attempts by src_ip 
  | where failed_attempts > 10 
  | sort - failed_attempts
  ```

## Findings
The query identified the following suspicious activity:
- **Source IP:** `192.168.1.22` - **Attempts:** 158
- **Source IP:** `10.0.0.5` - **Attempts:** 87

## Conclusion
The high volume of failed SSH login attempts from singular source IPs indicates a brute force attack. Immediate blocking of these IPs at the firewall is recommended.
