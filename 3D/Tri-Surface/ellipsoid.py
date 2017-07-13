#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri

fig = plt.figure(figsize=plt.figaspect(1))

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

u = np.linspace(0, 2 * np.pi, endpoint=True, num=30)
v = np.linspace(0 , np.pi, endpoint=True, num=30)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()

x = a * np.cos(u) * np.sin(v)
y = b * np.sin(u) * np.sin(v)
z = c * np.cos(v)

tri = mtri.Triangulation(u, v)

mpl.rc('text', usetex=True)
mpl.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
mpl.rcParams['axes.labelsize'] = 15

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_title('$Ellipsoid$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')

lim = (max(abs(max(max(x), max(y), max(z))), abs(min(min(x), min(y), min(z)))))

ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_zlim(-lim, lim)

plt.show()

