# mars rover challenge

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


# installation basic version  
```
git clone https://github.com/Michael-Coetzee/mars_rover_challenge.git  

cd mars_rover_challenge/basic  

python mars_rovers.py  

```

# future improvements
1. ~~add auto functionality - run a input instructions file, will pick up on rover amount~~
2. ~~manually add the rovers and instructions~~
3. ~~choose amount of rovers to deploy~~
4. grid to visualise rovers


