"""
Types of Shading
~~~~~~~~~~~~~~~~

Comparison of default, flat shading vs. smooth shading.
"""
# sphinx_gallery_thumbnail_number = 2
import pyvista

pyvista.set_plot_theme("document")
###############################################################################
# PyVista supports two types of shading, flat and smooth shading that uses
# VTK's Phong shading algorithm.
#
# This is a plot with the default flat shading:
sphere = pyvista.Sphere()
p = pyvista.Plotter(shape=(1, 2), window_size=[1000, 300])
p.subplot(0, 0)
p.add_text("Flat Shading")
p.add_mesh(sphere, color="w", smooth_shading=False)
p.subplot(0, 1)
p.add_text("Smooth Shading")
p.add_mesh(sphere, color="w", smooth_shading=True)
p.show(screenshot="shading.png")
