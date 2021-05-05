import pyvista as pv
from pyvista import examples

pv.set_plot_theme("document")

mesh = examples.load_uniform()
mesh["height"] = mesh.points[:, 2]

# Make two points at the bounds of the mesh and one at the center to
# construct a circular arc.
normal = [0, 1, 0]
polar = [mesh.bounds[0], mesh.bounds[2], mesh.bounds[5]]
center = [mesh.bounds[0], mesh.bounds[2], mesh.bounds[4]]
angle = 90.0

mesh.plot_over_circular_arc_normal(
    center, 100, normal, polar, angle, "height", fname="velocity.png"
)

# Preview how this circular arc intersects this mesh
arc = pv.CircularArcFromNormal(center, 100, normal, polar, angle)

p = pv.Plotter()
p.add_mesh(mesh, style="wireframe", color="w")
p.add_mesh(arc, color="b")
a = arc.points[0]
b = arc.points[-1]
p.add_point_labels(
    [a, b], ["A", "B"], font_size=48, point_color="red", text_color="red"
)
p.show(screenshot="kitchen.png")
