### Filter Function

def even(num):
    if num%2==0:
        return True

# this function will check one number at a time
# what if we want to check for the list of numbers to find even number among them
# so to do this we can use filter function

# syntax: filter(function,iterable_parameter)

lst = [1,2,5,6,8,10,23,25,30,0]
print(list(filter(even,lst)))

print(list(filter(lambda num:num%2==0,lst)))   #lambda function along with filter, combo pack


print(list(map(lambda num:num%2==0,lst)))    # here we can get difference between map and filter is that
                                            # filter will return only the true value
                                            # while map will return all true and false



## Reduuce