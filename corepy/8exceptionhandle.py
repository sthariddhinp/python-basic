## Exception Handling
# print(a)

#syntax
# try:
    ##code block where exception can occur
# except:
    # print("Some problem may have")

try:
    print(a)
except:
    print("Here variable is not defined before to operate.")    

try:
    a=b
    # a = 1
    # b = "Rk"
    # c = a + b
except NameError as ex1:
    print("User has not defined variable.") 
except Exception as ex:
    print(ex)

# try:
#     a=b
# except Exception as ex:
#     print(ex)
    
# a = 1
# b = "Rk"
# c = a + b

try:
    # a=b
    a = 1
    b = "Rk"
    c = a + b
except NameError:
    print("User has not defined variable.") 
except TypeError:
    print("Try to make similar data type.") 
except Exception as ex:
    print(ex)


### try else block ###

try:
    # a=b
    a = int(input("Enter the number 1"))
    b = int(input("Enter the number 2"))
    c = a + b
    d = a / b   ## divison by 0 exception
    e = a * b
    
except NameError:
    print("User has not defined variable.") 
except TypeError:
    print("Try to make similar data type.") 
except ZeroDivisionError:
    print("Please provide number greater then 0.")
except Exception as ex:
    print(ex)
else:
    print(c)
    print(d)
    print(e)

### try else finally ###
#=> In try else block, if you get some excetpion then your else block code will not exceuted if you have handle your exception.
try:
    # a=b
    a = int(input("Enter the number 1"))
    b = int(input("Enter the number 2"))
    c =  a / b   ## divison by 0 exception
except NameError:
    print("User has not defined variable.") 
except TypeError:
    print("Try to make similar data type.") 
except ZeroDivisionError:
    print("Please provide number greater then 0.")
except Exception as ex:
    print(ex)
else:
    print(c)
finally:
    print("The execution is done.")


### When to use else and finally
    
# Custom Exception
