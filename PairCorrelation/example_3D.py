import numpy as np
import matplotlib.pyplot as plt
from utilities import *
from paircorrelation import pairCorrelationFunction_3D

# Particle setup
domain_size = 20.0
num_particles = 10000

# Calculation setup
dr = 0.1

### Random arrangement of particles ###
particle_radius = 0.1
rMax = domain_size / 4
x = np.random.uniform(low=0, high=domain_size, size=num_particles)
y = np.random.uniform(low=0, high=domain_size, size=num_particles)
z = np.random.uniform(low=0, high=domain_size, size=num_particles)

# Compute pair correlation
g_r, r, reference_indices = pairCorrelationFunction_3D(x, y, z, domain_size, rMax, dr)

# Visualize
plt.figure()
plt.plot(r, g_r, color='black')
plt.xlabel('r')
plt.ylabel('g(r)')
plt.xlim( (0, rMax) )
plt.ylim( (0, 1.05 * g_r.max()) )
plt.show()
