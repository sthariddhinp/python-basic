## Lists : 
    # A list is a datastructure in Python.
    # It is a mutable or changeable, ordered sequence of elements.
    # Each element or value that is inside of a list is called an item.
    # As Strings are defined as characters between quotes, Lists are defined by having values between square brackets [].

print(type([]))

lst_ex = []
print(type(lst_ex))

lst = list()
print(type(lst))

lst = ['Stat','Python',200,300,400,500]
print(type(lst))
print(len(lst))

## Inbuild function
# Append: append is used to add elements at end of the list
lst.append("Programming")
print(lst)
# Nested List
lst.append(["Kathamndu","Koteshwor"])
print(lst)
# Indexing in List
print(lst[4])
# index with range of value
print(lst[1:])
print(lst[1:6])
# Inser: insert in a specific order
lst.insert(2,"Banehwor")
print(lst)
# Extend: it is used to add element to the list,
    # it will add list element by seperate element not as nested list
lst = [1,2,3,4,5]
lst.extend([6,7])
print(lst)

# Various operation on list
lst = [1,2,3,4,5]
print(sum(lst))
#Pop() method: it wil remove last element of the list if index is not provided, else remove the indexed value form the list
print(lst.pop())
print(lst.pop(0))
#count(): calcualte total occurence of given element of list
lst = [1,2,1,4,5]
print(lst.count(1))
# index(): returns the index of firs occurence. Start and end index are not necessary parameters
print(lst.index(2,0,4))  # value,start_index,end_index

# Min and Max
print(min(lst))
print(max(lst))

# some inbuilt methods
print(lst*2)

## SETS: A set is an unordered colleciton of data type that is iterable, mutable and has no dublicate elements.
        # Python's set class represents the mathematical notation of a set.
        # This is based on a data structure known as a hash table.

# Define empty set
set_var = set()
print(set_var)
print(type(set_var))

set_var = {1,2,3,4,3,1}
print(set_var)          # It will not print repeated or dublicate element in set

set_var = {"Ironman","Hitman","Avengers"}
print(set_var)
print(type(set_var))

# Indexing
#set_var[0]
#set_var["Hitman"]    # Doen't support indexing in set

# Inbuilt function in sets
set_var.add("Kunfu Panda")

print(set_var)

set1 = {"Ironman","Hitman","Kunfu Panda"}
set2 = {"Ironman","Hitman","Kunfu Panda","Kunfu Panda 2"}
# Difference
print(set2.difference(set1))

print(set2)  # there is no update on set 2 after doing difference

# difference update
print(set2.difference_update(set1))
print(set2)  # this time we get the updated result on our set 2

# intersection
set1 = {"Ironman","Hitman","Kunfu Panda"}
set2 = {"Ironman","Hitman","Kunfu Panda","Kunfu Panda 2"}
print(set2.intersection_update(set1))
print(set2)


## Dictionaries: A dictionary is a colleciton which is unordered, 
#changeable and indexed. In python dictionaries are written with curly brackets, and they have keys and values.

dic = {}
print(type(dic))
# Create a dictionary
my_dict = {"Book1":"Python","Book2":"Java","Book3":"DWDM"}
print(type(my_dict))

print(my_dict["Book1"])   # Indexing in Dictionary by reteriving keys

# loop through keys
for x in my_dict:
    print(x)

# loop through values
for x in my_dict.values():
    print(x)

# loop through both key and values
for x in my_dict.items():
    print(x)

# Adding item in dictionaries
my_dict["Book4"]="JavaScript"
print(my_dict)
# If we append same key in dictonary then it will overridden the previous key with new one

# Nested dictonary
book1 = {'ABC':2002}
book2 = {'XYZ':2008}
book3 = {'MNO':2010}

book_type = {'book1':book1,'book2':book2,'book3':book3}
print(book_type)
print(book_type['book2'])  # retreive value with key book2
print(book_type['book2']['XYZ'])   # retreive the Year value only

## Tuples: 
        # It is not mutable.

#empty tuple
my_tuple = tuple()
print(type(my_tuple))
my_tuple = ()
print(type(my_tuple))
#
my_tuple = ("Riddhi","Prem","Ud")
print(my_tuple)
print(my_tuple[0])
#my_tuple[0] = "Rockey"   # doesnot support item assigment on tuple. The element can't replace. but we can replace/change whole tuple.
my_tuple = ("Hello","Learners")
print(my_tuple)
# inbuilt functions
print(my_tuple.count("Hello"))
print(my_tuple.index("Learners"))