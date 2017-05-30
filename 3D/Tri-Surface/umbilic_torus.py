#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri

fig = plt.figure(figsize=plt.figaspect(1))

u = np.linspace(-np.pi, np.pi, endpoint=True, num=50)
v = np.linspace(-np.pi, np.pi, endpoint=True, num=50)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()

x = np.sin(u) * (7 + np.cos(u / 3 - 2 * v) + 2 * np.cos(u / 3 + v))
y = np.cos(u) * (7 + np.cos(u / 3 - 2 * v) + 2 * np.cos(u / 3 + v))
z = np.sin(u / 3 - 2 * v) + 2 * np.sin(u / 3 + v)

tri = mtri.Triangulation(u, v)

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_title('Umbilic Torus')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

lim = (max(abs(max(max(x), max(y), max(z))), abs(min(min(x), min(y), min(z)))))

ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_zlim(-lim, lim)

plt.show()
