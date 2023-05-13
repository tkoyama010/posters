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
resolution = 10000

# Preview how this circular arc intersects this mesh
arc = pv.CircularArcFromNormal(center, resolution, normal, polar, angle)

# mesh.plot_over_circular_arc_normal(
#     center, resolution, normal, polar, angle, fname="elevation.png"
# )

p = pv.Plotter(window_size=[1000, 500], off_screen=True)
p.add_mesh(mesh)
p.add_mesh(arc, color="white", line_width=10)
a = arc.points[0]
b = arc.points[-1]
p.add_point_labels(
    [a, b], ["A", "B"], font_size=48, point_color="red", text_color="red"
)
p.show_grid()
p.screenshot("kitchen.png")
