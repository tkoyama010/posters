from pyvista import examples
import pyvista as pv
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

pv.set_plot_theme("document")
mesh = examples.download_st_helens()
warped_mesh = mesh.warp_by_scalar("Elevation")
# Add scalar array with range (0, 100) that correlates with elevation
mesh["values"] = pv.plotting.normalize(mesh["Elevation"]) * 100
warped_mesh["values"] = pv.plotting.normalize(mesh["Elevation"]) * 100

p = pv.Plotter(shape=(2, 2))
p.subplot(0, 0)
p.add_text("Before Warp")
p.add_mesh(
    mesh, scalars="Elevation", cmap="hot", stitle="Matplotlib Hot"
)

p.subplot(0, 1)
p.add_text("After Warp")
p.add_mesh(
    warped_mesh, scalars="Elevation", cmap="hot", stitle="Matplotlib Hot"
)

p.subplot(1, 0)
p.add_text("Before Warp")
p.add_mesh(
    mesh, scalars="Elevation", cmap="cool", stitle="Matplotlib Cool"
)

p.subplot(1, 1)
p.add_text("After Warp")
p.add_mesh(
    warped_mesh, scalars="Elevation", cmap="cool", stitle="Matplotlib Cool"
)

p.show(screenshot="contour.png")

p = pv.Plotter()

sphere = examples.load_sphere_vectors()
warped = sphere.warp_by_vector()

p = pv.Plotter(shape=(1, 2), window_size=[1000, 300])
p.subplot(0, 0)
p.add_text("Before warp")
p.add_mesh(sphere, scalars=None)
p.subplot(0, 1)
p.add_text("After warp")
p.add_mesh(warped, scalars=None)
p.show(screenshot="warped_vector.png")
