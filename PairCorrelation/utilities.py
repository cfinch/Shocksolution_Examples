#!/usr/bin/env python
from numpy import *

def generate_hex_circle_packing(a, width):
    """Generate a domain of a given width filled with hexagonally packed
    circles.  The height will be determined so that the vertical 
    boundary condition is periodic.

    Arguments:
    a       particle radius
    width   domain width, in terms of particle radius

    Returns:
    x_list  list of x coordinates
    y_list  list of y coordinates
    x_size  width of domain (equal to argument width)
    y_size  height of domain
    """
    numParticles = 0

    x_list = []
    y_list = []
    y = a
    x = a
    rowNumber = 0
    # Create a row
    while y <= width*1.01:
        # Create circles in a row
        while x < width:
            x_list.append(x)
            x = x + 2*a
            y_list.append(y)
            numParticles = numParticles + 1
        y = y + a*sqrt(3.)
        rowNumber = rowNumber + 1
        if rowNumber%2 == 0:
            x = a
        else:
            x = 0
    x_size = width
    y_size = rowNumber*a*sqrt(3)

    return array(x_list), array(y_list), x_size, y_size

def plot_adsorbed_circles(adsorbed_x, adsorbed_y, radius, width, reference_indices=[]):
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle

    # Plot each run
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for p in range(len(adsorbed_x)):
        if len(np.where(reference_indices == p)[0]) > 0:
            ax.add_patch(Circle((adsorbed_x[p], adsorbed_y[p]), radius, 
                edgecolor='black', facecolor='black'))
        else:
            ax.add_patch(Circle((adsorbed_x[p], adsorbed_y[p]), radius,
                edgecolor='black', facecolor='white'))

    ax.set_aspect(1.0)
    plt.axhline(y=0, color='k')
    plt.axhline(y=width, color='k')
    plt.axvline(x=0, color='k')
    plt.axvline(x=width, color='k')
    plt.axis([-0.1*width, width*1.1, -0.1*width, width*1.1])
    plt.xlabel("non-dimensional x")
    plt.ylabel("non-dimensional y")

    return ax

