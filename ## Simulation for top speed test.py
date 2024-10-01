## Simulation for top speed test

import math

hpInWatts = 300*746
#Drag coef
cd = .4
## Frontal Area
a = 3.5
## Air density
rho = 1.225
## Initial Velocity
v = 0
## Step for time to find vel max
time_step = .1
max_speed = 0

while True:
    drag = .5 * rho * cd * a * v**2
    
    powerNeed = drag * v 
    
    hpInWatts
    
    if powerNeed >= hpInWatts:
        break
    
    v += 1
    
    topSpeed = v*2.237
    
print(f"Top speed for this vehicle is: {topSpeed:.2f} m/h")