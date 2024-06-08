## Object Oriented Programming
# class: It is the blueprint of an object.
# object: It is an instance of class.

class Bike:
    pass

bike1 = Bike()
print(bike1)

bike1.wheels=2
bike1.engine=1
print(bike1.wheels)

bike2 = Bike()
bike2.wheels=3
bike2.engine=2
print(bike2.engine)
bike2.engineType="petrol"
print(bike2.engineType)

## It is the bad approach of oop; here any number of attribute can be created by anyone.

print(dir(bike2))  # inbuit function of an object

# we can see many inbuilt function on an object. Here __init__ which is act like a contructor

class Bike:
    def __init__(self,wheels,enginetype):
        self.wheel=wheels
        self.engineTypes=enginetype
    
    def getEngineType(self):
        return "It is a {} bike.".format(self.engineTypes)

bike1 = Bike(2,"petrol")   # when we create an object; it will call __init__() method which act as like consturctor, will construct instance variable and allocate memory for it
bike2 = Bike(3,"disel")
print(bike1.wheel)
print(bike1.getEngineType())
print(bike2.wheel)
print(bike2.getEngineType())