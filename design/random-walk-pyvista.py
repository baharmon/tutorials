#!/usr/bin/env python

"""
Render 3D random walks with PyVista
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2025, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# Import libraries
import numpy as np
import pyvista as pv

# Set variables
i = 1000000 # Iterations
mu = 0.0 # Mean
sigma = 0.25 # Standard deviation
scale = 2 # Scale factor

# Instantiate random number generator
rng = np.random.default_rng()

# Generate random steps
u = rng.normal(mu, sigma * scale, i)
v = rng.normal(mu, sigma * scale, i)
w = rng.normal(mu, sigma / scale, i)

# Solve position
x = np.cumsum(u)
y = np.cumsum(v)
z = np.cumsum(w)

# Stack coordinates
xyz = np.column_stack((x, y, z))

# Set plot theme
pv.set_plot_theme("document")

# Plot
pv.plot(
    xyz,
    scalars=z,
    render_points_as_spheres=True,
    point_size=20,
    show_scalar_bar=False,
    eye_dome_lighting=True,
    ambient=0.6,
    diffuse=0.8,
    window_size=(2000, 2000),
    off_screen=True,
    screenshot='random-walk-3d.png'
)