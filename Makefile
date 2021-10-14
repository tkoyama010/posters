all:
	make slides.pdf

slides.pdf: slides.tex shrink.png hello_world.png frustum_of_camera.png camera_view.png kitchen.png extrude_rotate.png contour.png read_file.png warped_vector.png elevation.png rotate_mesh.png rotate_x.png rotate_y.png rotate_z.png rotate_custom.png tube.png
	pdflatex $<
main.pdf: main.tex shrink.png hello_world.png frustum_of_camera.png camera_view.png kitchen.png extrude_rotate.png contour.png read_file.png warped_vector.png elevation.png
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
warped_vector.png: contour.py
	python $<
elevation.png: kitchen.py
	python $<
rotate_mesh.png: rotate.py
	python $<
rotate_x.png: rotate.py
	python $<
rotate_y.png: rotate.py
	python $<
rotate_z.png: rotate.py
	python $<
rotate_custom.png: rotate.py
	python $<
tube.png: tube.py
	python $<
