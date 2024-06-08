## Python Data Classes
# In Python, the dataclass decorator is a feature introduced in Python 3.7 that provide a concise way to define classes primarily intended to store data.
# It automatically generates several sepecial methods, such as init,repr and equal, based on the class attributes you define. This simplifies the process of creating and working with data-focused classes.

## Import libraries
from dataclasses import dataclass

@dataclass
class Person:
    name:str
    age:int
    profession:str

# The @dataclass decorator automatically generates the following method for you:
#   __init__(): Initializes the object and assigns the provided values to the attributes.
#   __repr__(): Provides a string representation of the object.
#   __eq__(): Implements equality comparision betweeen two objects of the class based on their attributes.

person1=Person("Riddhi",28,"AI Engineer")
print(person1)

@dataclass
class Rectangle:
    width:int
    height:int
    color:str='white'

rect1=Rectangle(12,13)
rect2=Rectangle(23,12,'blue')
print(rect2.color)

@dataclass(frozen=True)
class Point:
    x:int
    y:int

p1=Point(3,4)
print(p1.x,p1.y)
# lets suppose i want to assign the value of the object, due to use of frozon property, it will show error
# p1.x = 12

## Inheritance ##
@dataclass
class Person:
    name:str
    age:int

@dataclass
class Employee(Person):
    emp_id:str
    department:str

p1=Person("Riddhi",28)
e1=Employee("Prem",29,"123","AI")
print(e1.name)

## Nested Dataclasses

@dataclass
class Address:
    street:str
    city:str
    zip_code:str

@dataclass
class Person:
    name:str
    age:str
    address:Address

add1=Address('123 main street','Koteshwor','452542')
per1=Person("Riddhi",29,add1)
print(per1.address)
print(per1.address.street)