# Python Nmap Port Scanner

A Python-based Nmap scanner that allows users to scan a specified range of ports on a target machine and provides detailed results, including open ports and their states.

## Features
- Scans a range of ports on a target machine (via IP address).
- Provides detailed output for each host, including hostname, state, protocol, and open ports.
- Displays results in a human-readable format.

## Requirements
- Python 3.x
- `python-nmap` module (install via `pip install python-nmap`)
- Nmap installed on your machine (use the appropriate method for your OS)

## Usage
To run the script, provide the target IP address and the range of ports you want to scan:

```bash
python nmap_scanner.py <target_ip> <start_port> <end_port>
