# Data Abstraction 

# It hides the unnecessary code details from the user. 
# Also,  when we do not want to give out sensitive parts of our code implementation and 
# this is where data abstraction came.

# Data Abstraction in Python can be achieved through creating abstract classes.


class MyClass:

	# Hidden member of MyClass
	__hiddenVariable = 0
	
	# A member method that changes
	# __hiddenVariable
	def add(self, increment):
		self.__hiddenVariable += increment
		print (self.__hiddenVariable)

# Driver code
myObject = MyClass()	
myObject.add(2)
myObject.add(5)

# This line causes error
print (myObject.__hiddenVariable)

