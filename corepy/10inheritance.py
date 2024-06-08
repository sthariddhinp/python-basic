## Inheritance Concept
# Note: All the class variables or instance variable are public
## Car Blueprint
class Car():
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
    def drive(self):
        print("The Person drives the car.")

car = Car(3,6,"diesel")

print(car.drive())

class audi(Car):
    def __init__(self,windows,doors,enginetype,enableai):
        super().__init__(windows,doors,enginetype)
        self.enableai=enableai
    def selfdriving(self):
        print("Audi support self driving")

audi1 = audi(5,5,"diesel",True)
print(dir(audi1))    # shows all the parameters of parent & child class
print(audi1.windows)
print(audi1.drive())
print(audi1.selfdriving())