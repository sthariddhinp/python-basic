# Class Methods and Class Variables
# Class Method: It is a method that is used to update/change the value of class variable only once.
# Suppose my goal is to upgrade my base price as year chnage by certain % rate.
# Then our class method will exists to do it.
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

# different ways to access instance or class variable
#1.
car1 = Car(3,6,2000)
print(car1.base_price)

#2.
print(Car.base_price)

# What if I want to chnage my base price in 2024 by 10%
# so to do this, we just call class method with appropriate prameter
Car.revise_base_price(0.10)
print(Car.base_price)

# Let's create an instance of Car
car2=Car(2,2,3000)
print(car2.base_price) # Here we saw that our base price is incresed for that car2 object.
