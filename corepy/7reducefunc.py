### Reduce Function
# Reduce function is a part of Python’s functools module. 
# It’s used to apply a function to all elements of a list, effectively ‘reducing’ the list to a single output. 
# Here’s a simple example

from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x+y, numbers)
print(result)

# Output:
# 15

def product_op(x, y):
    # (This is a placeholder for your complex operation)
    return x * y

numbers = [1, 2, 3, 4, 5]

# We'll use reduce to apply our custom function to these numbers
result = reduce(product_op, numbers)

print(result)

# Output:
# 120

###
# ALL MAP,FILTER AND REDUCE IN ONE

numbers = [1, 2, 3, 4, 5]

# Use map to square the numbers
squares = map(lambda x: x ** 2, numbers)

# Use filter to keep only the squares that are greater than 10
big_squares = filter(lambda x: x > 10, squares)

# Use reduce to find the sum of the big squares
sum = reduce(lambda x, y: x + y, big_squares)

print(sum)

# Output:
# 41
