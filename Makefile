all: client

client:
	pyinstaller client.py --onefile --noconsole --name "Trojark Client"

clean:
	rm -rf *.spec build dist