from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import cm
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
#local import
from random_walk import RandomWalk 

#generate our random walk
rwalk = RandomWalk()
rwalk.array_size = 10000
rwalk.gen_dwalk()

fig = plt.figure()
ax = p3.Axes3D(fig)

x = rwalk.dim_array[0]
y = rwalk.dim_array[1]
z = rwalk.dim_array[2]
# create the 
color = [[i, i, i] for i in range(0, rwalk.array_size)]
color = (color / np.linalg.norm(color)).tolist()

point, = ax.plot([x[0]], [y[0]], [z[0]], '--')

ax.set_xlim([min(x), max(x)])
ax.set_ylim([min(y), max(y)])
ax.set_zlim([min(z), max(z)])

# second option - move the point position at every frame
def update_point(n, rwalk, point):
    point.set_data(np.array([x[0:n], y[0:n]]))
    point.set_3d_properties(z[0:n], 'z')
    data[n%10] = np.random.random((3))
    point.set_color(data)
    return point

ani=animation.FuncAnimation(fig, update_point, rwalk.array_size, fargs=(rwalk, point), interval='1')
plt.show()
