#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri

fig = plt.figure(figsize=plt.figaspect(1))

angle = float(input("angle: "))
r = float(input("radius: "))
c = float(input("c: "))

n = angle / 360

u = np.linspace(0, r, endpoint=True, num=11 * n)
v = np.linspace(0, np.deg2rad(angle), endpoint=True, num=11 * n)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()

x = u * np.cos(v)
y = u * np.sin(v)
z = c * v

tri = mtri.Triangulation(u, v)

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_title('Helicoid')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

lim = (max(abs(max(max(x), max(y))), abs(min(min(x), min(y)))))

ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_zlim(0, max(z))

plt.show()

