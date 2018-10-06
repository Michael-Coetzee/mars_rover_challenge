#!/usr/bin/python3

class Rover:
    """
    calculate and return position of rovers based on input paramters
    """
    def __init__(self, x, y, xmax, ymax, bearing, intersection):
        """
        initialise parameters
        """
        self.x = x
        self.y = y
        self.xmax = xmax
        self.ymax = ymax
        self.bearing = bearing
        self.intersection = intsersection

    def tright(self):
        """
        turning right method 
        """
        self.bearing = orient[(orient.index(self.bearing) + 1) % len(orient)]

