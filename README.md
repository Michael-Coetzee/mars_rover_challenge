# Mars Rover Challenge

The problem below requires some kind of input. You are free to implement any mechanism for feeding input into your solution (for example, using hard coded data within a unit test). You should provide sufficient evidence that your solution is complete by, as a minimum, indicating that it works correctly against the supplied test data.  

We highly recommend using a unit testing framework such as JUnit or NUnit. Even if you have not used it before, it is simple to learn and incredibly useful.  

The code you write should be of production quality, and most importantly, it should be code you are proud of.  

MARS ROVERS  

A squad of robotic rovers are to be landed by NASA on a plateau on Mars.  

This plateau, which is curiously rectangular, must be navigated by the rovers so that their on board cameras can get a complete view of the surrounding terrain to send back to Earth.  

A rover's position is represented by a combination of an x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.  

In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot.  

'M' means move forward one grid point, and maintain the same heading.  

Assume that the square directly North from (x, y) is (x, y+1).  

Input:  

The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.  

The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau.  

The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation.  

Each rover will be finished sequentially, which means that the second rover   won't start to move until the first one has finished moving.  

Output:  

The output for each rover should be its final co-ordinates and heading.  

Test Input:  

5 5  

1 2 N  

LMLMLMLMM  

3 3 E  

MMRMMRMRRM  

Expected Output:  

1 3 N  

5 1 E  


## assumptions:
1. first input = grid size  
2. second input = position of n rover on grid  
3. third input = command given to rovers  
4. more than one rover can be deployed  
5. first input is hard coded  
6. even input will iterate between each rover deployed  
7. odd input will iterate between each instruction given to the rover  
8. rovers cannot exceed the grid size coordinates   
9. rovers need to take turns between commands, cannot run concurrently  
10. rovers cannot share the same coordinates after running command  
11. rovers cannot be deployed to the same coordinates  
12. will run over telnet or ssh session


## installation basic version  
```
git clone https://github.com/Michael-Coetzee/mars_rover_challenge.git  

cd mars_rover_challenge/basic  

python mars_rovers.py  

```

## future improvements
1. ~~add auto functionality - run a input instructions file, will pick up on rover amount~~
2. ~~manually add the rovers and instructions~~
3. ~~choose amount of rovers to deploy~~
4. grid/ui to visualise rovers
5. warning messages to be more dynamic, will be able to pinpoint which rover failed


