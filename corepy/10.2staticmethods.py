## Static Methods

# when we define static method, we don't have to provide instance parameter nor class parameter 
# Even though we don't provide that instance or class parameter, we can call that method with the help of class.
# Static method execute more faster then normal non static method.

# As soon as a class is loaded the first this that is initilaized i.e. static method
# Static method initalized only one time even your whole program is loaded.
# Multiple copies of static method can't be created.

import datetime
now = datetime.datetime.now()

class Car:
    base_price = 100000   # class variable or instance variable
    def __init__(self,windows,doors,power):
        self.windows=windows
        self.doors=doors
        self.power=power
    def what_base_price(self):
        print("The base price is {}".format(self.base_price))

    @classmethod
    def revise_base_price(cls,inflation):
        cls.base_price=cls.base_price+cls.base_price*inflation
    @staticmethod
    def check_year():
        if now.year==2024:
            return True
        else:
            return False

print(Car.check_year())

car1 = Car(2,3,1000)

if(car1.check_year()):
    pass
else:
    Car.revise_base_price()

print(car1.base_price)