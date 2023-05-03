import pyvista as pv

pv.set_plot_theme("document")

bunny = pv.read("bunny.ply")
cow = pv.read("cow.obj")
gears = pv.read("gears.stl")
human = pv.read("Human.vtp")

p = pv.Plotter(shape=(2, 2), window_size=[1000, 500], off_screen=True)
p.subplot(0, 0)
p.add_text("Bunny")
p.add_mesh(bunny, color="tan")
p.subplot(0, 1)
p.add_text("Cow")
p.add_mesh(cow, color="tan")
p.subplot(1, 0)
p.add_text("Gears")
p.add_mesh(gears, color="tan")
p.subplot(1, 1)
p.add_text("Human")
p.add_mesh(human, color="tan")

p.screenshot("read_file.png")

# pv.save_meshio("bunny.vtk", bunny)
# pv.save_meshio("cow.stl", cow)
# pv.save_meshio("gears.obj", gears)
# pv.save_meshio("Human.ply", human)
