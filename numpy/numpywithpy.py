## NumPy
##-> It is a general purpose array procesing package.
##-> It provide a high-performance multidimensional array object, and tools for working with these arrays.
## -> It is the fundamental package for scientific computing with Python.

# Array: 
#-> An array is data structure that stores values of same data type.
#-> In Python, this is main difference between arrays and lists. While python lists can
# contain values corresponding to differnt data types, arrays in python can only contain values corresponding to same data type.

# import numpy
import numpy as np 

my_lst = [1,2,3,4]
arr=np.array(my_lst)
print(type(arr))
print(arr) # It is 1 dimension array; because it has one [] with elememts of array
print(arr.shape)  # If it is 1D array, it will only shows number of element in that arrary
## We get (4,) as output means, the array has 4 elements on it.
# Q. Can we convert 1D array to 2D? ->Ans: Yes we can do it by inbuilt function reshape.
#arr.reshape()

# 2D Array
##Multinested Array
lst1=[1,2,3,4,5]
lst2=[2,3,4,5,6]
lst3=[9,7,6,8,9]
arr=np.array([lst1,lst2,lst3])
print(arr)
# Here we convert out 3 list into multi dimensional(2D) array using numpy
# here we see [[]] in your array two square brackets means it is 2D array
# If we see array's shape
print(arr.shape)
# we get shape of (3,5); which shows that 3*5=15 elements in array i.e. 3 rows and 5 columns elements
# we can do reshape this array having 15 total elements; i.e. (1,15),(5,3),(15,1) order, means you can't reshape below or above the total elements.
print(arr.reshape(5,3))
# What if we reshape(5,4), Can we do it?

## Indexing
#-> Accessing the array element
#1D Array
arr = np.array([1,2,3,4,5,6,7])

print(arr[5])
#2D Array
lst1=[1,2,3,4,5]
lst2=[2,3,4,5,6]
lst3=[9,7,6,8,9]
arr=np.array([lst1,lst2,lst3])
print(arr)
print(arr[1][2])  # arr[row][column]
print(arr[1,2])   # arr[row_index,colum_index]
print(arr[0:2,0:2])  #arr[row_index_range,column_index_range]
# Q Find 3,4,5 from the array?
print("Result is: ")
print(arr[1:2,1:4])

# InBuilt Functions in NumPy
## Arrange: Create one dimension array between lower and higher value.
arr = np.arange(0,10)
print(arr)
arr = np.arange(0,10,step=2)  #step gap of 2
print(arr)
# Linspace: It will also create number of array between start and stop points.
# It will generate equally divide points between two points.
arr=np.linspace(1,10,50)  # total 50 number generate equally between 1 to 10
print(arr)

##copy() function and broadcasting
arr = np.array([1,2,3,4,5,6,7,8,9])
arr[3:]=100    # broadcasting
print(arr)

arr1=arr
arr1[3:]=500
print(arr1)

print(arr)  # Here we see if we perform update on arr1 it will get reflected and updated to arr too.
            # which means array is a reference type; in referenc type all element wil share same memory location.
            # but in case of value type; it will have different memory location,so this kknd of update will not happen on it

# So inorder to prevent (reference problem) this we have copy() function
arr1 = arr.copy()  # here copy will taking another memeory location for arr1 instead to use same as arr in above step.
print(arr)
arr1[3:]=1000
print(arr1)

## Some Conditions that is very useful in Exploratory Data Analysis
val = 2
print(arr<2)
print(arr*2)
print(arr/2)
## What if i want exact value instead of bool return if arr<300
print(arr[arr<300])

## Create array and reshape
print(np.arange(0,10).reshape(5,2))

arr1=np.arange(0,10).reshape(2,5)
arr2=np.arange(0,10).reshape(2,5)
print(arr1*arr2)

# inbuilt functions to create array
print(np.ones(4,dtype=float))
print(np.ones((2,5),dtype=int))
## random distribution
print(np.random.rand(3,3))
# standard normal distribution
print(np.random.randn(4,4))

print(np.random.randint(0,100,8))  # between 0 to 100 select 8 random int values

print(np.random.random_sample((1,15)))  # return random floats in the half-open interval[0.0,1.0]