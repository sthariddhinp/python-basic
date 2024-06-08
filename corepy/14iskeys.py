#=>  #,copy(),deepcopy()


# equal to : '='
lst1 = [1,2,3,4]
lst2 = lst1
lst2[1]=1000

print(lst2)

print(lst1)   # even i check lst1, here it's index 1 also update with 1000 while updating it on lst2
         # it is due to both the variable have referenceing to same memeory location.

## copy() ##
#SHallow Copy
lst1 = [1,2,3,4]
lst2=lst1.copy()     # shallow copy, it will copy to different memory location not to same memroy location.
print(lst2)
lst2[1] = 5000
print(lst2)
print(lst1)

#SHallow Copy with nested list
lst1 = [[1,2,3,4],[5,6,7,8]]
lst2=lst1.copy()  
print(lst1)   
print(lst2)
lst2[1][0] = 100
print(lst2)
print(lst1)
## 
lst1.append([2,3,4,5])
print(lst1)
print(lst2)
# Here we can see that our new list added with append is added to lst1.
# since we have use our shallow copy to make lst2
# but we can't see that value is appended to lst2
# This new  item will not get copied into lst2 but  if we change the object of the  item then it will get changed.

## Deep Copy
import copy
lst1 = [1,2,3,4]
lst2 = copy.deepcopy(lst1)

lst2[1]=500
print(lst1)
print(lst2)
## In a normal list shallow copy = deepp copy

## In nested list:
lst1 = [[1,2,3,4[3,4,5],[5,6,7]]
lst2 = copy.deepcopy(lst1)
lst2[1][0] = 100
print(lst2)
print(lst1)
# every things is on sepearte memroy location
# In a nested list shallow copy != deep copy

