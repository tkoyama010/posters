"""
.. _clip_with_plane_box_example:

Clipping with Planes & Boxes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clip/cut any dataset using using planes or boxes.
"""
# sphinx_gallery_thumbnail_number = 2
import pyvista as pv
from pyvista import examples
pv.set_plot_theme("document")

###############################################################################
# Clip with Plane
# +++++++++++++++
#
# Clip any dataset by a user defined plane using the
# :func:`pyvista.DataSetFilters.clip` filter
dataset = examples.download_bunny_coarse()
clipped = dataset.clip('y', invert=False)

p = pv.Plotter(window_size=[1000, 300], off_screen=True)
p.add_mesh(dataset, style='wireframe', color='blue', label='Input')
p.add_mesh(clipped, label='Clipped')
p.add_legend()
p.camera_position = [(0.24, 0.32, 0.7),
                     (0.02, 0.03, -0.02),
                     (-0.12, 0.93, -0.34)]
p.screenshot("clipping1.png")


###############################################################################
# Clip with Bounds
# ++++++++++++++++
#
# Clip any dataset by a set of XYZ bounds using the
# :func:`pyvista.DataSetFilters.clip_box` filter.
dataset = examples.download_office()

bounds = [2,4.5, 2,4.5, 1,3]
clipped = dataset.clip_box(bounds)

p = pv.Plotter(window_size=[1000, 300], off_screen=True)
p.add_mesh(dataset, style='wireframe', color='blue', label='Input')
p.add_mesh(clipped, label='Clipped')
p.add_legend()
p.screenshot("clipping2.png")

