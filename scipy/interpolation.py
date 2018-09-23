from scipy.interpolate import interp1d, UnivariateSpline
from scipy.stats import norm
from numpy import arange
from numpy.random import uniform
import matplotlib.pyplot as plt
from time import time

deltax = 0.1
xmin = -5.0
xmax = 5.0

# Set up samples
x_samples = arange(xmin, xmax, deltax)
pdf_samples = norm.pdf(x_samples)
fig = plt.plot(x_samples, pdf_samples, 'ro', label='Sampled')

# Interpolate on a finer grid
pdf_interp = interp1d(x_samples, pdf_samples, kind='linear')
x_interp = arange(xmin+deltax, xmax-deltax, 0.001)
plt.plot(x_interp, pdf_interp(x_interp), 'b-', label='Interpolated')

# Do the same thing with UnivariateSpline
u = UnivariateSpline(x_samples, pdf_samples, k=1, s=0.0)
plt.plot(x_interp, u(x_interp), 'k-', label='Spline')

plt.xlabel('x')
plt.ylabel('pdf')
plt.legend()
plt.show()

# Time tests
start_time = time()
for i in range(100000):
    pdf_interp(uniform(xmin+deltax, xmax-deltax))
print("interp1d run time: {}".format(time() - start_time))

start_time = time()
for i in range(100000):
    u(uniform(xmin+deltax, xmax-deltax))
print("UnivariateSpline run time: {}".format(time() - start_time))

x_fine = arange(xmin + deltax, xmax - deltax - 0.001, 1e-6)

start_time = time()
pdf_interp(x_fine)
print("interp1d run time: {}".format(time() - start_time))

start_time = time()
u(x_fine)
print("UnivariateSpline run time: {}".format(time() - start_time))