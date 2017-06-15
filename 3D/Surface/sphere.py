#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=plt.figaspect(1))

u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=25)
v = np.linspace(0 , np.pi, endpoint=True, num=25)
u, v = np.meshgrid(u, v)

x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_surface(x, y, z, cmap=plt.cm.Spectral)
ax.set_title('Sphere')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

scale = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
ax.auto_scale_xyz(*[[np.min(scale), np.max(scale)]]*3)

plt.show()
