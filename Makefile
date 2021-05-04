main.pdf: main.tex shrink.png airplane.png frustum_of_camera.png camera_view.png
	pdflatex $<
shrink.png: shrunk_mesh.py
	python shrunk_mesh.py
airplane.png: airplane.py
	python airplane.py
frustum_of_camera.png: frustum_of_camera.py
	python frustum_of_camera.py
camera_view.png: camera_view.py
	python camera_view.py
