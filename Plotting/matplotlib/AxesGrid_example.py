#!/usr/bin/env python

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.axislines import Subplot

fig1 = plt.figure(1, (3,3), facecolor='white')

ax1 = Subplot(fig1, 111)
fig1.add_subplot(ax1)

ax1.axis["right"].set_visible(False)
ax1.axis["top"].set_visible(False)

plt.show()

