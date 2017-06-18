#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=plt.figaspect(1))

angle = float(input("angle: "))
r = float(input("radius: "))
c = float(input("c: "))

n = angle / 360

u = np.linspace(0, r, endpoint=True, num=11 * n)
v = np.linspace(-np.deg2rad(angle), np.deg2rad(angle), endpoint=True, num=22 * n)
u, v = np.meshgrid(u, v)

x = u * np.cos(v)
y = u * np.sin(v)
z = c * v

mpl.rc('text', usetex=True)
mpl.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
mpl.rcParams['axes.labelsize'] = 15

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_surface(x, y, z, cmap=plt.cm.Spectral)
ax.set_title('$Helicoid$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')

lim = (max(abs(max(np.max(x), np.max(y), np.max(z))), abs(min(np.min(x), np.min(y), np.min(z)))))

ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_zlim(-lim, lim)

plt.show()

