#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
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

mpl.rc('text', usetex=True)
mpl.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
mpl.rcParams['axes.labelsize'] = 15

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_surface(x, y, z, cmap=plt.cm.Spectral)
ax.set_title('$Catenoid$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')

lim = (max(abs(max(np.max(x), np.max(y), np.max(z))), abs(min(np.min(x), np.min(y), np.min(z)))))

ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_zlim(-lim, lim)

plt.show()

