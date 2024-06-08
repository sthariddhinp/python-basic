# Iterables vs Iterators

lst = [1,2,3,4,5]
for i in lst:
    print(i)   
# since here we iterate over all the elements of list , we called list as iterable  =>  'List is Iterable'
# when we create a list, then we allocated all values in memory location, when we do for loop to it, it generally iterating through memory location.

# iter(): it will coverts list into an iterator.
lst1 = iter(lst)
print(lst1)

## properties ##
#1.
#  When we convert list into iterator using iter() method, all the value wil not initalized into memory.
#  So, unless n until we call inbuild function i.e. next() . Once we call next() function, then it will initalized first element that prsent inside that iterator.

# To see the iterator element, use next() inbuilt method.

print(next(lst1))  # firs element 1
print(next(lst1))  # second element 2 

### Whatever value store into iterator, it will not store whole value once into memory like list. It will only store only one elment by calling next()

## Another way to reterive iterator's values is just use of for loop, which will initalize list into iterator and loop through end of the loop
for i in lst1:
    print("iterator",i)



## Why we use iterator?
#=> Suppose we have million of lists, if we initalize it into memory, guess how much it wil consume memory.
# If we convert list into iterator, then it will not store into memory until unless we call next() function.