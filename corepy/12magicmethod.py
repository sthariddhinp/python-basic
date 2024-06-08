# Magic Methods in Class
class Car():
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
    def drive(self):
        print("The Person drives the car.")

c = Car(3,6,"diesel")
print(dir(c))  # magic method are __<method>__

# We can override the magic method: __str__
class Car():
    def __new__(self,windows,doors,enginetype):
        print("The object has strated getting initialized.")
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
    def __str__(self):
        return "the object has been initialized"
    def drive(self):
        print("The Person drives the car.")

c = Car(3,6,"diesel")
print(c) 

# If we want to print the size of object we can use __sizeof__ magic method
print(c.__sizeof__())
# We can also override this magic method too.

## __new__ magic method will get inialized at the first
