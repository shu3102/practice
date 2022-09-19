# abstraction


# By defining an abstract base class, 
# you can define a common Application Program 
# Interface(API) for a set of subclasses. 
# This capability is especially useful in situations 
# where a third-party is going to provide implementations, 
# such as with plugins, 
# but can also help you when working in a large team or 
# with a large code-base where keeping all classes in 
# your mind is difficult or not possible. 



# By default, 
#   Python does not provide abstract classes. 
# Python comes with a module that provides the base for defining Abstract Base classes(ABC) 
# and that module name is ABC. 
# ABC works by decorating methods of the base class as abstract 
# and then registering concrete classes as implementations of the abstract base. 
# A method becomes abstract when decorated with the keyword @abstractmethod. For Example –
#  


# Python program showing
# abstract base class work

from abc import ABC, abstractmethod

class Polygon(ABC):

	@abstractmethod
	def noofsides(self):
		pass

class Triangle(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 3 sides")

class Pentagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 5 sides")

class Hexagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 6 sides")

class Quadrilateral(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 4 sides")

# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

# I have 3 sides
# I have 4 sides
# I have 5 sides
# I have 6 sides







# Concrete Methods in Abstract Base Classes : 
# Concrete classes contain only concrete (normal)methods
# whereas abstract classes may contain 
#       both concrete methods and 
#       abstract methods. 
# The concrete class provides an implementation of abstract methods, 
# the abstract base class can also provide 
# an implementation by invoking the methods via super(). 

# Python program invoking a
# method using super()



class R(ABC):
	def rk(self):
		print("Abstract Base Class")

class K(R):
	def rk(self):
		super().rk()
		print("subclass ")

# Driver code
r = K()
r.rk()

# output
# Abstract Base Class
# subclass 



# Abstract Properties : 
# Abstract classes include attributes in addition to methods, 
# you can require the attributes in concrete classes by defining them with 
#       @abstractproperty. 
 
# Python program showing
# abstract properties

import abc
from abc import ABC, abstractmethod

class parent(ABC):
	@abc.abstractproperty
	def geeks(self):
		return "parent class"
class child(parent):
    @property
    def geeks(self):
        # print(super().geeks())
        return "child class"


try:
	r =parent()
	print( r.geeks)
except Exception as err:
	print (err)

r = child()
print (r.geeks)

# output
# Can't instantiate abstract class parent with abstract methods geeks
# child class





# Abstract Class Instantiation : 
# Abstract classes are incomplete 
# because they have methods that have nobody. 
# If python allows creating an object for abstract classes then using that object 
# if anyone calls the abstract method, 
# but there is no actual implementation to invoke. 
# So we use an abstract class as a template and according to the need, 
# we extend it and build on it before we can use it. 
# Due to the fact, an abstract class is not a concrete class, 
# it cannot be instantiated. 
# When we create an object for the abstract class it raises an error.

# Python program showing
# abstract class cannot
# be an instantiation
from abc import ABC,abstractmethod

class Animal(ABC):
	@abstractmethod
	def move(self):
		pass
class Human(Animal):
	def move(self):
		print("I can walk and run")

class Snake(Animal):
	def move(self):
		print("I can crawl")

class Dog(Animal):
	def move(self):
		print("I can bark")

class Lion(Animal):
	def move(self):
		print("I can roar")

try:
    c=Animal()
except Exception as err:
    print("cant create class")
    print(err)


 
#  output
#  cant create class
# Can't instantiate abstract class Animal with abstract methods move

