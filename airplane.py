import pyvista as pv
from pyvista import examples

pv.set_plot_theme("document")
mesh = examples.load_airplane()
mesh.plot(screenshot="airplane.png")
