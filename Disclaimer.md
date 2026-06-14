# Disclaimer

Packet Mirage is provided **for educational, defensive research, and authorized security testing purposes only**. It is designed to demonstrate concepts of network traffic obfuscation, deception, network reconnaissance, and WiFi security testing.

---

## Critical Legal Warning

⚠️ **UNAUTHORIZED USE IS ILLEGAL**

This project contains three distinct tools with different risk profiles:

### packet_mirage.py (Traffic Obfuscation)
- Generates fake HTTP, DNS, and ICMP network traffic for obfuscation and noise
- Supports multiple intensity modes: low, medium, high, max, and insane
- **Lower risk** - primarily for privacy and traffic analysis demonstration
- Use requires network access and raw socket privileges (sudo)

### arp.py (ARP Network Reconnaissance)
- Sniffs and tracks ARP (Address Resolution Protocol) activity on local networks
- Maps ARP movement patterns, identifies unique IPs, and logs traffic
- Exports findings to JSON format for analysis
- **Moderate risk** - requires explicit network owner authorization
- Network reconnaissance without permission is illegal

### wifi_poison.py (WiFi Deauthentication Attack)
- Sends deauthentication frames to disconnect WiFi clients
- Configurable power levels and attack duration
- Places interface in monitor mode for packet injection
- **HIGH RISK** - constitutes a network attack if used without authorization
- **Violations:**
  - **US:** Computer Fraud and Abuse Act (CFAA) - up to 10 years imprisonment
  - **EU:** Network and Information Systems Regulations (NIS2)
  - **UK:** Computer Misuse Act 1990
  - **Most countries:** Unauthorized network interference is a criminal offense

---

## Legal Requirements

**BEFORE using any tool in this project:**

1. ✅ You **MUST** have **explicit written permission** from the network owner/administrator
2. ✅ Testing must occur only on **networks you own or are authorized to test**
3. ✅ Comply with all **local, national, and international cybersecurity laws**
4. ✅ Understand your **legal liability** in your jurisdiction
5. ✅ Document all testing with proper **authorization records**

---

## Specific Tool Restrictions

### packet_mirage.py - Authorized Use
- Testing traffic obfuscation on your own networks
- Educational demonstrations of traffic masking
- Personal privacy experiments on networks you control
- Defensive research in isolated lab environments
- **NOT for:** Evading legitimate network monitoring, bypassing security controls, or obfuscating malicious activity

### arp.py - Authorized Use
- ARP reconnaissance on networks you own or administer
- Network diagnostics and troubleshooting
- Authorized security assessments with written scope
- Lab-based network analysis and learning
- **NOT for:** Unauthorized network mapping, surveillance without consent, or eavesdropping

### wifi_poison.py - Authorized Use
- **ONLY** authorized penetration testing on networks you own
- **ONLY** security research in controlled lab environments with isolated test networks
- **ONLY** red team exercises with written approval and rules of engagement
- **ONLY** educational demonstrations in classroom settings with instructor authorization
- **NOT for:** Disrupting others' WiFi, malicious attacks, or unauthorized network interference

---

## What This Project is NOT

❌ Not a replacement for VPNs, firewalls, or enterprise security solutions
❌ Not a tool for launching attacks on networks you don't own
❌ Not for bypassing security systems on networks without permission
❌ Not for disrupting network services or interfering with others' connectivity
❌ Not for eavesdropping or unauthorized network reconnaissance
❌ Not for any illegal or unethical purposes

---

## Insane Mode - NOT RECOMMENDED

The **"insane" intensity level** in packet_mirage.py is provided for research purposes only and comes with serious risks:

**Risks of Insane Mode:**
- 🚨 **Router Damage:** Extremely high packet rates (0.01s delays) can overwhelm and crash home/small office routers
- 🚨 **ISP Detection:** ISP monitoring systems can flag massive traffic spikes as potential attacks, leading to:
  - Account suspension or termination
  - IP address blacklisting
  - Network throttling/rate limiting
  - Legal investigation or contact
- 🚨 **Network Instability:** Can render your entire connection unusable
- 🚨 **Hardware Failure:** Repeated insane mode usage may damage networking hardware

**Who Should Use Insane Mode:**
- ✅ Only authorized penetration testers in **legal test environments**
- ✅ Only in **isolated lab networks** with permission
- ✅ Only in **enterprise legal operations** with proper authorization
- ✅ Never on ISP-provided residential internet

---

## Liability & Responsibility

The authors and contributors are **NOT responsible** for:
- Misuse of this software
- Unauthorized network access or attacks
- Criminal charges or legal consequences
- Network damage, data loss, or service disruptions
- Any violations of law arising from this project
- ARP spoofing incidents or network reconnaissance liability
- WiFi disruption or denial-of-service consequences
- Personal, civil, or criminal liability

**By downloading, installing, or using Packet Mirage, you:**
1. Accept full responsibility for your actions
2. Agree to use the software only for lawful purposes
3. Acknowledge you have obtained necessary permissions
4. Agree to comply with all applicable laws and regulations
5. Release the authors from all liability

---

## Questions?

If you're unsure whether your intended use is legal or ethical, **consult a lawyer** familiar with cybersecurity law in your jurisdiction before proceeding.

---

**Last Updated:** 2026-06-14
**Status:** Strictly Educational & Authorized Use Only

⚠️ **Remember:** With great power comes great responsibility. Use wisely, legally, and ethically.
