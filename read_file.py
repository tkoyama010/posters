import pyvista as pv

pv.set_plot_theme("document")

p = pv.Plotter(window_size=[1000, 300])
mesh = pv.read("bunny.ply")
p.add_mesh(mesh, color="tan")

p.show(screenshot="read_file.png")
