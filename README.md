# Packet Mirage

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Packet Mirage** is a lightweight network toolkit that provides three powerful Python tools for network obfuscation, reconnaissance, and WiFi security testing.

It blends noise generation (HTTP, DNS, ICMP) with network analysis capabilities, making it useful for defensive research, authorized security testing, and educational demonstrations.

---

## 📋 What's Included

Packet Mirage contains three distinct tools:

| Tool | Purpose | Risk Level | Key Features |
|------|---------|-----------|---------------|
| **packet_mirage.py** | Traffic Obfuscation | Lower | HTTP/DNS/ICMP noise, 5 intensity levels |
| **arp.py** | Network Reconnaissance | Moderate | ARP mapping, topology discovery, JSON export |
| **wifi_poison.py** | WiFi Security Testing | **HIGH** | Deauth attacks, monitor mode, configurable power |

---

## ⚠️ Critical Legal Notice

**UNAUTHORIZED USE IS ILLEGAL** - Each tool has specific legal implications:

- **packet_mirage.py:** Lower risk, requires authorization for evading monitoring
- **arp.py:** Moderate risk, network reconnaissance requires written permission
- **wifi_poison.py:** **HIGH RISK** - constitutes network attack without authorization

**All tools require explicit written permission from network owners before use.**

Violations can result in:
- 🚨 Up to **10 years imprisonment** (CFAA, Computer Misuse Act)
- 💰 Substantial fines (GDPR, NIS2, state laws)
- 🔒 Criminal prosecution in most jurisdictions

**Before proceeding, read [Disclaimer.md](Disclaimer.md) and [terms_of_use.md](terms_of_use.md) carefully.**

---

## Installation

```bash
git clone https://github.com/neo4-svg/packet-mirage.git
cd packet-mirage
pip install scapy  # Required for all tools
```

---

## 🔧 Tool Documentation

### 1. packet_mirage.py - Traffic Obfuscation

Generates randomized fake network traffic to mask real activity.

#### Quick Start

```bash
sudo python3 packet_mirage.py
```

#### Interactive Prompts

**Select Mode:**
- `http` - Fake HTTP requests
- `dns` - Fake DNS queries
- `icmp` - Fake ICMP ping requests
- `mixed` - Random combination of all types

**Select Intensity:**
- `low` - 2.0s delay between packets (gentle)
- `medium` - 1.0s delay (default, balanced)
- `high` - 0.5s delay (aggressive)
- `max` - 0.1s delay (very aggressive)
- `insane` - 0.01s delay (extreme - **NOT RECOMMENDED**, see warnings)

**Duration:**
- Enter time in seconds for limited duration
- Leave blank for infinite runtime

#### Example Session

```
=== Packet Mirage ===
Select mode [http/dns/icmp/mixed]: mixed
Select intensity [low/medium/high/max/insane]: high
Duration in seconds (blank = infinite): 120
Running Mirage: mode=mixed, intensity=high, duration=120s
```

#### How It Works

- **HTTP Mode:** Sends random HTTP GET requests to example.com (port 80)
- **DNS Mode:** Sends random DNS queries to 8.8.8.8 (port 53)
- **ICMP Mode:** Sends random ICMP packets to 8.8.8.8
- **Mixed Mode:** Randomly selects between HTTP, DNS, and ICMP each iteration

#### Requirements

- sudo/root privileges (for raw socket access)
- Linux only

---

### 2. arp.py - Network Reconnaissance

Sniffs and analyzes ARP (Address Resolution Protocol) activity to map network relationships.

#### Quick Start

```bash
sudo python3 arp.py
```

#### Features

- **ARP Movement Tracking** - Maps IP-to-IP communication patterns
- **Network Statistics** - Tracks unique IPs, packet counts, top talkers
- **ARP Frequency Heatmap** - Visual representation of ARP activity
- **JSON Export** - Exports network topology data for analysis
- **Real-time Logging** - Logs ARP activity to `arp_log.txt`

#### Interactive Setup

1. **Legal Confirmation:** Tool asks if running in legal environment
2. **Interface Detection:** Auto-detects suitable network interface
3. **ARP Sniffing:** Begins capturing and analyzing ARP packets

#### Output Tables

**ARP Movement Map:**
```
Source IP      | Targets
192.168.1.1    | 192.168.1.100, 192.168.1.101
192.168.1.100  | 192.168.1.1, 192.168.1.254
```

**ARP Statistics:**
```
Metric           | Value
Total ARP Packets | 1024
Unique IPs Seen   | 42
Top Talker        | 192.168.1.1
```

#### File Outputs

- **arp_log.txt** - Line-by-line ARP activity log
- **arp_export.json** - JSON export of network topology and statistics

#### Requirements

- sudo/root privileges
- Linux only
- Scapy library
- Permission from network owner

#### Example Output

```json
{
  "arp_graph": {
    "192.168.1.1": ["192.168.1.100", "192.168.1.101"],
    "192.168.1.100": ["192.168.1.1", "192.168.1.254"]
  },
  "unique_ips": ["192.168.1.1", "192.168.1.100", "192.168.1.101"],
  "packet_count": 1024,
  "arp_frequency": {"192.168.1.1": 512, "192.168.1.100": 256}
}
```

---

### 3. wifi_poison.py - WiFi Security Testing

Sends IEEE 802.11 deauthentication frames for WiFi penetration testing.

#### ⚠️ CRITICAL: HIGH RISK TOOL

**This tool sends direct attacks to WiFi networks. Unauthorized use is a criminal offense.**

#### Quick Start

```bash
sudo python3 wifi_poison.py
```

#### Prerequisites

1. **Wireless Interface:** Must support monitor mode (common on Linux)
2. **Monitor Mode Setup:** Tool auto-configures interface
3. **Written Authorization:** You must have explicit permission to test target network
4. **Target Information:** Need WiFi BSSID (MAC address) and target client MACs

#### Interactive Setup

**Monitor Interface:**
- Default: `wlan0mon`
- Tool automatically puts interface in monitor mode
- Removes from monitor mode after attack

**Target Router BSSID:**
- Enter WiFi router's MAC address
- Example: `AA:BB:CC:DD:EE:FF`
- Use WiFi scanning tools to find BSSID

**Target Client MAC:**
- Specific client MAC to disconnect, or
- Leave blank for `ff:ff:ff:ff:ff:ff` (all clients)

**Power Levels:**
- `low` - 40 packets/sec (soft disconnect)
- `medium` - 100 packets/sec (good effect, default)
- `high` - 200 packets/sec (strong attack)
- `insane` - 350 packets/sec (very aggressive)

**Duration:**
- Specify attack duration in seconds (default: 15)

#### Example Session

```
=== Packet Mirage - WiFi Poison Mode ===

Enter monitor interface [wlan0mon]: wlan0mon
[+] Putting wlan0 into monitor mode...
[+] Monitor mode activated.

Are you running this in a legal environment? [y/n] > y

Enter Target Router BSSID (MAC Address): AA:BB:CC:DD:EE:FF
Target Client MAC (press Enter for all clients): 
Choose power level (medium): high
Attack duration in seconds (15): 30

🚀 Starting HIGH WiFi Poison Attack...
Target AP   : AA:BB:CC:DD:EE:FF
Target Client: ff:ff:ff:ff:ff:ff
Duration    : 30 seconds
Power       : HIGH (200 packets/sec)

[+] Sent 300 deauth packets...
✅ Attack finished. 1200 packets sent.
Clients should reconnect automatically.
```

#### Technical Details

- **Protocol:** IEEE 802.11 Deauthentication Frames
- **Mechanism:** Sends deauth frames with reason code 7 (CLASS3_FRAME_FROM_NONASSOC_STA)
- **Effect:** Forces WiFi clients to disconnect and reconnect
- **Duration:** Configurable attack window

#### Safety & Legal

✅ **Authorized Use:**
- Your own WiFi networks
- Written authorization from network owner
- Penetration testing contracts
- Controlled lab environments
- Classroom demonstrations with permission

❌ **Prohibited:**
- Any network without explicit written authorization
- Public WiFi networks
- Neighbor networks
- Corporate networks without IT approval
- Malicious disruption or harassment

#### Requirements

- sudo/root privileges
- Linux only
- WiFi adapter with monitor mode support
- Scapy library
- **Explicit written authorization from network owner**

---

## Requirements

- **Linux** (macOS/Windows not supported - no raw sockets)
- **Python 3.8+**
- **sudo/root privileges** (all tools require raw socket or monitor mode access)
- **Scapy** (for packet crafting and WiFi functionality)

Install dependencies:

```bash
sudo pip install scapy
```

---

## 🚨 Warnings & Security Notes

### Insane Mode - NOT RECOMMENDED

The "insane" intensity in packet_mirage.py (0.01s delay) carries serious risks:

**Risks:**
- 🔥 Can crash home/small office routers
- 🚨 ISP monitoring systems may flag as attack (account suspension, IP blacklisting)
- 💥 May render entire network unusable
- ⚠️ Can damage networking hardware

**Safe Alternative:** Use `high` intensity (0.5s delay) for normal operations.

### WiFi Poison Legal Risks

Unauthorized WiFi attacks can result in:
- **10+ years imprisonment** (CFAA - US)
- **Criminal prosecution** (most countries)
- **Civil liability** from network owners
- **FCC fines** for RF interference

### Network Reconnaissance Risks

Unauthorized ARP sniffing/mapping can result in:
- **Computer Misuse Act violations** (UK, up to 10 years)
- **Unauthorized access charges** (CFAA - US)
- **NIS2 violations** (EU, significant fines)
- **Civil liability** from network owners

---

## How It Works

### packet_mirage.py
- Creates raw TCP/UDP sockets
- Generates random packets to specified destinations
- Sends at configurable intervals
- Provides traffic obfuscation through noise

### arp.py
- Uses Scapy to sniff network packets
- Filters for ARP protocol frames
- Builds graph of IP relationships
- Tracks packet frequency and communication patterns
- Exports data in JSON format

### wifi_poison.py
- Enables monitor mode on wireless interface
- Crafts IEEE 802.11 deauthentication frames
- Injects frames at specified power level
- Manages interface mode setup/teardown

---

## Legal & Ethical

By using Packet Mirage, you agree to:
- ✅ Obtain explicit written authorization before testing any network
- ✅ Use tools only for lawful purposes
- ✅ Comply with all applicable laws (CFAA, Computer Misuse Act, NIS2, etc.)
- ✅ Accept full legal responsibility for your actions
- ✅ Not use tools for unauthorized attacks or harm

**See [Disclaimer.md](Disclaimer.md) and [terms_of_use.md](terms_of_use.md) for complete legal information.**

---

## License

MIT License - See [LICENSE](LICENSE) for details

---

## References

- **Scapy Documentation:** https://scapy.readthedocs.io/
- **IEEE 802.11 Deauthentication:** RFC 802.11
- **ARP Protocol:** RFC 826
- **Computer Fraud and Abuse Act:** https://www.law.cornell.edu/uscode/text/18/1030
- **Computer Misuse Act 1990:** https://www.legislation.gov.uk/ukpga/1990/18/contents
- **GDPR:** https://gdpr-info.eu/

---

**Made by @neo4-svg** | Educational Security Research Tool

⚠️ **Remember:** With great power comes great responsibility. Use wisely, legally, and ethically.
