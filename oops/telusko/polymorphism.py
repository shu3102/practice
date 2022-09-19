# polymorphism

#     poly        morphism
#       |             |
#       |             |
#       \/            \/
#     many           forms 
    
# polymorphism = many forms

# there are 4 ways of implementaing polymorphism
    # 1. Duck typing
    # 2. Operator Overloading
    # 3. Method Overloading
    # 4. Method Overriding
    

# 1. DUCK TYPING in PYTHON 

# Duck Typing is a type system used in dynamic languages. 
# For example, Python, Perl, Ruby, PHP, Javascript, etc. 

# where the type or the class of an object is less important than the method it defines. 

# Using Duck Typing, we do not check types at all. 
# Instead, we check for the presence of a given method or attribute.

# Ex 

class VSCODE:
    def execute(self):
        print("compiling code")
        print("running code")



class laptop:
    def code(self, ide):
        ide.execute()  

ide1 = VSCODE()

lap1 = laptop()
lap1.code(ide1)

# ata aplyla navin ide banvychi ahe tar parat ticha type same asavi asa class banvychi garaj nahi
# tyat fakt ti method asli pahije ji apn call karat ahe 
# baki class kontahi asel tar chalel
# yala duck typing mantat

# Ex.
class myvscode:
    def execute(self):
        print("Chekking spell")
        print("syntax check")
        print("compiling")
        print("compiling code")
        print("running code")
newvscode = myvscode()
lap1.code(newvscode)






print("operator overloading")
# 2. operator overloading in python

# Operator Overloading means giving extended meaning beyond their predefined operational meaning.
# For example operator + is used to add two integers
# as well as join two strings 
# and merge two lists. 
# It is achievable because ‘+’ operator is overloaded by int class and str class. 
# You might have noticed that the same built-in operator or 
# function shows different behavior for objects of different classes, 
# this is called Operator Overloading. 


# EX. 
# Python program to show use of
# + operator for different purposes.
  
print(1 + 2)
  
# concatenate two strings
print("Geeks"+"For") 
  
# Product two numbers
print(3 * 4)
  
# Repeat the String
print("Geeks"*4)

 
# Python Program illustrate how
# to overload an binary + operator

class Student:
	def __init__(self, mark):
		self.mark = mark

	# adding two objects
	def __add__(self, other):
		return self.mark + other.mark

ob1 = Student(1)
ob2 = Student(2)
ob3 = Student("Shubham")
ob4 = Student("Somwanshi")

# __add__(self, other) method n add karta 
# apn print(ob1+ob2) kele tar error yeto 

# pan __add__() add operator apn overload kelo 
# this is operator overloading/

print(ob1 + ob2)
print(ob3 + ob4)


#  Ex2. 

# Python program to overload equality
# and less than operators

class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if(self.a<other.a):
            return "ob1 is lessthan ob2"
        else:
            return "ob2 is less than ob1" 
    def __eq__(self, other):
        if(self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"
    def __gt__(self, other):
        if(self.a > other.a):
            return "ob1 is greaterthan ob2"
        else:
            return "ob2 is greater than ob1"
        
				
ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print(ob1 == ob2)



print("method overloading")
# METHOD OVERLOADING

# Like other languages (for example, method overloading in C++) do, 
# python does not support method overloading by default. 
# But there are different ways to achieve method overloading in Python. 

# python 'method overloading' support karat nahi

# nantar ji method define keli ahe tech ti new consider karte

# The problem with method overloading in Python is that we may overload the methods
# but can only use the latest defined method. 


# 1. 
# Method 1 (Not The Most Efficient Method):
# We can use the arguments to make the same function work differently 
# i.e. as per the arguments.

# Function to take multiple arguments
def add(datatype, *args):

	# if datatype is int
	# initialize answer as 0
	if datatype =='int':
		answer = 0
		
	# if datatype is str
	# initialize answer as ''
	if datatype =='str':
		answer =''

	# Traverse through the arguments
	for x in args:

		# This will do addition if the
		# arguments are int. Or concatenation
		# if the arguments are str
		answer = answer + x

	print(answer)

# Integer
add('int', 5, 6)
# String
add('str', 'Hi ', 'Geeks')


# Method 2 (Efficient One):
# By Using Multiple Dispatch Decorator 

from multipledispatch import dispatch

#passing one parameter
@dispatch(int,int)
def product(first,second):
	result = first*second
	print(result);

#passing two parameters
@dispatch(int,int,int)
def product(first,second,third):
	result = first * second * third
	print(result);

#you can also pass data type of any value as per requirement
@dispatch(float,float,float)
def product(first,second,third):
	result = first * second * third
	print(result);


#calling product method with 2 arguments
product(2,3,2) #this will give output of 12
product(2.2,3.4,2.3) # this will give output of 17.985999999999997



 # METHOD OVERWRITTING

# Method overriding is an ability of any object-oriented programming language
# that allows a subclass or child class to provide a specific implementation
# of a method that is already provided by one of its super-classes or parent classes. 
# When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) 
# as a method in its super-class, then the method in the subclass is said to override the method in the super-class.



         
# Python program to demonstrate
# method overriding


# Defining parent class
class Parent():
	# Constructor
	def __init__(self):
		self.value = "Inside Parent"
	# Parent's show method
	def show(self):
		print(self.value)
		
# Defining child class
class Child(Parent):
	# Constructor
	def __init__(self):
		self.value = "Inside Child"
	# Child's show method
	def show(self):
		print(self.value)
# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()



# Method overriding with multiple and multiple inheritance

# Python program to demonstrate
# overriding in multiple inheritance


# Defining parent class 1
class Parent1():
		
	# Parent's show method
	def show(self):
		print("Inside Parent1")
		
# Defining Parent class 2
class Parent2():
		
	# Parent's show method
	def display(self):
		print("Inside Parent2")
		

# Defining child class
class Child(Parent1, Parent2):
		
	# Child's show method
	def show(self):
		print("Inside Child")
	
		
# Driver's code
obj = Child()

obj.show()
obj.display()


# Multilevel Inheritance: When we have a child and grandchild relationship

# Python program to demonstrate
# overriding in multilevel inheritance


# Python program to demonstrate
# overriding in multilevel inheritance


class Parent():
		
	# Parent's show method
	def display(self):
		print("Inside Parent")
	
	
# Inherited or Sub class (Note Parent in bracket)
class Child(Parent):
		
	# Child's show method
	def show(self):
		print("Inside Child")
	
# Inherited or Sub class (Note Child in bracket)
class GrandChild(Child):
		
	# Child's show method
	def show(self):
		print("Inside GrandChild")		
	
# Driver code
g = GrandChild()
g.show()
g.display()




# Calling the Parent’s method within the overridden method
        # 1. using class name
        # 2. using super() method

# Python program to demonstrate
# calling the parent's class method
# inside the overridden method


class Parent():
	
	def show(self):
		print("Inside Parent")
		
class Child(Parent):
	
	def show(self):
		
		# Calling the parent's class
		# method
		Parent.show(self)
		print("Inside Child")
		
# Driver's code
obj = Child()
obj.show()


# using super()

# Python program to demonstrate
# calling the parent's class method
# inside the overridden method using
# super()


class Parent():
	
	def show(self):
		print("Inside Parent")
		
class Child(Parent):
	
	def show(self):
		
		# Calling the parent's class
		# method
		super().show()
		print("Inside Child")
		
# Driver's code
obj = Child()
obj.show()
