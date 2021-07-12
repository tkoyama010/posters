=======
PyVista
=======
Visualize 3D scientific data in a Pythonic way like matplotlib

Tetsuo Koyama ( `@tkoyama010 <https://twitter.com/tkoyama010>`_ )

Overview
========

.. Do you want to visualize 3D scientific data in a Pythonic way like matplotlib?
.. If you want, this LT is for you.
.. This poster is the introduction of PyVista.
.. It is
.. 1. "VTK for humans"\: a high-level API to the Visualization Toolkit (VTK)
.. 2. 3D plotting made simple and built for large/complex data geometries
.. 3. mesh data structures and filtering methods for spatial datasets

Who am I ?
==========

Hello World!
============

.. In this code, we demonstrate the "Hello World!" of PyVista.
.. Basic step of PyVista script is the following.
.. First, import PyVista.
.. Then generate mesh and add it to
.. Plotter object using add_mesh method.
.. And finally, we can check the render view figure of PyVista using show() method.

Load and plot from a files
==========================

.. Loading a mesh is trivial - if your data is in one of the many supported file formats,
.. simply use pyvista.read()
.. to load your spatially referenced dataset into a PyVista mesh object.
.. Also note that we can export any PyVista mesh to any file format supported by meshio.
.. To save a PyVista mesh using meshio, use pyvista.save_meshio():

Extracting and Contouring
=========================

.. Attributes are data values that live on either the nodes or cells of a mesh.
.. In PyVista, we work with both point data and cell data and allow easy access to data dictionaries to hold arrays for attributes that live either on all nodes or on all cells of a mesh.
.. Meshes can have a scalar field extracted
.. using warp_by_scalar() method.
.. Also can have a vector filed extracted
.. using warp_by_vector() method.
.. add_mesh() method can use a Matplotlib, Colorcet, cmocean, or custom colormap when plotting scalar values

Camera class
============

.. Camera class is a virtual camera for 3D rendering.
.. It provides methods to position and orient the view point and focal point.
.. Convenience methods for moving about the focal point also are provided.
.. More complex methods allow the manipulation of the computer graphics model including view up vector, clipping planes, and camera perspective.
.. Code Listing CameraFrustumCode create a camera and frustum.
.. Then create a scene of inside frustum adding Camera object to Plotter object.

Controlling Camera Rotation
===========================

.. In addition to directly controlling the camera position by setting it via the pyvista.
.. Camera.position
.. property, you can also directly control the
.. pyvista.Camera.roll,
.. pyvista.Camera.elevation, and
.. pyvista.Camera.azimuth
.. of the camera.

Rotations
=========

.. Rotations of a mesh about its axes.
.. In this model, the x axis is from the left to right; the y axis is from bottom to top; and the z axis emerges from the image.
.. The camera location is the same in all four images.

Define camera and axes
----------------------

.. Define camera and axes. Setting axes origin to (3.0, 3.0, 3.0).

Original Mesh
-------------

.. Plot original mesh. Add axes actor to Plotter.

Rotation about the x axis
-------------------------

.. Plot the mesh rotated about the x axis every 60 degrees.
.. Add the axes actor to the Plotter and set the axes origin to the point of rotation.

Rotation about the y axis
-------------------------

.. Plot the mesh rotated about the y axis every 60 degrees.
.. Add the axes actor to the Plotter and set the axes origin to the point of rotation.

Rotation about the z axis
-------------------------

.. Plot the mesh rotated about the z axis every 60 degrees.
.. Add axes actor to the Plotter and set the axes origin to the point of rotation.

Rotation about a custom vector
------------------------------

.. Plot the mesh rotated about a custom vector every 60 degrees.
.. Add the axes actor to the Plotter and set axes origin to the point of rotation.

Plot data over circular arc
===========================

.. It can be plotting the values of a dataset over a circular arc through that dataset using
.. plot_over_circular_arc_normal.

Acknowlegment
=============
.. I would like to thank PyVista developer team for developing useful library.

Conclusion
==========

Contact Information
===================
