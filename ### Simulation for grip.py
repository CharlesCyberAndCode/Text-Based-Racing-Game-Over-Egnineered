### Simulation for grip
import math


### Tire grip coefficient table
 # ultra perf tire == 1 - 1.2  race slick == 1.3 - 1.5 maybe more.   all season == .6 -.8.   
        # sports tire == .8 - 1.
## grip sim
    # grip = lateral grip
    # tireGrip = coef of friction of the tire
    # weight = weight of car
    # centGrav = center of gravity
    # COGaffect = how muhc center of gravity affects performance. Should be fairly small. maybe .05
    
## Grip model tentative == grip = tireGrip * (scalor for weight being bad/weight) * (1 - .05 * centGrav)
    
tireGrip = 1.2
weight = 1000
centGrav = .2

# CONSTANTS TO KEEP DO NOT MESS WITH UNLESS CALCS REQUIRE IT FOR BALANCING
COGaffect = .8
k = 500

## MODEL IS WORKING
grip = (tireGrip*(k/weight)*(1-COGaffect*centGrav))+.4

print(f"Grip in g force is: {grip:.4f}g's")

