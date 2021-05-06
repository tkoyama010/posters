import pyvista as pv
import numpy as np
from pyvista import examples

pv.set_plot_theme("document")

camera = pv.Camera()
near_range = 0.3
far_range = 0.8
camera.clipping_range = (near_range, far_range)
unit_vector = np.array(camera.direction) / np.linalg.norm(
    np.array([camera.focal_point]) - np.array([camera.position])
)

bunny = examples.download_bunny()
xyz = camera.position + unit_vector * 0.6 - np.mean(bunny.points, axis=0)
bunny.translate(xyz)

p = pv.Plotter(window_size=[1024, 384])
p.add_mesh(bunny)
p.camera = camera
p.show(screenshot="camera_view.png")
