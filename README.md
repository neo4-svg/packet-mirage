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

---

## Installation

```bash
git clone https://github.com/neo4-svg/packet-mirage.git
cd packet-mirage
python3 packet_mirage.py
```

---

## Updates

### New: WiFi Positioning Integration (wifi-posit.py)

We've added **wifi-posit.py**, a companion tool for WiFi-based positioning and location spoofing. This module enhances Packet Mirage by:

- Detecting and spoofing WiFi access point signals
- Simulating location data across multiple WiFi networks
- Providing realistic WiFi positioning obfuscation
- Integrating seamlessly with Packet Mirage's traffic generation

This addition strengthens privacy by masking not just your network traffic, but also your physical location inference based on WiFi networks.

**Usage:**
```bash
python3 wifi_posit.py --mode spoof --intensity high
```

For more details, see [wifi_posit.py documentation](wifi_posit.py).

---

## Usage

[Add your usage documentation here]

---

## License

MIT License - See [LICENSE](LICENSE) for details
