#Author SasinduShamika
#Time   12:26
#Date   2026-02-08

import socket
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

target = sys.argv[1]
print("Scanning target: ",target)

def scan_port(port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target,port))

    if result == 0:
        print(f"PORT {port} is OPEN")
    s.close()

with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(scan_port, range(1, 1025))