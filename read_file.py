import pyvista as pv

pv.set_plot_theme("document")

p = pv.Plotter()
mesh = pv.read("bunny.ply")
p.add_mesh(mesh, color="tan")
p.camera_position = "xy"

p.show(screenshot="read_file.png")
