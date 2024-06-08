# List Comprehension #

# List comprehensions provide a concise way to create lists. 
# It consists of brackets containing an expression followed by a for cluase, then zero or more for or if cluases.
# The expressions can be anything, meaning you can put in all kinds of objects in lists.

lst1 = []
def lst_square(lst):
    for i in lst:
        lst1.append(i*i)
    return lst1

print(lst_square([1,2,3,4,5,6]))

# List comprehension
lst = [1,2,3,4,5,6,7]
lst1 = [i*i for i in lst]
print(lst1)

# square of only even number in the list
lst2 = [i*i for i in lst if i%2==0]
print(lst2)