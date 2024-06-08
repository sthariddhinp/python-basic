### Functions ###
# Why Functions
# Function Definition
# Positional and Keyword Arguments in Functions

# num = 12
# if num%2==0:
#     print("The number is even")
# else:
#     print("The number is odd")

def even_odd(num):
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")

even_odd(12)



# Print Vs Return
def hello():
    print("Hello world!!")

hello()

# If we store the function into a variable value:
value = hello()
print(value)   # We can see the it will print None , because our hello() function has not any return value

def hello():
    return "Hello world!!"

value = hello()
print(value)

# Positional and Keyword Arguments 
def helloworld(name,age=28):
    print("My name is {} and age is {}.".format(name,age))

helloworld("Prem")  # here we have only pass only one value and we get anther value by default
                    # The value that have to required to pass while function call is positional argument 
                    # and default value which has pass as key value pair is a keyword argument in function definition


# Another way to define positional and keyword arugments
def hello(*args,**kwargs):
    print(args)
    print(kwargs)

hello("Riddhi","Prem",age=28,dob=1994)

#alternative
lst = ["Riddhi","Prem"]
dict_args = {'age':28,'dob':1994}

hello(lst,dict_args)  # here our hello() method assume both arugment as positonal arugments so to distinguish it. we have to pass * and **
hello(*lst,**dict_args)


# Demo: To find Even and Odd number in list?
lst = [1, 2, 3, 4, 5, 6, 7, 8]

def oddevensum(lst):
    even_sum = 0
    odd_sum = 0
    for i in lst:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return even_sum, odd_sum

even_sum, odd_sum = oddevensum(lst)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
