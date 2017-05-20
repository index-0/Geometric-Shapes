import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri

fig = plt.figure(figsize=plt.figaspect(1))

u = np.linspace(0, 2 * np.pi, endpoint=True, num=50)
v = np.linspace(0, 2 * np.pi, endpoint=True, num=50)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()

R = int(input("Insert R (major radius): "))
r = int(input("Insert r (minor radius): "))

x = np.cos(v) * (R + r * np.cos(u))
y = np.sin(v) * (R + r * np.cos(u))
z = r * np.sin(u)

tri = mtri.Triangulation(u, v)

ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles)
ax.set_title('Torus')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-R, R)
ax.set_ylim(-R, R)
ax.set_zlim(-R, R)

plt.show()
