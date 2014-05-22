all:
	./generate.py

logo.png : logo.ipe
	iperender -png -resolution 200 logo.ipe logo.png

