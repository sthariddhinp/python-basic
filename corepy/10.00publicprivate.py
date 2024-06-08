# Public, Protected and Private Access Modifier
### Python never restict something, like other programming like java etc.
# all the class variables are public
class Car:
    def __init__(self,windows,doors,enginetype):
        # when we define variable like below 'windows' it is public type.
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype

audi = Car(4,5,"Diesel")
print(dir(audi))

# all the class variables are protected
# to access protected variable we have to use subclass and superclass.
# overriden only happen from your sublcass.
class Car:
    def __init__(self,windows,doors,enginetype):
        self._windows=windows
        self._doors=doors
        self._enginetype=enginetype

audi = Car(3,2,"Diesel")
print(dir(audi))
# We can only override protected variabe from our subclass/child class
class Truck(Car):
    def __init__(self,windows,doors,enginetype,horsepower):
        super().__init__(windows,doors,enginetype)
        self.horsepower=horsepower

truck=Truck(4,4,"Diesel",4500)
print(dir(truck))
# Override protected variable
truck._doors=6
print(truck._doors)

## Private 
## It can't access anywhere.
# private variable can't be modified from outside of this particular class.
class Car:
    def __init__(self,windows,doors,enginetype):
        self.__windows=windows
        self.__doors=doors
        self.__enginetype=enginetype

audi = Car(3,3,"Diesel")
print(dir(audi))