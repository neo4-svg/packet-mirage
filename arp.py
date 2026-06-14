#!/usr/bin/env python3

import os
import sys
import json
from scapy.all import sniff, ARP, get_if_list
from datetime import datetime
from collections import defaultdict, Counter
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

BANNER = """
[bold cyan]
==============================================
        ARP Movement Tracker
        github: neo4-svg
        X: germanhack40404
==============================================
[/bold cyan]
"""

arp_graph = defaultdict(set)
packet_count = 0
unique_ips = set()
arp_frequency = Counter()

def legal_check():
    console.print("[yellow]Are you running this tool in a legal environment (your own network)?[/yellow]")
    ans = input("[y/n] > ").strip().lower()
    if ans != "y":
        console.print("[red]Exiting...[/red]")
        sys.exit(0)

def check_sudo():
    if os.geteuid() != 0:
        console.print("[bold red][!] This tool requires sudo privileges.[/bold red]")
        sys.exit(1)

def auto_detect_iface():
    """Pick the first non-loopback, non-virtual interface."""
    interfaces = get_if_list()
    for iface in interfaces:
        if iface != "lo" and not iface.startswith(("vir", "docker", "vbox")):
            return iface
    return None

def log_to_file(text):
    with open("arp_log.txt", "a") as f:
        f.write(text + "\n")

def export_json():
    data = {
        "arp_graph": {src: list(tgts) for src, tgts in arp_graph.items()},
        "unique_ips": list(unique_ips),
        "packet_count": packet_count,
        "arp_frequency": dict(arp_frequency)
    }
    with open("arp_export.json", "w") as f:
        json.dump(data, f, indent=4)
    console.print("[green]Exported ARP data to arp_export.json[/green]")

def print_graph():
    table = Table(title="ARP Movement Map", box=box.ROUNDED)
    table.add_column("Source IP", style="cyan")
    table.add_column("Targets", style="magenta")
    for src, targets in arp_graph.items():
        table.add_row(src, ", ".join(targets))
    console.print(table)

def print_stats():
    table = Table(title="ARP Stats", box=box.ROUNDED)
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("Total ARP Packets", str(packet_count))
    table.add_row("Unique IPs Seen", str(len(unique_ips)))
    if arp_frequency:
        table.add_row("Top Talker", arp_frequency.most_common(1)[0][0])
    console.print(table)

def print_heatmap():
    table = Table(title="ARP Frequency Heatmap", box=box.ROUNDED)
    table.add_column("IP", style="cyan")
    table.add_column("Count", style="yellow")
    for ip, count in arp_frequency.most_common():
        bar = "█" * min(count, 40)
        table.add_row(ip, bar)
    console.print(table)

def arp_callback(pkt):
    global packet_count
    if ARP in pkt:
        packet_count += 1
        src_ip = pkt[ARP].psrc
        dst_ip = pkt[ARP].pdst
        op = "REQUEST" if pkt[ARP].op == 1 else "REPLY"
        unique_ips.add(src_ip)
        unique_ips.add(dst_ip)
        arp_graph[src_ip].add(dst_ip)
        arp_frequency[src_ip] += 1
        log_entry = f"[{datetime.now()}] {op} | {src_ip} -> {dst_ip}"
        log_to_file(log_entry)
        console.print(f"[green]{log_entry}[/green]")
        console.print(f"    [yellow]{src_ip} has talked to:[/yellow] {', '.join(arp_graph[src_ip])}")

def start_sniffer(interface):
    console.print(f"[bold green][+] Sniffing ARP packets on {interface}...[/bold green]")
    sniff(filter="arp", iface=interface, prn=arp_callback, store=False)

def main():
    print(BANNER)
    legal_check()
    check_sudo()

    iface = auto_detect_iface()
    if iface:
        console.print(f"[bold green][+] Auto-detected interface:[/bold green] {iface}")
    else:
        console.print("[bold red][!] Could not auto-detect a valid interface.[/bold red]")
        sys.exit(1)

    start_sniffer(iface)

if __name__ == "__main__":
    main()
