main.pdf: main.tex shrink.png airplane.png frustum_of_camera.png
	pdflatex $<
shrink.png: shrunk_mesh.py
	python shrunk_mesh.py
airplane.png: airplane.py
	python airplane.py
frustum_of_camera.png: frustum_of_camera.py
	python frustum_of_camera.py
