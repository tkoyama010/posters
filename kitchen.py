import pyvista as pv
from pyvista import examples

pv.set_plot_theme("document")

mesh = examples.download_kitchen()

# Make two points to construct the line between
a = [mesh.bounds[0], mesh.bounds[2], mesh.bounds[4]]
b = [mesh.bounds[1], mesh.bounds[3], mesh.bounds[5]]

# Preview how this line intersects this mesh
line = pv.Line(a, b)

p = pv.Plotter()
p.add_mesh(mesh, style="wireframe", color="w")
p.add_mesh(line, color="b")
p.show(screenshot="kitchen.png")

mesh.plot_over_line(a, b, resolution=100, fname="velocity.png")
