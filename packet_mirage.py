#!/usr/bin/env python3
"""
Packet Mirage - Interactive Network Noise Generator
Blasts fake traffic to mask real activity.
Run with sudo for raw sockets.
"""

import socket
import random
import time
import os

def fake_http(host="example.com", port=80):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        req = f"GET /{random.randint(1,999)} HTTP/1.1\r\nHost: {host}\r\n\r\n"
        s.send(req.encode())
    except Exception:
        pass
    finally:
        s.close()

def fake_dns(host="8.8.8.8", port=53):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        packet = os.urandom(32)
        s.sendto(packet, (host, port))
    except Exception:
        pass
    finally:
        s.close()

def fake_icmp(host="8.8.8.8"):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    try:
        packet = os.urandom(64)
        s.sendto(packet, (host, 0))
    except Exception:
        pass
    finally:
        s.close()

def run(mode, intensity, duration):
    delay = {"low":2.0,"medium":1.0,"high":0.5,"max":0.1,"insane":0.01}[intensity]
    start = time.time()
    while True:
        if mode == "http":
            fake_http()
        elif mode == "dns":
            fake_dns()
        elif mode == "icmp":
            fake_icmp()
        else:  # mixed
            random.choice([fake_http, fake_dns, fake_icmp])()
        time.sleep(delay)
        if duration and (time.time() - start > duration):
            break

if __name__ == "__main__":
    print("=== Packet Mirage ===")
    mode = input("Select mode [http/dns/icmp/mixed]: ").strip().lower()
    if mode not in ["http","dns","icmp","mixed"]:
        mode = "mixed"

    intensity = input("Select intensity [low/medium/high/max/insane]: ").strip().lower()
    if intensity not in ["low","medium","high","max","insane"]:
        intensity = "medium"

    dur = input("Duration in seconds (blank = infinite): ").strip()
    duration = int(dur) if dur else None

    print(f"Running Mirage: mode={mode}, intensity={intensity}, duration={'infinite' if not duration else duration}s")
    run(mode, intensity, duration)
