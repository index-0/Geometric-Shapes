#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri

fig = plt.figure(figsize=plt.figaspect(1))

u = np.linspace(-np.pi, np.pi, endpoint=True, num=25)
v = np.linspace(-np.pi, np.pi, endpoint=True, num=25)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()

x = 1 / 4 * (u ** 3 - 3 * u - 3 * u * v **2)
y = 1 / 4 * (3 * v + 3 * v * u ** 2 - v ** 3)
z = 3 / 4 * (v ** 2 - u ** 2)

tri = mtri.Triangulation(u, v)

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_title('Enneper Surface')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

lim = (max(abs(max(max(x), max(y), max(z))), abs(min(min(x), min(y), min(z)))))

ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_zlim(-lim, lim)

plt.show()

