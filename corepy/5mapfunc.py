## Map Function 

def even_odd(num):
    if num %2==0:
        return "The {} is Even.".format(num)
    else:
        return "The {} is Odd.".format(num)

print(even_odd(2))

# What if I want to find odd even from list of numbers?
lst = [1,2,3,4,5,6,7,8,14,18,20,50,67]
## We can use it in our even_odd() function using for loop; which will take time, 
# but we can easily get this by using Map function


#syntax: map(function,iterable_parameter)

print(map(even_odd,lst))     # It uses Lazy loading techique i.e. initally memory is not initalized, we need to convert it into list

print(list(map(even_odd,lst))) 