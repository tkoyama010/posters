main.pdf: main.tex shrink.png
	pdflatex $<
shrink.png: shrunk_mesh.py
	python shrunk_mesh.py
