"""
.. _background_image_example:

Background Image
~~~~~~~~~~~~~~~~

Add a background image with :func:`pyvista.Plotter.add_background_image`.

"""
import pyvista as pv
from pyvista import examples


###############################################################################
# Plot an airplane with the map of the earth in the background
earth_alt = examples.download_topo_global()

pl = pv.Plotter(window_size=[1000, 300], off_screen=True)
actor = pl.add_mesh(examples.load_airplane(), smooth_shading=True)
pl.add_background_image(examples.mapfile)
pl.screenshot("background_image1.png")

