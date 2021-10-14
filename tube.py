import pyvista as pv
import numpy as np

pv.set_plot_theme("document")

p = pv.Plotter(shape=(1, 2), window_size=[1000, 300])

p.subplot(0, 0)
p.add_text("Line")
line = pv.Line((0, 0, 0), (10, 0, 0))
p.add_mesh(line, color="k", line_width=5)

p.subplot(0, 1)
p.add_text("Tube")
tube = pv.Tube((0, 0, 0), (10, 0, 0))
p.add_mesh(tube)

p.show(cpos="xz", screenshot="tube.png")
