### Simulation for 0-60
import math

'''
VARIABLES
'''
## Weight in kg
weight = 1270
## .8 for average power not just peak, second .8 for mechanical loss. / 26.82 as it is 60 mph ->
## meters per second. Allows to find power of engine at speed. usableHP is converted to newtons
usableHP = .8 * .85 * (290*746) 
## Need to find out realistic grip coef for 60s/70's cars.
coefGrip = .8
## Drag coefficient of the vehicle.
coefDrag = .19
## Frontal Area of the vehicle
frontal = 1.5
## Density of air
p = 1.225
## 60 mph converted and squared for equation
v = 26.82**2
hasPosi = True
isRWD = True
'''
CALCULATIONS
'''
## Simple aero drag model applied constantly as a function of the vehicle at 60 mph
fDrag = .5 * coefDrag * p * frontal * v
## .5 weight as driven wheels presumably only have 50% of weight. Simplified
if isRWD == True:
    fGrip = coefGrip * .54 * ((weight - (weight * .05)) * 9.81)
    ## LSD in rear effect
    if hasPosi == True:
        fGrip = fGrip + (.05 * fGrip)
        
elif isRWD != True:
    fGrip = coefGrip * .48 * ((weight - (weight * .05))  * 9.81)
    ## LSD in front effect 
    if hasPosi:
        fGrip = fGrip + (.05 * fGrip)
## Find minimum force between engine and grip
fNet = min(fGrip,usableHP)
print(fGrip,usableHP)
fNet = fNet - fDrag
## Acceleration, .9 accounting for loss of 10% due to suspension and .97 due to rolling resistance.
a = .9 * .97 * fNet / weight
## Equation for time, target velocity ove acceleration
t60 = (26.82 / a)
## Time for single shift by a skilled driver
t60 = t60 + .35
print(f"0-60 time is {t60:.2f} seconds")
