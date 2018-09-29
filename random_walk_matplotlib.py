import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors
from matplotlib import cm
from random_walk import RandomWalk
from random_args_parser import RandomArgsParser

fig = plt.figure()

def color(rwalk):
    colors_map = "jet"
    cs = [i for i in range(0, rwalk.array_size+1)]
    cmx = plt.get_cmap(colors_map)
    c_norm = colors.Normalize(vmin=min(cs), vmax=max(cs))
    scalar_map = cm.ScalarMappable(norm=c_norm, cmap=cmx)
    return scalar_map, cs

def print_plot(rwalk):
    if rwalk.dim_size == 2:
        ax = fig.add_subplot(111)
        print("2D")
        scalar_map, cs = color(rwalk)
        ax.scatter(rwalk.dim_array[0], rwalk.dim_array[1], cmap=scalar_map.to_rgba(cs), marker='o', s=1)
        scalar_map.set_array(cs)
    elif rwalk.dim_size == 3:
        print("3D")
        ax = fig.add_subplot(111, projection="3d")
        scalar_map, cs = color(rwalk)
        ax.scatter(rwalk.dim_array[0], rwalk.dim_array[1], rwalk.dim_array[2], c=scalar_map.to_rgba(cs), marker='o', s=1)
        scalar_map.set_array(cs)
        ax.set_zlabel('Z label')
    ax.set_xlabel('X label')
    ax.set_ylabel('Y label')


def main():
    rwalk = RandomWalk()
    rwalk.array_size, rwalk.dim_size = RandomArgsParser.read_args(RandomArgsParser, sys.argv, rwalk.array_size, rwalk.dim_size)
    print(rwalk.dim_size)
    rwalk.gen_dwalk()
    if rwalk.dim_size >= 2:
        print_plot(rwalk)
        plt.show()

if __name__ == "__main__":
    main()
