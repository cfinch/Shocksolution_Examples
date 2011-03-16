#!/usr/bin/env python
from numpy import *
from matplotlib import pyplot as plt
import lu_solver

# Setup
num_layers = 4

D = ones(num_layers)
delta_h = ones(num_layers)

D[1] = 0.5
D[3] = 2.0
D[2] = 0.1

delta_h[0] = 0.25
delta_h[1] = 1.0
delta_h[2] = 1.75
delta_h[3] = 0.25

C_0 = 0
C_N = 1.0

# Set up matrices and arrays
A = array([[8, 2, 3, 12], [2, 4, 7, 0.25], [3, 7, 3, 5], [12, 0.25, 5, 2]], 
        dtype='double', order='f')
print(A)
b = array([25, 13.25, 18, 19.25], dtype=float64, order='f')
print(b)

indx, d, code = lu_solver.lu.ludcmp(A, num_layers)

print("LU Decomposition:")
print A
print indx
print d
print code

if code == 0:
    lu_solver.lu.lubksb(A, num_layers, indx, b)

print("Solution:")
print b
