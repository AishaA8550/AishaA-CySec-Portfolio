## How I Enhanced Threat Detection with Custom Wazuh Rules

As a cybersecurity enthusiast building my home lab, I discovered that while Wazuh provides excellent out-of-the-box security monitoring, true defensive power comes from customizing detection rules for specific threats. My journey into custom rule creation began with addressing two critical threats: SSH brute force attacks and cryptomining operations.

## The Rule Creation Process

### Starting with SSH Authentication Monitoring

I first tackled SSH security by creating rules to detect failed authentication attempts. Accessing the Wazuh rules directory required administrative privileges:

```bash
cd /var/ossec/etc/rules/
sudo nano local_rules.xml
```

The initial challenge was understanding rule hierarchy. Wazuh processes rules sequentially, and my custom rule for "Failed password" patterns wasn't triggering. After investigation, I discovered that built-in rule 5710 was catching these events first. The solution was rule chaining:

```xml
<rule id="100051" level="5">
  <if_sid>5710</if_sid>
  <description>SSH authentication failed: Custom rule detection</description>
  <group>authentication_failed,pci_dss_10.2.4,pci_dss_10.2.5,</group>
</rule>
```

This taught me a valuable lesson: custom rules should complement rather than replace existing detection mechanisms.

### Escalating to Cryptomining Detection

Cryptominers represent a significant threat—they consume resources, indicate system compromise, and often serve as entry points for more severe attacks. I implemented a two-layer detection strategy:

**Layer 1: Mining Pool Communications**
```xml
<rule id="100100" level="10">
  <match>pool.minexmr.com|xmr.pool.minergate|eth.2miners.com|stratum+tcp</match>
  <description>Crypto miner pool connection detected</description>
  <group>cryptomining,attack</group>
</rule>
```

**Layer 2: Miner Executable Detection**
```xml
<rule id="100101" level="12">
  <match>xmrig|ccminer|cgminer|bfgminer|minerd</match>
  <description>Crypto miner executable detected</description>
  <group>cryptomining,attack,malware</group>
</rule>
```

The level 12 severity for executable detection reflects the critical nature of this finding—it indicates active malware execution rather than just suspicious connections.

## Testing and Validation Methodology

Creating rules is only half the battle; thorough testing ensures they work as intended. I used multiple validation approaches:

1. **Synthetic Testing**: Generating test events using logger commands
2. **Logtest Utility**: Validating rule syntax with `wazuh-logtest`
3. **Service Management**: Restarting Wazuh-manager after rule changes
4. **Alert Verification**: Monitoring `/var/ossec/logs/alerts/alerts.log`

The testing commands revealed the rules' effectiveness:
```bash
echo "process xmrig miner started connecting to pool.minexmr.com" | logger
```

## Real-World Impact and Lessons

The custom rules immediately proved their value by detecting simulated attack patterns. More importantly, the process taught me crucial security monitoring principles:

**Correlation Over Isolation**: Single events might be ambiguous, but multiple related alerts create high-confidence detections. A miner executable combined with pool connections is unmistakable malicious activity.

**Progressive Rule Development**: Start simple and iterate. My initial SSH rule evolved through multiple versions as I understood Wazuh's rule processing logic.

**Documentation is Critical**: Maintaining detailed records of rule purposes, testing procedures, and modification history ensures long-term maintainability.

## Conclusion

Building custom Wazuh rules transformed my approach to security monitoring. Moving from passive observation to active threat hunting empowered me to address specific risks in my environment. The process demonstrated that effective security isn't just about having tools—it's about tailoring them to your unique threat landscape. Whether defending against credential stuffing or resource theft, custom rules turn a generic SIEM into your personal security sentinel.

---
