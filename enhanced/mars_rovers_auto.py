#!/usr/bin/python3

import os.path

# initialise global variables
# amount of rovers that landed
rover_count = 2
# orientation list
orient = ['N', 'E', 'S', 'W']
# movement of rovers, 1 grid point
move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
# commands sent to rovers
instructions = {'L': 'tleft', 'R': 'tright', 'M': 'move'}


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
        self.intersection = set(intersection)

    def tright(self):
        """
        turning right method
        """
        self.bearing = orient[(orient.index(self.bearing) + 1) % len(orient)]

    def tleft(self):
        """
        turning left method
        """
        self.bearing = orient[(orient.index(self.bearing) - 1) % len(orient)]

    def move(self):
        """
        moving forward 1 grid point method
        """
        xmod = self.x + move[self.bearing][0]
        ymod = self.y + move[self.bearing][1]
        # check intersection to see if nrover is not the same position as mrover
        if (xmod, ymod) not in self.intersection:
            if xmod <= self.xmax and xmod >= 0:
                self.x = xmod
            if ymod <= self.ymax and ymod >= 0:
                self.y = ymod
            else:
                print('Out of bounds try again!!')
                exit()
        else:
            print('rovers cannot occupy the same spot, try again!!')
            exit()


if __name__ == '__main__':
    """
    future improvements
    1. add auto manual functionality, auto: run a input instructions file
    2. manually add the rovers and instructions
    3. choose amount of rovers to deploy
    """
    auto = input('manual override or auto? Enter (A | auto) or (M | manual)\n')
    if auto or auto.upper() in ['A', 'auto']:
        file = input('Select file name(make sure file is in this directory):')
        if os.path.exists(file):
            intersection = set([])
            data = []
            num_lines = sum(1 for line in open(file)) - 1
            rover_count = int(num_lines / 2)
            for line in open(file):
                data.append(line.rstrip())
            xmax, ymax = map(int, data[0].split())
            intersection = set([])
            results = []
            count_a = 1
            count_b = 2
            for _ in range(rover_count):
                x, y, bearing = data[count_a].split()
                rover = Rover(int(x), int(y), xmax, ymax, bearing, intersection)
                count_a += 2
                for command in data[count_b]:
                    getattr(rover, instructions[command])()
                count_b += 2
                intersection.add((rover.x, rover.y))
                results.append((rover.x, rover.y, rover.bearing))
            for x, y, z in results:
                print(x, y, z)
            exit()
        else:
            print('file does not exist, make sure file is in this directory)')
    elif auto in ['M', 'manual']:
        rover_count = int(input('How many rovers would you like to deploy?:'))
        # get grid size from input
        xmax, ymax = map(int, input('Enter grid size:').split())
        # initialise intersection rovers soon to be positions
        intersection = set([])
        check_coords = []
        results = []
        # count_a for rover_count for loop
        count_a = 1
        # count_b for instructions for loop
        count_b = 1
        # iterate over rover count
        for _ in range(rover_count):
            # get rover coordinates and NESW bearing
            x, y, bearing = input('coordinates for rover %d:' % count_a).split()
            count_a += 1
            # check to see that you havent deployed rovers with the same coordinates
            if [x, y, bearing] not in check_coords:
                check_coords.append([x, y, bearing])
                rover = Rover(int(x), int(y), xmax, ymax, bearing, intersection)
                # iterate over instructions string
                for i in input('instructions for rover %d:' % count_b):
                    if i not in 'MRL':
                        # exit if not valid instruction
                        print('invalid instruction "%s": use M or R or L - please try again' % i)
                        exit()
                    else:
                        # store and run instructions
                        getattr(rover, instructions[i])()
                count_b += 1
                # add nrovers coords to intersection
                intersection.add((rover.x, rover.y))
                results.append((rover.x, rover.y, rover.bearing))
            else:
                print('2 or more of your rovers share the same spot, please try again')
                exit()
        # print results
        for x, y, z in results:
            print(x, y, z)
    else:
        print('Are you sure you typed the correct choice? Enter (A | auto) or (M | manual)')
        exit()


