import pyvista as pv

pv.set_plot_theme("document")

cyl = pv.Cylinder()
arrow = pv.Arrow()
sphere = pv.Sphere()

p = pv.Plotter(shape=(1, 3), window_size=[1000, 300], off_screen=True)
p.subplot(0, 0)
p.add_text("Cylinder")
p.add_mesh(cyl, color="tan", show_edges=True)
p.subplot(0, 1)
p.add_text("Arrow")
p.add_mesh(arrow, color="tan", show_edges=True)
p.subplot(0, 2)
p.add_text("Sphere")
p.add_mesh(sphere, color="tan", show_edges=True)

p.screenshot("hello_world.png")
