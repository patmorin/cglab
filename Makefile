all : logo.png
	./generate.py
	cp logo.png ../public_html
	cp logo.png ../public_html/seminar/

logo.png : logo.ipe
	iperender -png logo.ipe logo.png

