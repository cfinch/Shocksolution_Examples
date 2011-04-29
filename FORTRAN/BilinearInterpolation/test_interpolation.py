#!/usr/bin/env python
from numpy import *
import interp
from PlotUtils.PlotUtils3D import rect_surface_plot

x_array = arange(-2.0, 2.1, 0.2)
y_array = x_array.copy()
z_array = empty([len(x_array), len(y_array)])

for i in range(len(x_array)):
    for j in range(len(y_array)):
        z_array[i,j] = x_array[i]*y_array[j]*exp(-x_array[i]**2 - y_array[j]**2)

rect_surface_plot(x_array, y_array, z_array, "original")

x_interpolated = arange(-2.0, 2.1, 0.1)
y_interpolated = x_interpolated.copy()
z_interpolated = empty([len(x_interpolated), len(y_interpolated)])

for i in range(len(x_interpolated)):
    for j in range(len(y_interpolated)):
        x = x_interpolated[i]
        y = y_interpolated[j]
        z_interpolated[i,j] = interp.interpolation.interpolate(len(x_array),
                x_array, len(y_array), y_array, z_array, x, y, delta=1e-5)

rect_surface_plot(x_interpolated, y_interpolated, z_interpolated, "interpolated")
