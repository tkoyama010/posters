main.pdf: main.tex shrink.png hello_world.png frustum_of_camera.png camera_view.png kitchen.png extrude_rotate.png contour.png read_file.png
	pdflatex $<
shrink.png: shrunk_mesh.py
	python $<
hello_world.png: hello_world.py
	python $<
frustum_of_camera.png: frustum_of_camera.py
	python $<
camera_view.png: camera_view.py
	python $<
kitchen.png: kitchen.py
	python $<
extrude_rotate.png: extrude_rotate.py
	python $<
contour.png: contour.py
	python $<
read_file.png: read_file.py
	python $<
