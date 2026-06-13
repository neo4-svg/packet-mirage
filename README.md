# Packet Mirage

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Packet Mirage** is a lightweight network obfuscation tool that generates randomized fake traffic to mask your real network activity.

It blends noise (HTTP, DNS, ICMP) with your legitimate traffic, making it harder for basic sniffers, ISP monitoring, or simple traffic analysis to profile you.

---

## Features

- Multiple modes: **HTTP**, **DNS**, **ICMP**, and **Mixed**
- Adjustable intensity (Low → Insane)
- Lightweight and fast (pure Python + raw sockets)
- Easy to run on Linux
- Educational & defensive research focused
- WiFi Poison attack capability for advanced network testing

---

## Installation

```bash
git clone https://github.com/neo4-svg/packet-mirage.git
cd packet-mirage
pip install scapy  # Required for WiFi Poison mode
```

---

## Usage

### Basic Traffic Obfuscation (packet_mirage.py)

Run the interactive tool with **sudo** (required for raw socket access):

```bash
sudo python3 packet_mirage.py
```

**Interactive Prompts:**

1. **Select Mode:**
   - `http` - Generate fake HTTP requests
   - `dns` - Generate fake DNS queries
   - `icmp` - Generate fake ICMP ping requests
   - `mixed` - Randomly mix all traffic types

2. **Select Intensity:**
   - `low` - 2 second delay between packets
   - `medium` - 1 second delay (default)
   - `high` - 0.5 second delay
   - `max` - 0.1 second delay
   - `insane` - 0.01 second delay (intense) ⚠️ **NOT RECOMMENDED** (see warning below)

3. **Duration:**
   - Enter time in seconds or leave blank for infinite runtime
   - Example: `60` for 60 seconds
   - Press Enter for infinite

**Example Session:**
```
=== Packet Mirage ===
Select mode [http/dns/icmp/mixed]: mixed
Select intensity [low/medium/high/max/insane]: high
Duration in seconds (blank = infinite): 120
Running Mirage: mode=mixed, intensity=high, duration=120s
```

---

### WiFi Poison Attack Mode (wifi_poison.py)

Advanced mode for WiFi deauthentication attacks. **Requires sudo and monitor mode interface.**

```bash
sudo python3 wifi_poison.py
```

**Interactive Setup:**

1. **Monitor Interface:**
   - Default: `wlan0mon`
   - Must be in monitor mode (tool auto-configures)

2. **Target Router BSSID:**
   - Enter the MAC address of target router
   - Example: `AA:BB:CC:DD:EE:FF`

3. **Target Client MAC:**
   - Enter specific client to disconnect
   - Leave blank for all clients (`ff:ff:ff:ff:ff:ff`)

4. **Power Level:**
   - `low` - Soft disconnect (40 pps)
   - `medium` - Good effect (100 pps) - default
   - `high` - Strong attack (200 pps)
   - `insane` - Very aggressive (350 pps) ⚠️ **NOT RECOMMENDED** (see warning below)

5. **Duration:**
   - Attack duration in seconds (default: 15)

**Example Session:**
```
=== Packet Mirage - WiFi Poison Mode ===

Enter monitor interface [wlan0mon]: wlan0mon
[+] Putting wlan0 into monitor mode...
[+] Monitor mode activated.

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
```

---

## Requirements

- **Linux** (raw sockets not available on macOS/Windows)
- **Python 3.8+**
- **sudo/root privileges** (for raw socket and monitor mode access)
- **Scapy** library (for WiFi Poison mode)

Install dependencies:
```bash
sudo pip install scapy
```

---

## Security & Legal Notice

⚠️ **CRITICAL WARNING - READ BEFORE USE**

### Insane Mode - NOT RECOMMENDED

The **"insane" intensity level** is provided for research purposes only and comes with serious risks:

**Risks of Insane Mode:**
- 🚨 **Router Damage:** Extremely high packet rates can overwhelm and crash home/small office routers
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

**Recommendation:**
Use `high` or `medium` intensity for normal operations. Only use `insane` if:
1. You have explicit written authorization
2. You're testing your own isolated network
3. You understand the legal consequences
4. You accept full responsibility

### General Legal Disclaimer

⚠️ **Disclaimer:** This tool is for **educational and authorized security testing only**. Unauthorized network attacks are illegal. Always have explicit written permission before testing on networks you don't own or manage.

**Use this tool at your own risk.** The authors assume no liability for misuse or legal consequences.

See [Disclaimer.md](Disclaimer.md) for full legal information.

---

## How It Works

- **packet_mirage.py** generates fake packets to create network noise, obfuscating real traffic patterns
- **wifi_poison.py** sends deauthentication frames to temporarily disconnect WiFi clients
- Combined, they provide traffic obfuscation and WiFi testing capabilities

---

## License

MIT License - See [LICENSE](LICENSE) for details

---

**Made by @neo4-svg** | Educational Security Research Tool
