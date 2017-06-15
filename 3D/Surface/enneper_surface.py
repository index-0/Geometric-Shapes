#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=plt.figaspect(1))

u = np.linspace(-np.pi, np.pi, endpoint=True, num=30)
v = np.linspace(-np.pi, np.pi, endpoint=True, num=30)
u, v = np.meshgrid(u, v)

x = u * (1 - u ** 2 / 3 + v **2) / 3
y = -v * (1 -v ** 2 / 3 + u ** 2) / 3
z = (u ** 2 - v ** 2) / 3

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_surface(x, y, z, cmap=plt.cm.Spectral)
ax.set_title('Enneper Surface')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

scale = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
ax.auto_scale_xyz(*[[np.min(scale), np.max(scale)]]*3)

plt.show()

