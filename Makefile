all: client

client:
	pyinstaller client.py --onefile --noconsole --name "Trojark Client"

# server:
# 	pyinstaller -F server.py

clean:
	rm -rf *.spec build dist