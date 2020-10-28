all: install
install:
	if [ ! -d "/usr/share/ToHex" ]; then mkdir "/usr/share/ToHex"; fi;
	cp ./src/main.py /usr/share/ToHex
	chmod +x ./ToHex
	cp ./ToHex /usr/bin/

remove:
	rm /usr/bin/ToHex
