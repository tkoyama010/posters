"""
.. _silhouette_example:

Silhouette Highlight
~~~~~~~~~~~~~~~~~~~~

Extract a subset of the edges of a polygonal mesh to generate an outline
(silhouette) of a mesh.
"""

import pyvista
from pyvista import examples
pyvista.set_plot_theme("document")

###############################################################################
# Prepare a triangulated ``PolyData``
bunny = examples.download_bunny()

###############################################################################
# Now we can display the silhouette of the mesh and compare the result:
plotter = pyvista.Plotter(shape=(1, 2), window_size=[1000, 300], off_screen=True)
plotter.subplot(0, 0)
silhouette = dict(color='red', line_width=8.0, decimate=None)
plotter.add_mesh(bunny, color='tan', silhouette=silhouette)
plotter.add_text("Silhouette")
plotter.view_xy()
plotter.subplot(0, 1)
plotter.add_mesh(bunny, color='tan')
plotter.add_text("No silhouette")
plotter.view_xy()
p.screenshot("silhouette1.png")

