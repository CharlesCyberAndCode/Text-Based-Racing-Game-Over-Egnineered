### Text Based Racing Game Main
import math

'''
VARIABLES AND CLASS INITIALIZATION
'''
# Will have these filled with different values to represent the car user has chosen.
# Engine will be the horsepower they have for now Will create spreadsheet to have ->
# names and values organized for all variables
engineList = [300,150,50]
# Tires as well will have values relating to a named part for user to buy
tireList = [.4,.5,.6,.8,.9,1,1.2]
# Will figure out bodies. Bodies need 3 values at the moment, so may simplify to 3 lists ->
# A bodiesCD list for coefficient of drag, a bodiesFA for frontal area, ->
# and a bodiesCOG for center of gravity. Currently it shows CD
### MAY STILL USE THIS WILL PROBABLY USE THE CLASS AND OBJECTS INSTEAD

# Main car class that all others will be from
# Will implement body variables in future
class Car:
    def __init__(self, engine, tire,cog,weight,frontal,coefDrag,):
        self.engine = engine
        self.tire = tire
        self.cog = cog
        self.weight = weight
        self.frontal = frontal
        self.coefDrag = coefDrag
        pass
## Body variable has too many things to convey, will take variables from this class for user car
class Body:
    def __init__(self,coefDrag,cog,weight,frontal):
        self.coefDrag = coefDrag
        self.cog = cog
        self.weight = weight
        self.frontal = frontal
        pass
suv = Body(.45,.5,1750,2.75)
van = Body(.6,1,2200,3.5)
sport = Body(.3,.3,1350,2)
muscle = Body(.35,.3,1450,2.2)
miura = Body(.25,.25,1050,1.8)
beetle = Body(.4,.45,850,1.6)


# Users car. This will change as the game goes on.     
userCar = Car(engineList[0], tireList[0])
print(userCar.engine)
print(userCar.tire)

#First AI car that will have a set part collection.
johnCar = Car(engineList[1], tireList[1])
## johnCar.engine = engineList[0]
# simple way to change object values based on user input

'''
CODE FOR AI CARS
'''


'''
MAIN LOOP
'''
