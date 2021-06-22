import socket
import chalk


def ip(clientsocket: socket.socket, address: tuple):
    clientsocket.send(bytes('curl "https://api.ipify.org"', "utf-8"))
