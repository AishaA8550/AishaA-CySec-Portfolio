# NIST SP 800-61r3 Incident Response Playbook

## Overview
This document is a personal summary and interpretation of the **NIST Special Publication 800-61 Revision 3** (Computer Security Incident Handling Guide, April 2025). It serves as a foundational playbook for modern incident response practices integrated into the NIST Cybersecurity Framework (CSF) 2.0.

## Table of Contents
- [Philosophy Shift: Integration over Isolation](#philosophy-shift-integration-over-isolation)
- [The CSF 2.0 Core as the New IR Model](#the-csf-20-core-as-the-new-ir-model)
- [Core Functions & IR Responsibilities](#core-functions--ir-responsibilities)

---

## Philosophy Shift: Integration over Isolation

### The Old Model (NIST SP 800-61 Rev 2)
- Incident Response was treated as a **separate, distinct process**.
- It was visualized as a **four-stage cycle**:
  1.  Preparation
  2.  Detection & Analysis
  3.  Containment, Eradication, & Recovery
  4.  Post-Incident Activity
- **Limitation:** This model could become isolated from the organization's overall business risk and strategy. Improvement was a periodic "final step."

### The New Model (NIST SP 800-61 Rev 3)
- **IR is fully integrated into the NIST Cybersecurity Framework (CSF) 2.0.**
- **IR is a core part of overall Cybersecurity Risk Management.**
- This means IR is not just an IT problem; it's a **business risk problem**.
- It involves **everyone**: Executive leadership (GOVERN), system owners (IDENTIFY/PROTECT), communications, legal, and HR (during RESPOND).

## The CSF 2.0 Core as the New IR Model

The new incident response life cycle is mapped directly to the six functions of the CSF 2.0 Core, with **IMPROVE (ID.IM)** as a continuous feedback mechanism.

| CSF 2.0 Function | IR Phase | Description |
| :--- | :--- | :--- |
| **GOVERN** | Continuous Preparation | Leadership establishes IR strategy, policies, roles, and provides oversight. |
| **IDENTIFY** | Continuous Preparation | Understanding assets, risks, and vulnerabilities to enable prioritization during an incident. |
| **PROTECT** | Continuous Preparation | Implementing safeguards (training, access control, patching) to prevent incidents. |
| **DETECT** | Active Handling | Activities that discover and alert on a potential incident. |
| **RESPOND** | Active Handling | The analysis, containment, and mitigation actions taken during an incident. |
| **RECOVER** | Active Handling | Restoring systems and services to normal operation. |
| **IMPROVE (ID.IM)** | **Continuous Feedback** | Lessons learned are fed back into **all functions** continuously, not just at the end. |

## Core Functions & IR Responsibilities

- **GOVERN (GV):** Strategy, policy, roles, funding.
- **IDENTIFY (ID):** Asset management, risk assessment, prioritization.
- **PROTECT (PR):** Security controls, awareness training, patching.
- **DETECT (DE):** Monitoring, anomaly detection, event analysis.
- **RESPOND (RS):** Triage, analysis (RS.AN), containment (RS.MI), communication (RS.CO).
- **RECOVER (RC):** Recovery planning, system restoration, verification.
- **IMPROVE (ID.IM):** Applying lessons learned to update all of the above functions without delay.

---
## Preparation: The CSF Community Profile (GOVERN, IDENTIFY, PROTECT)

NIST provides a prioritized list of outcomes (a "Community Profile") for IR preparedness. These are the continuous activities that form the foundation of response capabilities.

### GOVERN (GV) - The Strategy
*High-Priority Outcomes include:*
- **GV.IR (Strategy):** IR strategy is aligned with organizational mission and priorities.
- **GV.PO (Policies):** IR policies are established, published, and enforced.
- **GV.OV (Oversight):** Leadership provides oversight of IR preparedness.
- **GV.RM (Risk Management):** Cybersecurity risks are understood and inform IR planning.

### IDENTIFY (ID) - Knowledge of Environment
*High-Priority Outcomes include:*
- **ID.AM (Asset Management):** **Hardware, devices, data, and software are inventoried.** (Critical for prioritization).
- **ID.RA (Risk Assessment):** Threats and vulnerabilities are identified.
- **ID.IM (Improvement):** IR plans are improved based on lessons learned and exercises.

### PROTECT (PR) - Proactive Controls
*High-Priority Outcomes include:*
- **PR.AA (Identity Management):** Access to assets is managed. (Essential for investigation/containment).
- **PR.DS (Data Security):** Data is protected.
- **PR.IP (Security Infrastructure):** Logging and monitoring configurations are managed. (**Foundation for Detection**).
- **PR.AT (Awareness & Training):** Users are trained to report anomalies.

> **Key Insight:** The "Preparation" phase is not a one-time activity. It is the daily execution of the GOVERN, IDENTIFY, and PROTECT functions, guided by high-priority IR outcomes.
