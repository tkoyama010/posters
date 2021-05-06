import pyvista as pv
from pyvista import examples

pv.set_plot_theme("document")

mesh = examples.download_st_helens()

# Make two points at the bounds of the mesh and one at the center to
# construct a circular arc.
normal = [0, 0, 1]
polar = [4000.0, 0.0, 0.0]
center = mesh.center
angle = 90.0

mesh.plot_over_circular_arc_normal(
    center, 10000, normal, polar, angle, fname="velocity.png"
)

# Preview how this circular arc intersects this mesh
arc = pv.CircularArcFromNormal(center, 100, normal, polar, angle)

p = pv.Plotter()
p.add_mesh(mesh)
p.add_mesh(arc, color="white", line_width=10)
a = arc.points[0]
b = arc.points[-1]
p.add_point_labels(
    [a, b], ["A", "B"], font_size=48, point_color="red", text_color="red"
)
p.show_grid()
p.show(screenshot="kitchen.png")
