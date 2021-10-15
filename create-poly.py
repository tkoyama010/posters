"""
.. _ref_create_poly:

Create PolyData
~~~~~~~~~~~~~~~

Creating a PolyData (triangulated surface) object from NumPy arrays of the
vertices and faces.

"""

import numpy as np
import pyvista as pv

pv.set_plot_theme("document")

# mesh points
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
                     [0.5, 0.5, -1]])

# mesh faces
faces = np.hstack([[4, 0, 1, 2, 3],
                   [3, 0, 1, 4],
                   [3, 1, 2, 4]])

surf = pv.PolyData(vertices, faces)

# plot each face with a different color
surf.plot(cpos=[-1, 1, 0.5], screenshot="create-poly.png", show_edges=True)
