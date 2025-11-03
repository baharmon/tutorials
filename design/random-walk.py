#!/usr/bin/env python

"""
Random walk
"""

__author__ = "Brendan Harmon"
__copyright__ = "Copyright 2025, Brendan Harmon"
__email__ = "brendan.harmon@gmail.com"
__license__ = "MIT"
__version__ = "1.0.0"

# Import libraries
import numpy as np
import seaborn as sns

# Set theme
sns.set_theme(
    context='paper', 
    style="darkgrid"
    )

# Set variables
i = 1000 # Iterations
mu = 0.0 # Mean
sigma = 0.25 # Standard deviation

# Instantiate random number generator
rng = np.random.default_rng()

# Generate random steps
u = rng.normal(mu, sigma, i)
v = rng.normal(mu, sigma, i)

# Solve position
x = np.cumsum(u)
y = np.cumsum(v)

# Plot function
plot = sns.scatterplot(
    x=x,
    y=y,
    size=np.arange(i),
    sizes=(10, 100),
    hue=np.arange(i),
    palette='flare',
    legend=False
    )
