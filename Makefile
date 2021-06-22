all: client server

client:
	pyinstaller client.py

server:
	pyinstaller server.py
