#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=plt.figaspect(1))

u = np.linspace(-np.pi, np.pi, endpoint=True, num=50)
v = np.linspace(-np.pi, np.pi, endpoint=True, num=50)
u, v = np.meshgrid(u, v)

x = np.sin(u) * (7 + np.cos(u / 3 - 2 * v) + 2 * np.cos(u / 3 + v))
y = np.cos(u) * (7 + np.cos(u / 3 - 2 * v) + 2 * np.cos(u / 3 + v))
z = np.sin(u / 3 - 2 * v) + 2 * np.sin(u / 3 + v)

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_surface(x, y, z, cmap=plt.cm.Spectral)
ax.set_title('Umbilic Torus')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

scale = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
ax.auto_scale_xyz(*[[np.min(scale), np.max(scale)]]*3)

plt.show()
