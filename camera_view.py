import pyvista as pv
import numpy as np
from pyvista import examples

pv.set_plot_theme("document")

camera = pv.Camera()
near_range = 0.3
far_range = 0.8
camera.clipping_range = (near_range, far_range)

p = pv.Plotter(window_size=[1000, 300])
p.camera = camera

unit_vector = np.array(camera.direction) / np.linalg.norm(
    np.array([camera.focal_point]) - np.array([camera.position])
)
bunny = examples.download_bunny()
xyz = camera.position + unit_vector * 0.6 - np.mean(bunny.points, axis=0)
bunny.translate(xyz)
p.add_mesh(bunny)
p.show(screenshot="camera_view.png")

p = pv.Plotter(shape=(3, 1), window_size=[1000, 900])
p.subplot(0, 0)
p.add_text("Roll 10 degree")
p.add_mesh(bunny)
p.camera = camera.copy()
p.camera.roll += 10
p.subplot(1, 0)
p.add_text("Azimuth 45 degree")
p.add_mesh(bunny)
p.camera = camera.copy()
p.camera.azimuth = 45
p.subplot(2, 0)
p.add_text("Elevation 10 degree")
p.add_mesh(bunny)
p.camera = camera.copy()
p.camera.elevation = 10
p.show(screenshot="camera_rotation.png")
