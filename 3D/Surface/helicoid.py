#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=plt.figaspect(1))

angle = float(input("angle: "))
r = float(input("radius: "))
c = float(input("c: "))

n = angle / 360

u = np.linspace(0, r, endpoint=True, num=11 * n)
v = np.linspace(0, np.deg2rad(angle), endpoint=True, num=11 * n)
u, v = np.meshgrid(u, v)

x = u * np.cos(v)
y = u * np.sin(v)
z = c * v

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_surface(x, y, z, cmap=plt.cm.Spectral)
ax.set_title('Helicoid')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

scale = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
ax.auto_scale_xyz(*[[np.min(scale), np.max(scale)]]*3)
ax.set_zlim(0)

plt.show()

