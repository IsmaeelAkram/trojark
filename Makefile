all: client

client:
	pyinstaller client.py --onefile --noconsole --name "Trojark Client" --icon icon.ico

# server:
# 	pyinstaller -F server.py

clean:
	rm -rf *.spec build dist