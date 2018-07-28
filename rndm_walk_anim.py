import sys
import numpy as np
import matplotlib.pyplot as plt
from random_walk import RandomWalk
from random_args_parser import RandomArgsParser
from matplotlib.animation import FuncAnimation


#if '-p' in sys.argv:
    #import cProfile

anim_count = 0
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r', animated=True)

rwalk = RandomWalk()
rwalk.array_size = 10000;
rwalk.dim_size = 2
rwalk.gen_dwalk()

def init():
    global rwalk
    ax.set_xlim(np.nanmin(rwalk.dim_array[0]), np.nanmax(rwalk.dim_array[0]))
    ax.set_ylim(np.nanmin(rwalk.dim_array[1]), np.nanmax(rwalk.dim_array[1]))
    return ln,

def update(frame):
    global anim_count
    xdata.append(rwalk.dim_array[0][anim_count])
    ydata.append(rwalk.dim_array[1][anim_count])
    ln.set_data(xdata, ydata)
    anim_count += 1
    return ln,

def main():
    if rwalk.dim_size >= 2:
        ani = FuncAnimation(fig, \
                update, \
                frames=10000,\
                init_func=init, \
                blit=True,
                interval=5,
                save_count=10000)
        ani.save('rndm_walk.mp4',fps=60)

if __name__ == "__main__":
    main()
