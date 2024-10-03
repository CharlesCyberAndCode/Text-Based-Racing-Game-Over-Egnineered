### Text Based Racing Game Main
import math


# Will have these filled with different values to represent the car user has chosen.
# Engine will be the horsepower they have for now Will create list to have names and values organized
engineList = [300,150]
# Tires as well will have values relating to a named part for user to buy
tireList = [1.2,1.5]
# Will figure out bodies. Bodies need 3 values at the moment, so may simplify to 3 lists ->
# A bodiesCD list for coefficient of drag, a bodiesFA for frontal area, ->
# and a bodiesCOG for center of gravity. Currently it shows CD
### MAY STILL USE THIS WILL PROBABLY USE THE CLASS AND OBJECTS INSTEAD

# Main car class that all others will be from
# Will implement body variables in future
class Car:
    def __init__(self, engine, tire):
        self.engine = engine
        self.tire = tire
        pass
## Body variable has too many things to convey, will take variables from this class for user car
class Body:
    def __init__(self,coefDrag,cog,weight,frontal):
        self.coefDrag = coefDrag
        self.cog = cog
        self.weight = weight
        self.frontal = frontal
        pass



# Users car. This will change as the game goes on.     
userCar = Car(engineList[0], tireList[0])
print(userCar.engine)
print(userCar.tire)

#First AI car that will have a set part collection.
johnCar = Car(engineList[1], tireList[1])
## johnCar.engine = engineList[0]
# simple way to change object values based on user input

