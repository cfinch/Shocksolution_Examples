#!/usr/bin/env python
from numpy import *
from scipy.linalg import solve
import tridiag

upper = array([10.0, 10.0, 10.0, 10.0, 0.0])  
middle = array([-40.0, -30.0, -30.0, -30.0, 40.0])
lower = upper.copy()
b = array([-10.0, -10.0, -10.0, -10.0, -30.0])
m = len(middle)
n = m

(solution, exit_code) = tridiag.tri.tridiag(lower, middle, upper, b, n)

print "Fortran solution:"
print solution
print exit_code

# Create matrix from diagonals
coeffs = zeros([m,n])

coeffs[0,0] = middle[0]
coeffs[0,1] = upper[0]

for i in range(1,m-1):
    coeffs[i,i-1] = lower[i]
    coeffs[i,i] = middle[i]
    coeffs[i,i+1] = upper[i]

coeffs[m-1,m-2] = lower[m-1]
coeffs[m-1,m-1] = middle[m-1]

print "Python input:"
print coeffs
print b
Python_solution = solve(coeffs, b)

print "Python solution:"
print Python_solution


