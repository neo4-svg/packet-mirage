# Terms of Use

**Packet Mirage - Comprehensive Terms of Service**

---

## 1. Acceptance of Terms

By downloading, installing, accessing, or using Packet Mirage (including `packet_mirage.py`, `arp.py`, `wifi_poison.py`, documentation, and all related code), you agree to be bound by these Terms of Use in their entirety.

These terms are in addition to, and not instead of, the Disclaimer.md file included in this project.

---

## 2. Definitions

- **"Software"** - The Packet Mirage project, including `packet_mirage.py`, `arp.py`, `wifi_poison.py`, documentation, and all related code
- **"packet_mirage.py"** - Traffic obfuscation tool that generates fake HTTP, DNS, and ICMP packets
- **"arp.py"** - ARP reconnaissance tool for network mapping and traffic analysis
- **"wifi_poison.py"** - WiFi deauthentication attack tool
- **"Network"** - Any computer network, WiFi network, LAN, WAN, or internet-connected infrastructure
- **"User"** - Any individual, organization, or entity downloading or using the Software
- **"Owner"** - The person or entity that owns or administers a Network
- **"Authorized Testing"** - Security testing conducted with explicit written permission from the Network Owner
- **"Unauthorized Access"** - Any use of the Software without proper authorization

---

## 3. Tool-Specific Definitions

### 3.1 Traffic Obfuscation (packet_mirage.py)
- Generates fake network traffic across HTTP, DNS, and ICMP protocols
- Supports intensity levels: low (2.0s), medium (1.0s), high (0.5s), max (0.1s), insane (0.01s)
- Requires raw socket access (sudo/root privileges)
- Lower risk profile - intended for privacy demonstration

### 3.2 Network Reconnaissance (arp.py)
- Captures and analyzes ARP packets on local networks
- Maps ARP communication patterns and IP relationships
- Generates JSON exports of network topology data
- Requires sudo/root privileges and network interface access
- Moderate risk profile - constitutes network reconnaissance

### 3.3 WiFi Attacks (wifi_poison.py)
- Sends IEEE 802.11 deauthentication frames
- Requires monitor mode interface setup
- Supports power levels: low (40 pps), medium (100 pps), high (200 pps), insane (350 pps)
- High risk profile - constitutes direct network attack

---

## 4. Licensing & Intellectual Property

- All code and documentation are provided under the applicable open-source license (see LICENSE)
- The Software is provided "AS IS" without warranty of any kind
- Users retain the right to use, modify, and distribute in accordance with the license
- **Condition:** All modifications must include these Terms of Use and Disclaimer.md
- You may not use the Software name or branding for purposes contrary to these terms

---

## 5. Mandatory Authorization Requirements

### 5.1 Explicit Written Permission

**You MUST obtain explicit written authorization before using any tool on any Network.**

- "Written permission" means documented approval (email, signed contracts, formal letters)
- Verbal permission is **NOT** sufficient
- Implied consent is **NOT** acceptable
- Permission must come directly from the Network Owner or authorized administrator
- Keep all authorization documentation for your records

### 5.2 Scope of Authorization

Your authorization must explicitly cover:
- **What networks** can be tested (by IP range, SSID, or network name)
- **Which tools** are authorized (packet_mirage.py, arp.py, wifi_poison.py, or combination)
- **Duration** of authorized testing (start and end dates)
- **Frequency** and timing of tests
- **Scope** of testing objectives and limitations

### 5.3 Tool-Specific Authorization

**packet_mirage.py Authorization:**
- Specify networks where traffic obfuscation is permitted
- Define acceptable intensity levels
- Document duration and frequency
- State purpose (research, defense testing, etc.)

**arp.py Authorization:**
- Explicitly permit network reconnaissance/mapping
- Define network scope and subnets to analyze
- Authorize data collection and JSON exports
- Specify retention and use of collected data

**wifi_poison.py Authorization:**
- **MUST be explicit and specific** for any WiFi testing
- Define target WiFi networks/BSSIDs
- Authorize specific power levels and frequencies
- Specify affected client devices or ranges
- Document rules of engagement and test windows

### 5.4 Third-Party Networks

You are **strictly prohibited** from using the Software on:
- Networks owned by third parties without authorization
- Public WiFi networks (regardless of access level)
- Corporate networks without IT department approval
- Government networks or infrastructure
- Educational networks without administrator permission
- Healthcare networks or critical infrastructure
- Financial institution networks
- Any network you do not own or lack written authorization for

---

## 6. Prohibited Uses

**The following uses are strictly prohibited:**

### 6.1 Traffic Obfuscation Misuse (packet_mirage.py)
- Using to evade legitimate network security monitoring
- Obfuscating malicious traffic or attacks
- Bypassing network security controls
- Evading intrusion detection systems (IDS/IPS)
- Masking unauthorized activities

### 6.2 Reconnaissance Misuse (arp.py)
- Unauthorized network mapping or topology discovery
- Eavesdropping on network communications
- Collecting data about networks you don't own
- Network surveillance without consent
- Creating detailed network maps for attack planning
- Sharing collected data with unauthorized parties

### 6.3 WiFi Attack Misuse (wifi_poison.py)
- Using to attack, disrupt, or interfere with any Network
- Disconnecting users without authorization
- Launching denial-of-service (DoS) attacks
- Testing networks without explicit written permission
- Any form of unauthorized network interference
- Criminal harassment through WiFi disruption

### 6.4 General Prohibited Activities
- Bypassing security measures, firewalls, or authentication
- Gaining unauthorized access to systems or data
- Evading detection from security tools with malicious intent
- Masking identity to conduct unauthorized activities
- Stealing, modifying, or accessing confidential data
- Violating privacy laws (GDPR, CCPA, HIPAA, etc.)
- Illegal, unethical, or harmful purposes
- Conducting fraud, extortion, blackmail, or criminal activity
- Impersonating authorized security personnel
- Using deceptive tactics to gain network access

---

## 7. Authorized Use Cases

The Software is authorized for use **ONLY** in the following scenarios:

### 7.1 Personal Testing on Your Own Networks
- Testing on networks that you own and administer
- Devices connected via networks you control
- Home networks you own and manage
- Personal lab or sandbox environments
- Authorized corporate networks under your administration

### 7.2 Authorized Penetration Testing
- Professional security assessments with written scope agreements
- Red team exercises with explicit authorization and rules of engagement
- Authorized vulnerability assessments by qualified professionals
- Network security testing as part of official job responsibilities
- Contractual security testing arrangements

### 7.3 Educational & Research Settings
- University lab environments with instructor authorization
- Classroom demonstrations with explicit permission
- Controlled research environments in academic settings
- Security conferences or workshops with proper authorization
- Published security research with ethical review

### 7.4 Network Administration & Maintenance
- Testing security measures on networks you administer
- Validating security controls and defenses
- Authorized network diagnostics and troubleshooting
- Operational security testing as part of your role
- Documentation and verification of network capabilities

---

## 8. Liability Disclaimer

### 8.1 No Warranty
The Software is provided "AS IS" without any warranties, express or implied, including:
- Fitness for a particular purpose
- Merchantability or non-infringement
- Accuracy or reliability of results
- Lack of bugs or defects
- Performance or stability guarantees

### 8.2 Limitation of Liability
The authors, contributors, and maintainers are **NOT responsible** for:
- Any damages, losses, or harm from use of the Software
- Criminal charges, civil lawsuits, or legal consequences
- Network disruptions, data loss, or service interruptions
- Unauthorized access or security breaches
- Violations of law or regulation
- Misuse of the Software
- Any direct, indirect, incidental, or consequential damages
- WiFi disruption, device interference, or network damage
- ARP spoofing incidents or data interception
- ISP account suspension or blacklisting

### 8.3 Indemnification
You agree to indemnify, defend, and hold harmless the authors, contributors, and maintainers from:
- Your use of the Software
- Your violation of these Terms of Use
- Your violation of any law or regulation
- Claims by third parties related to your use
- Any unauthorized or malicious use
- Any breach of authorization requirements

---

## 9. Legal Compliance Requirements

### 9.1 Applicable Laws

You agree to comply with all applicable laws and regulations, including:

**United States:**
- Computer Fraud and Abuse Act (CFAA)
- Wiretap Act and Electronic Communications Privacy Act (ECPA)
- Children's Online Privacy Protection Act (COPPA)
- FCC regulations on radio frequency interference
- State and local computer crime statutes

**European Union:**
- Network and Information Systems Regulations (NIS2)
- General Data Protection Regulation (GDPR)
- ePrivacy Directive
- National cybercrime laws

**United Kingdom:**
- Computer Misuse Act 1990
- Data Protection Act 2018
- Investigatory Powers Act 2016

**Other Jurisdictions:**
- Unauthorized computer access laws
- Network interference prohibitions
- Data protection and privacy regulations
- Wiretapping and interception laws
- Radio frequency and WiFi regulations

### 9.2 Jurisdiction-Specific Risks

**United States:**
- CFAA violations: up to 10 years imprisonment
- WiFi hacking treated as serious felony in most jurisdictions
- FCC fines for unlicensed RF transmission
- State laws may impose additional penalties

**European Union:**
- NIS2 violations: substantial fines
- GDPR violations: significant monetary penalties
- Member states have independent cybercrime laws

**United Kingdom:**
- Computer Misuse Act: up to 10 years imprisonment
- Data Protection Act: substantial fines

**Other Countries:**
- Most treat unauthorized network access as criminal offense
- Penalties range from fines to imprisonment
- Some have harsher penalties for infrastructure attacks

### 9.3 Due Diligence

Before using the Software, you must:
- Consult legal counsel in your jurisdiction
- Understand specific laws applicable to your location
- Obtain all necessary authorizations and permissions
- Document all compliance efforts
- Keep records of authorizations
- Maintain audit trails of testing

---

## 10. Authorization & Documentation Requirements

### 10.1 Required Documentation

Before conducting any testing, you **MUST** have:
- Written authorization from the Network Owner
- Scope of work document defining authorized activities
- Rules of engagement for testing
- Timeline for authorized testing activities
- Contact information for escalation
- Documentation of permissions
- For wifi_poison.py: specific target BSSIDs and approval for deauthentication

### 10.2 Record Retention

You must maintain and retain:
- All authorization documents for at least **3 years**
- Logs of all testing activities and dates
- Results and findings from testing
- Any incidents or issues encountered
- Communication with Network Owner
- Copies of authorization scope documents

### 10.3 Reporting & Transparency

When conducting authorized testing:
- Maintain transparency with the Network Owner
- Report findings promptly and securely
- Avoid unnecessary disclosure of vulnerabilities
- Follow responsible disclosure practices
- Document all activities for compliance
- Provide clear reports of test scope and results

---

## 11. Responsible Disclosure

If you discover vulnerabilities while using the Software:

### 11.1 Vulnerability Reporting
- Report findings only to the Network Owner (not publicly)
- Provide technical details to help remediation
- Allow reasonable time for fixing before disclosure
- Use secure communication channels
- Do not exploit vulnerabilities beyond testing scope

### 11.2 Coordinated Disclosure
- Work with the Network Owner on fix timeline
- Do not discuss vulnerabilities with unauthorized parties
- Follow responsible disclosure standards
- Consider embargo periods for critical vulnerabilities
- Coordinate public disclosure carefully

---

## 12. User Responsibilities

### 12.1 Your Obligations

By using the Software, you agree to:
- Take full responsibility for your actions
- Ensure all use is legal and authorized
- Obtain necessary permissions before any testing
- Comply with all applicable laws and regulations
- Respect others' networks and privacy
- Use the Software ethically and professionally
- Maintain confidentiality of findings
- Report any security incidents promptly
- Understand the specific capabilities and risks of each tool

### 12.2 Acknowledgment of Risks

You acknowledge and accept:
- The Software is powerful and can cause harm if misused
- Unauthorized use is illegal with serious consequences
- Each tool has specific legal and technical risks
- You understand the legal and ethical implications
- You have reviewed all warnings and disclaimers
- You accept full legal responsibility for your actions

---

## 13. Termination of Rights

Your right to use the Software is **immediately terminated** if you:
- Violate any provision of these Terms of Use
- Use the Software without proper authorization
- Engage in any prohibited activity
- Break any applicable law
- Misuse the Software for attacks or harm
- Attempt to circumvent authorization requirements

Upon termination, you must:
- Cease all use immediately
- Uninstall the Software
- Destroy all copies in your possession
- Delete any findings or data collected

---

## 14. No Support or Maintenance

- The Software is provided without support or maintenance
- The authors make no guarantee of continued availability
- Bug fixes, patches, or improvements are not guaranteed
- You are responsible for staying informed of security issues
- Use at your own risk regarding compatibility and security

---

## 15. Modifications to Terms

The authors reserve the right to modify these Terms of Use at any time. Continued use after modifications constitutes acceptance.

---

## 16. Entire Agreement

These Terms of Use, together with the Disclaimer.md file, constitute the entire agreement between you and the authors regarding the Software.

---

## 17. Governing Law & Jurisdiction

- These terms are governed by applicable laws where you reside
- You are responsible for understanding and complying with local laws
- The authors disclaim liability for violations of local or international law
- You waive any claim that these terms are unenforceable in your location

---

## 18. Final Acknowledgment

**By using Packet Mirage, you explicitly acknowledge and agree to:**

1. ✅ You have read and understood all terms herein
2. ✅ You understand the legal consequences of unauthorized use
3. ✅ You will obtain explicit written authorization before testing any network
4. ✅ You will use each tool only for lawful and authorized purposes
5. ✅ You accept full responsibility and liability for your actions
6. ✅ You release the authors from all liability and claims
7. ✅ You understand violations may result in criminal prosecution
8. ✅ You have consulted legal counsel if uncertain about your jurisdiction's laws
9. ✅ You understand each tool's specific risks and capabilities
10. ✅ You will not use these tools for unauthorized network interference

---

**Last Updated:** 2026-06-14
**Status:** Strictly Educational & Authorized Use Only

⚠️ **READ THIS CAREFULLY. YOUR LEGAL FREEDOM DEPENDS ON IT.**

This software requires authorized use. Unauthorized use is a federal crime in most countries.
If you're unsure whether your intended use is legal, **stop and consult a lawyer immediately.**
