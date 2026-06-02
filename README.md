# Packet Mirage

**Packet Mirage** is a lightweight network obfuscation tool that generates randomized traffic to major IP ranges (Google, Microsoft, Amazon).  
By blending fake signals with real connections, it disrupts sniffers, confuses outdated monitoring setups, and masks traffic patterns — acting like a partial VPN for added privacy.

## Features
- Randomized ICMP, DNS, HTTP, and ARP packets
- Targets trusted cloud IP ranges for camouflage
- Obfuscates traffic fingerprints and timing analysis
- Lightweight CLI design, easy to run on Linux

## Use Cases
- Hide browsing patterns from basic ISP monitoring
- Confuse attackers using outdated sniffers
- Add a deception layer to network defense

## Installation
Clone the repo and run:
```bash
git clone https://github.com/neo4-svg/packet-mirage.git
cd packet-mirage
python3 packet_mirage.py
