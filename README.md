# Packet Mirage

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/neo4-svg/packet-mirage)](https://github.com/neo4-svg/packet-mirage/stargazers)
[![Code style: python](https://img.shields.io/badge/Code%20style-Python-blue)](https://www.python.org/)

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
```
