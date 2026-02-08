#Author SasinduShamika
#Time   12:26
#Date   2026-02-08

import socket
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

def usage():
    print("Usage:")
    print("  python port_scanner.py <target_ip> <start_port> <end_port>")
    print()
    print("Example:")
    print("  python port_scanner.py 127.0.0.1 1 1024")
    print("  python port_scanner.py 192.168.1.1 20 200")

if len(sys.argv) != 4:
    usage()
    sys.exit(1)

target = sys.argv[1]
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target:",target)

def scan_port(port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target,port))

    if result == 0:
        print(f"PORT {port} is OPEN")
    s.close()

with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(scan_port, range(start_port, end_port + 1))