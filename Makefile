main.pdf: main.tex shrink.png airplane.png
	pdflatex $<
shrink.png: shrunk_mesh.py
	python shrunk_mesh.py
airplane.png: airplane.py
	python airplane.py
