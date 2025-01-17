import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Viz:
    def __init__(self):
        pass

    @staticmethod
    def render_2d(cube):
        """
        Prints a 2D unwrapped render with the actual state of the passed cube variable.
        :param cube:
        :return:
        """
        c = cube
        unwrap = f"""
         |{c['r'][0]}|{c['r'][1]}|{c['r'][2]}|
         |{c['r'][3]}|{c['r'][4]}|{c['r'][5]}|
         |{c['r'][6]}|{c['r'][7]}|{c['r'][8]}|
|{c['b'][0]}|{c['b'][1]}|{c['b'][2]}|{c['w'][0]}|{c['w'][1]}|{c['w'][2]}|{c['g'][0]}|{c['g'][1]}|{c['g'][2]}|\
{c['y'][0]}|{c['y'][1]}|{c['y'][2]}|
|{c['b'][3]}|{c['b'][4]}|{c['b'][5]}|{c['w'][3]}|{c['w'][4]}|{c['w'][5]}|{c['g'][3]}|{c['g'][4]}|{c['g'][5]}|\
{c['y'][3]}|{c['y'][4]}|{c['y'][5]}|
|{c['b'][6]}|{c['b'][7]}|{c['b'][8]}|{c['w'][6]}|{c['w'][7]}|{c['w'][8]}|{c['g'][6]}|{c['g'][7]}|{c['g'][8]}|\
{c['y'][6]}|{c['y'][7]}|{c['y'][8]}|
         |{c['o'][0]}|{c['o'][1]}|{c['o'][2]}|
         |{c['o'][3]}|{c['o'][4]}|{c['o'][5]}|
         |{c['o'][6]}|{c['o'][7]}|{c['o'][8]}|
        """
        # Render Unwrapped picture
        print(unwrap)

    @staticmethod
    def render_3d(cube): #todo figure out how to render our own matrix
        # https://www.geeksforgeeks.org/how-to-draw-3d-cube-using-matplotlib-in-python/
        # Create axis
        axes = [3, 3, 3]
        # Create Data
        data = np.ones(axes, dtype=bool)
        # Control colour
        colors = np.empty(axes + [3], dtype=int)
        colors[0] = [1, 0, 0]  # red
        colors[1] = [0, 1, 0]  # green
        colors[2] = [0, 0, 1]  # blue
        # Plot figure
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # Voxels is used to customizations of
        # the sizes, positions and colors.
        ax.voxels(data, facecolors=colors, edgecolors='black')
        # it can be used to change the axes view
        ax.view_init(50, 0)

        return plt.show()
