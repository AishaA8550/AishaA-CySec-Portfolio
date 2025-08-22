# Day 1: Networking Basics - Core Concepts & Hands-On Labs

## Theory Summary

Today I explored the fundamental building blocks of how computers communicate. Key concepts I learned:

**IP Address:** A unique identifier for a device on a network, similar to a home address.
- **Public IP:** The address the internet sees for your entire network (found by searching "what is my ip" on Google)
- **Private IP:** The address assigned to a device within a local network (e.g., `192.168.1.101` on your home Wi-Fi)

**DNS (Domain Name System):** The "phonebook of the internet." It translates human-readable domain names (like `google.com`) into machine-readable IP addresses (like `142.251.42.206`).

**Protocols:** Rules for communication. Key ones include:
- **ICMP:** Used by `ping` for testing connectivity
- **TCP & UDP:** Protocols for sending data. TCP is reliable (used for web, email), UDP is fast (used for video streaming)

**Traceroute:** A diagnostic tool that shows the path (and delays) packets take to reach a network host.

## Hands-On Lab Exercises

I used command-line tools to apply these concepts practically on my Linux system.

### Lab 1: Discover Your Network Identity
**Command:** `ip a`  
**Purpose:** To find my machine's private IP address and network interface details.  
**Screenshot:** <img width="1366" height="768" alt="lab1-ip-command" src="https://github.com/user-attachments/assets/9d7117cd-4140-4f2e-8167-9ee836945501" />

### Lab 2: Query the DNS Phonebook
**Command:** `nslookup google.com`  
**Purpose:** To manually perform a DNS lookup and see the IP address(es) associated with a domain name.  
**Screenshot:** <img width="1366" height="768" alt="lab2-nslookup-output" src="https://github.com/user-attachments/assets/7c764d97-75e4-4003-bb63-f8f0f65921af" />


### Lab 3: Test Network Connectivity
**Command:** `ping 8.8.8.8`  
**Purpose:** To use the ICMP protocol to test if I can reach a reliable host (Google's DNS server) and measure the response time (latency).  
**Screenshot:** <img width="1366" height="768" alt="lab3-ping-output" src="https://github.com/user-attachments/assets/98cf0cf8-8ac1-4b7f-b85d-a1e024fe661b" />


### Lab 4: Trace the Network Path
**Command:** `traceroute 8.8.8.8`  
**Purpose:** To see the sequence of routers (hops) my data passes through to get from my computer to its final destination. This is crucial for diagnosing where network delays or failures occur.  
**Screenshot:** <img width="1366" height="768" alt="lab4-traceroute-output" src="https://github.com/user-attachments/assets/3687b60b-82a1-449e-808b-310de3993e85" />


## Key Takeaway

Understanding these core concepts and tools is the first step in cybersecurity. To defend a network or investigate an attack, you must first understand how it normally functions. These commands are the baseline for any network troubleshooting or monitoring task.

**Resources:** TryHackMe
