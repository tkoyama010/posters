from pyvista import examples
import pyvista as pv
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

pv.set_plot_theme("document")
mesh = examples.download_st_helens().warp_by_scalar()
# Add scalar array with range (0, 100) that correlates with elevation
mesh['values'] = pv.plotting.normalize(mesh['Elevation']) * 100

p = pv.Plotter(shape=(1, 2))
p.subplot(0, 0)
p.add_mesh(mesh, scalars='Elevation', cmap="hot",
           lighting=True, stitle="Matplotlib Hot")

p.subplot(0, 1)
p.add_mesh(mesh, scalars='Elevation', cmap="cool",
           lighting=True, stitle="Matplotlib Cool")

p.show(screenshot="contour.png")
