#!/usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.text import Text

import numpy

fig1 = plt.figure(facecolor='white')
ax1 = plt.axes(frameon=False)

#ax1.set_frame_on(False)     # Alternate way to turn frame off

ax1.get_xaxis().tick_bottom()   # Turn off ticks at top of plot

#ax1.axes.get_xaxis().set_visible(False)
ax1.axes.get_yaxis().set_visible(False)     # Hide y axis

# Add a plot
y_offset = 2.0
x = numpy.arange(-5.0, 5.0, 0.1)
for i in range(3):
    ax1.plot(x, numpy.sin((i + 1) * x) + i * y_offset, label=str(i+1))

plt.legend(loc='lower right')

# Draw the x axis
xmin, xmax = ax1.get_xaxis().get_view_interval()
ymin, ymax = ax1.get_yaxis().get_view_interval()
ax1.add_artist(Line2D((xmin, xmax), (ymin, ymin), color='black', linewidth=2))

plt.show()

