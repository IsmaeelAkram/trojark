all: client server

client:
	pyinstaller -F -w client.py

server:
	pyinstaller -F server.py

clean:
	rm -rf *.spec build dist