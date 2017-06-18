#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri

fig = plt.figure(figsize=plt.figaspect(1))

u = np.linspace(0, 2 * np.pi, endpoint=True, num=30)
v = np.linspace(0, 2 * np.pi, endpoint=True, num=30)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()

R = float(input("Insert R (major radius): "))
r = float(input("Insert r (minor radius): "))

x = np.cos(v) * (R + r * np.cos(u))
y = np.sin(v) * (R + r * np.cos(u))
z = r * np.sin(u)

tri = mtri.Triangulation(u, v)

mpl.rc('text', usetex=True)
mpl.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
mpl.rcParams['axes.labelsize'] = 15

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_title('$Torus$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_xlim(-R, R)
ax.set_ylim(-R, R)
ax.set_zlim(-R, R)

plt.show()
