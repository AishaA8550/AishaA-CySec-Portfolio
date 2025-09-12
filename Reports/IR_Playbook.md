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


## Active Incident Handling: The CSF Community Profile (DETECT, RESPOND, RECOVER)

This profile details the outcomes required for the active management of incidents. These activities are often performed concurrently.

### DETECT (DE) - Discovery
*High-Priority Outcomes include:*
- **DE.AE (Anomalies & Events):** Potential incidents are detected and reported (via tools and users).
- **DE.CT (Continuous Monitoring):** The network and systems are monitored to identify potential incidents.

### RESPOND (RS) - Action
This function is broken into key categories:
- **RS.MA (Incident Management):**
  - **RS.MA-1:** Incidents are **triaged and prioritized** based on impact.
  - **RS.MA-2:** Incidents are escalated appropriately.
- **RS.AN (Analysis):**
  - **RS.AN-1:** Incidents are investigated to determine impact and root cause.
  - **RS.AN-2:** **Forensic data is collected and preserved.**
  - **RS.AN-3:** Incidents are categorized (e.g., ransomware, data breach).
- **RS.MI (Mitigation):**
  - **RS.MI-1:** **Containment** actions are taken (e.g., isolate network).
  - **RS.MI-2:** **Eradication** actions are taken (e.g., patch, remove malware).
- **RS.CO (Communication):** **(Critical)**
  - **RS.CO-1:** Response activities are coordinated with internal/external stakeholders (Legal, PR, HR).
  - **RS.CO-2:** Information is shared consistent with response plans.

### RECOVER (RC) - Restoration
*High-Priority Outcomes include:*
- **RC.RP (Recovery Planning):** Recovery plans are executed to restore systems and operations.
- **RC.IM (Improvement):** Recovery processes are improved.

> **Key Insight:** The RESPOND function is not a linear step-by-step process. Analysis (RS.AN) informs mitigation (RS.MI), while management (RS.MA) and communication (RS.CO) happen continuously throughout the incident.


## Putting It All Together: Coordination, Lifecycle Execution & Best Practices

The theoretical model and profiles are applied through continuous coordination, clear execution, and adherence to overarching best practices.

### Coordination & Communication: The IR Team Sport
Effective incident response requires seamless coordination that extends far beyond the core IR team. This is the practical execution of the **RS.CO** outcomes.
- **Internal Stakeholders:**
  - **Leadership (GOVERN):** Provides strategic direction, resource allocation, and approves major decisions (e.g., taking systems offline).
  - **Legal Counsel:** Advises on regulatory obligations (e.g., data breach notifications), evidence preservation, and interactions with law enforcement.
  - **Human Resources (HR):** Manages incidents involving employees (e.g., insider threats).
  - **Public Relations / Communications:** Develops and releases external and internal statements to manage reputation and provide clear messaging.
- **External Stakeholders:**
  - **Information Sharing Organizations (e.g., ISACs):** Share threat indicators to help others and receive contextual information.
  - **Law Enforcement (e.g., FBI):** Involved in cases of cybercrime. Requires careful evidence handling.
  - **Government Agencies (e.g., CISA):** Can provide technical assistance and resources.
  - **Partners & Vendors:** Critical in supply chain incidents.

### Executing the Lifecycle: A Non-Linear Narrative
The CSF-based lifecycle is a guide for dynamic, concurrent activities. The following illustrates how the functions interact in practice:

1.  **Preparation (Ongoing - GOVERN, IDENTIFY, PROTECT):**
    - The organization maintains policies (**GV**), an asset inventory (**ID.AM**), and security controls (**PR**).
    - **Example:** A company has patched its systems (PR.IP) and trained users to report phishing (PR.AT).

2.  **Detection (DETECT):**
    - An anomaly is identified.
    - **Example:** A user reports a suspicious email (DE.AE), which is caught by a monitoring tool (DE.CT).

3.  **Response (RESPOND):**
    - This is not a sequence but a set of parallel actions:
        - **RS.MA (Manage):** The event is triaged as a high-priority potential phishing incident.
        - **RS.AN (Analyze):** The email is analyzed; it's found to contain a malicious link. Impact is assessed.
        - **RS.MI (Mitigate):** Based on initial analysis, the URL is blocked, and the email is purged from all mailboxes (Containment).
        - **RS.CO (Communicate):** The IT team is notified. A warning is sent to all staff. Legal is briefed.

4.  **Recovery (RECOVER):**
    - **RC.RP:** A few machines that clicked the link are investigated, cleaned, and restored to normal operation.

5.  **Improve (Continuous - ID.IM):**
    - **During:** The analysis reveals the email bypassed a filter rule. The rule is immediately updated (**PR.IP**).
    - **After:** A lesson-learned review leads to an update in phishing training materials (**PR.AT**) and the IR playbook itself (**GV.PO**).

### Overarching Best Practices
- **Document Everything:** Maintain detailed logs of all actions, decisions, and findings during an incident. This is crucial for analysis, legal requirements, and improvement.
- **Leverage Automation:** Use automation to accelerate detection (DE), containment (RS.MI - e.g., auto-isolating a host), and forensic data collection (RS.AN).
- **Measure Effectiveness:** Track metrics like Mean Time to Detect (MTTD) and Mean Time to Respond (MTTR) to gauge IR performance and identify areas for improvement (**ID.IM**), reporting to leadership (**GV.OV**).

> **Final Key Insight:** The modern NIST IR lifecycle is a dynamic, integrated, and continuous risk management process. Communication (RS.CO) is its bloodstream, and improvement (ID.IM) is its nervous system, ensuring the organization learns and adapts faster than the threat evolves.

*Documentation Status: Complete. Analysis of NIST SP 800-61r3 finalized. Playbook includes philosophy, profiles, and practical execution.*
