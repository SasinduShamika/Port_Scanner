#Author SasinduShamika
#Time   12:26
#Date   2026-02-08

import socket
import sys

target = sys.argv[1]
print("Scanning target: ",target)

for port in range(1,1025):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target,port))

    if result == 0:
        print(f"PORT {port} is OPEN")
    s.close()