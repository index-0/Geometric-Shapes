#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri

fig = plt.figure(figsize=plt.figaspect(1))

zmax = float(input("Maximum height:  "))
zmin = float(input("Minimum height: "))
c = float(input("c: "))

u = np.linspace(-np.pi, np.pi, endpoint=True, num=30)
v = np.linspace(zmin, zmax, endpoint=True, num=30)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()

x = c * np.cosh(v / c) * np.cos(u)
y = c * np.cosh(v / c) * np.sin(u)
z = v

tri = mtri.Triangulation(u, v)

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_title('Catenoid')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

lim = (max(abs(max(max(x), max(y), max(z))), abs(min(min(x), min(y), min(z)))))

ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_zlim(-lim, lim)

plt.show()

