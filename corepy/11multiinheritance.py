# Multiple Inheritance
class A:
    def method1(self):
        print("A class method is called")

class B(A):
    def method1(self):
        print("B class method is called")

class C(A):
    def method1(self):
        print("C class method is called")

# Multiple Inheritance: One class is inherting from two or more base class
class D(B,C):
    def method1(self):
        print("D class method is called")

d=D()
d.method1()

# Can we call method1 of C , B  and A class from D, since here method name is same
# To do this: you have to use <class_name>.<method>(<object of child class>)
B.method1(d)
A.method1(d)


# alternate way to do same thing
class A:
    def method1(self):
        print("A class method is called")

class B(A):
    def method1(self):
        print("B class method is called")

class C(A):
    def method1(self):
        print("C class method is called")

# Multiple Inheritance: One class is inherting from two or more base class
class D(B,C):
    def method1(self):
        print("D class method is called")
        C.method1(self)
        B.method1(self)
        A.method1(self)

d = D()
d.method1()