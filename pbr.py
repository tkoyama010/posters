"""
.. _pbr_example:

Physically Based Rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~

VTK 9 introduced Physically Based Rendering (PBR) and we have exposed
that functionality in PyVista. Read the `blog about PBR
<https://blog.kitware.com/vtk-pbr/>`_ for more details.

PBR is only supported for :class:`pyvista.PolyData` and can be
triggered via the ``pbr`` keyword argument of ``add_mesh``. Also use
the ``metallic`` and ``roughness`` arguments for further control.

Let's show off this functionality by rendering a high quality mesh of
a statue as though it were metallic.

"""

import pyvista as pv
from pyvista import examples

# Load the statue mesh
mesh = examples.download_nefertiti()
mesh.rotate_x(-90.)  # rotate to orient with the skybox

# Download skybox
cubemap = examples.download_sky_box_cube_map()


###############################################################################
# Let's render the mesh with a base color of "linen" to give it a metal looking
# finish.
p = pv.Plotter(window_size=[1000, 300], off_screen=True)
p.add_actor(cubemap.to_skybox())
p.set_environment_texture(cubemap)
p.add_mesh(mesh,color='linen',pbr=True,metallic=0.8,roughness=0.1,diffuse=1)

# Define a nice camera perspective
p.camera_position = [(-313.40, 66.09, 1000.61),
        (0.0, 0.0, 0.0),
        (0.018, 0.99, -0.06)]

p.screenshot("pbr1.png")


###############################################################################
# Show the variation of the metallic and roughness parameters.
#
# Plot with metallic increasing from left to right and roughness
# increasing from bottom to top.

colors = ['red', 'teal', 'black', 'orange', 'silver']
p = pv.Plotter(window_size=[1000, 300], off_screen=True)
p.set_environment_texture(cubemap)
for i in range(5):
    for j in range(6):
        sphere = pv.Sphere(radius=0.5, center=(0.0, 4 - i, j))
        p.add_mesh(sphere, color=colors[i],
                   pbr=True, metallic=i/4, roughness=j/5)
p.view_vector((-1, 0, 0), (0, 1, 0))
p.screenshot("pbr2.png")

