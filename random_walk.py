from random import getrandbits
from numpy import fromiter
from numpy import arctan2
import numpy as np

class RandomWalk():
    def __init__(self):
        self.array_size = 100000
        self.dim_size = 3 
        self.dim_array = 0
        self.color = 0
    #random walk generator for numpy arrays
    def fill_array(self):
        next_value = 0
        for i in range(-1, self.array_size):
            #fast coin flipper
            if not getrandbits(1):
                next_value -= 1
            else:
                next_value += 1
            yield next_value

    #Returns a numpy array that is filled with a single coordinate of a random walk
    def one_dwalk_gen(self):
        return fromiter(self.fill_array(), dtype='float')

    #Generate the values for an n-dimensional 
    def gen_dwalk(self):
        self.dim_array = np.array([self.one_dwalk_gen() for i in range(0, self.dim_size)])
        if self.dim_size >= 2:
            self.color = np.array(arctan2(self.dim_array[0], self.dim_array[1]))
