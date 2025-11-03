#!/usr/bin/env python

"""
Render 3D random walks with Open3D
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2025, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# Import libraries
import numpy as np
import open3d as o3d
import matplotlib.cm as cm
import matplotlib.colors as colors

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

# Read point cloud
cloud = o3d.geometry.PointCloud()
cloud.points = o3d.utility.Vector3dVector(xyz)

# Assign color gradient
colormap = cm.get_cmap("viridis")
normalization = colors.Normalize(vmin=z.min(), vmax=z.max())
normalization = normalization(z)
gradient = colormap(normalization)
gradient = gradient[:, :3]
cloud.colors = o3d.utility.Vector3dVector(gradient)

# Render points
o3d.visualization.draw(
    [cloud],
    point_size=4,
    width=2000,
    height=2000,
    show_skybox=False,
    raw_mode=True
    )
