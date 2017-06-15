#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=plt.figaspect(1))

zmax = float(input("Maximum height: "))
zmin = float(input("Minimum height: "))
c = float(input("c: "))

u = np.linspace(-np.pi, np.pi, endpoint=True, num=30)
v = np.linspace(zmin, zmax, endpoint=True, num=30)
u, v = np.meshgrid(u, v)

x = c * np.cosh(v / c) * np.cos(u)
y = c * np.cosh(v / c) * np.sin(u)
z = v

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_surface(x, y, z, cmap=plt.cm.Spectral)
ax.set_title('Catenoid')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

scale = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
ax.auto_scale_xyz(*[[np.min(scale), np.max(scale)]]*3)

plt.show()

