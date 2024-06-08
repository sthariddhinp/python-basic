# Basic of Python Programming

## Datatypes in Py
## Variable and Variable Assignment
## Print formating

### DataTypes ###

# Numbers #
print(1+1)
print(2*10)
print(10/2)
print(10%2)
print(10**2)  # 10 to the power of 2
print(10 * ' Nepal')
## CHeck the data types
print(type(1))
print(type("Nepal"))

# Strings #
print("Hello")
print('World')

## Variable & Variable Assignment ##
    # syntax
    # var_name = values
a = 10
print(type(a))
b = "Riddhi K Shrestha"
print(type(b))
    # Mathematical operaiton with variable
a = 10
b = 20
print(a*b)
print(a/b)
print(a%b)
print((a*b)+(a/b))   # BODMAS Rule


## Various ways of printing
print("Nepal")

first_name = "Riddhi"
last_name = "Shrestha"

print("My first name is {} and last name is {}".format(first_name,last_name))
print("My First name is {first} and last name is {last}".format(first=first_name,last=last_name))

print(len("Riddhi K Shrestha"))



# Boolean #
    ## Boolean and Logical Operators ##

print(True,False)
print(type(True))
print(bool())

## InBuilt Functions
my_name = "Riddhi Shrestha"
print(my_name.isalnum())   # check if all char are numbers
print(my_name.isalpha())   # chcek if all char in the string are alphabetic
print(my_name.isdigit())    # chcek if string contain digits
print(my_name.istitle())    # check if string contain title word
print(my_name.isupper())    # check if string contain upper case
print(my_name.isspace())    # check if string contains spaces
print(my_name.endswith('a')) # check if the string endwith a 'a'
print(my_name.startswith('R'))

## Boolean and Logical Operations
print(True and True)
print(True and False)
print(True or False)
print(True or True)

## Is vs == 
lst1 = ["Riddhi","Prem","Rk"]   # store in different memory location
lst2 = ["Riddhi","Prem","Rk"]   # store in different memory location
print(lst1==lst2)               # == will compare the elements equality

print(lst1 is lst2)

lst1 = ["Riddhi","Prem","Rk"]   # store in some memory location
lst2 = lst1                     # same memory location of lst1 is reference to lst2

print(lst1 is lst2)
