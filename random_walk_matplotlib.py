import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors
from matplotlib import cm
from random_walk import RandomWalk
from random_args_parser import RandomArgsParser

#if '-p' in sys.argv:
    #import cProfile

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

def color(rwalk):
    colorsMap = "jet"
    cs = [i for i in range(0, rwalk.array_size+1)]
    cmx = plt.get_cmap(colorsMap)
    cNorm = colors.Normalize(vmin=min(cs), vmax=max(cs))
    scalarMap = cm.ScalarMappable(norm=cNorm, cmap=cmx)
    return scalarMap, cs

def print_plot(ax, rwalk):
    ax.set_xlabel('X label')
    ax.set_ylabel('Y label')
    if rwalk.dim_size == 2:
        print("2D")
        scalarMap, cs = color(rwalk)
        ax.scatter(rwalk.dim_array[0], rwalk.dim_array[1], cmap=scalarMap.to_rgba(cs), marker='o', s=1)
        scalarMap.set_array(cs)
    elif rwalk.dim_size == 3:
        print("3D")
        scalarMap, cs = color(rwalk)
        ax.scatter(rwalk.dim_array[0], rwalk.dim_array[1], rwalk.dim_array[2], c=scalarMap.to_rgba(cs), marker='o', s=1)
        scalarMap.set_array(cs)
        ax.set_zlabel('Z label')

def main():
    rwalk = RandomWalk()
    rwalk.array_size, rwalk.dim_size = RandomArgsParser.read_args(RandomArgsParser, sys.argv, rwalk.array_size, rwalk.dim_size)
    rwalk.gen_dwalk()
    if rwalk.dim_size >= 2:
        print_plot(ax, rwalk)
        plt.show()

if __name__ == "__main__":
    main()