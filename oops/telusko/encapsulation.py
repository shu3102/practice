
# Encapsulation 


# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
# It describes the idea of wrapping data and the methods that work on data within one unit. 
# This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 
# To prevent accidental change, an object’s variable can only be changed by an object’s method. 
# Those types of variables are known as private variables.



# Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class 
# but can be accessed from within the class and its subclasses. 
# To accomplish this in Python, 
# just follow the convention by prefixing the name of the member by a single underscore “_”.

# single underscore ne protected hotat python madhe


# Python program to
# demonstrate protected members

# Creating a base class
class Base:
	def __init__(self):
		# Protected member
		self._a = 2

# Creating a derived class
class Derived(Base):
	def __init__(self):
		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling protected member of base class: ", self._a)

		# Modify the protected variable:
		self._a = 3
		print("Calling modified protected member outside class: ", self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2=base: ", obj2._a)


