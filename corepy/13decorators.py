## Decorators ##

## function copy
## clousers
## decorators

# Function copy: suppose we define a function and assign it to some variable and delete the function, then
# also we can access the function due to the function copy

# def welcome():
#     print("Welcome to Nepal")

# w = welcome()

# w   # this wil not return or print any outcome


## Function Copy ##
def welcome():
    return "Welcome to Nepal Return"

wel = welcome()
del welcome

print(wel)

#welcome()   # It will shows an error 'welcome' is not defined

## Clousers ##
# Function written inside a function is clauser.
# whatever you pass into parent function will get accessible in sub functions in clousers.

def main_welcome(msg):
    # msg = "Hello Learners"
    def sub_welcome():
        print("Welcome to Nepal clouser.")
        print(msg)
        print("Let's Learn share and grow together.")
    return sub_welcome()

main_welcome("Hello Learners")

## Clousers & inital Decorators
# Inside a function when we pass inbuilt function as a parameter instead of specific variable or message

def main_welcome(func):
    # msg = "Hello Learners"
    def sub_welcome():
        print("Welcome to Nepal clouser.")
        func("Nepal Nepal")
        print("Let's Learn share and grow together.")
    return sub_welcome()

main_welcome(print)

def main_welcome(func):
    # msg = "Hello Learners"
    def sub_welcome():
        print("Welcome to Nepal clouser.")
        print(func([1,2,3,4,5,6,7]))
        print("Let's Learn share and grow together.")
    return sub_welcome()

main_welcome(len)


## Decorators 
# Decorator is, Where you are calling function within the function and also you are passing function as a paremeter.

def main_welcome(func):
    # msg = "Hello Learners"
    def sub_welcome():
        print("Welcome to Nepal clouser.")
        func()
        print("Let's Learn share and grow together.")
    return sub_welcome()

def my_name():
    print("My Name is Riddhi K. Shrestha.")

main_welcome(my_name)

# Alternate way to define decorator or calling decorator is:
@main_welcome
def my_name():
    print("My name is RKS, from decorators style.")

# #MAin use of decorators is the resusablity of code.
