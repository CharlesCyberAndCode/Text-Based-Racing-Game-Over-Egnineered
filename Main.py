### Text Based Racing Game Main
import math


# Will have these filled with different values to represent the car user has chosen.
engineList = [300,150]
tireList = [1.2,1.5]
bodyList = [.5,.7]

class Car:
    def __init__(self, engine, body, tire):
        self.engine = engine
        self.body = body
        self.tire = tire
        pass
    
userCar = Car(engineList[0], bodyList[0], tireList[0])
print(userCar.engine)
print(userCar.body)
print(userCar.tire)

johnCar = Car(engineList[1], bodyList[1], tireList[1])
johnCar.engine = engineList[0]

print(johnCar.engine)
print(johnCar.body)
print(johnCar.tire)
