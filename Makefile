main.pdf: main.tex shrink.png hello_world.png frustum_of_camera.png camera_view.png kitchen.png extrude_rotate.png
	pdflatex $<
shrink.png: shrunk_mesh.py
	python shrunk_mesh.py
hello_world.png: hello_world.py
	python hello_world.py
frustum_of_camera.png: frustum_of_camera.py
	python frustum_of_camera.py
camera_view.png: camera_view.py
	python camera_view.py
kitchen.png: kitchen.py
	python kitchen.py
extrude_rotate.png: extrude_rotate.py
	python extrude_rotate.py
