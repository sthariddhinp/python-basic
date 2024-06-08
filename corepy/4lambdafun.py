### Lambda function
# anonymous function
# A function with no name
# work faster then normal function
# lambda function will only work when you have single expression of execution


def addition(a,b):
    return a+b 

print(addition(3,4))

##########################3
# syntax
# lambda_keyword input_variable_pass : operation or expression that want to perform
add = lambda a,b: a+b 

print(add(2,3))

evenvar=lambda a:a%2==0
print(evenvar(4))

addthree=lambda a,b,c:a+b+c 
print(addthree(1,2,3))