# CLASS  = blueprints or the prototype from which the objects are being created



# Classes are created by keyword class.
# Attributes are the variables that belong to a class.
# Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute


# Python3 program to demonstrate defining
# a class

class Dog:
	pass


# OBJECTS  =  instances of classes
 
# The object is an entity that has a state and behavior associated with it

# State: It is represented by the attributes of an object. It also reflects the properties of an object.
# Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
# Identity: It gives a unique name to an object and enables one object to interact with other objects.


obj = Dog()

# The self  

# Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it
# If we have a method that takes no arguments, then we still have to have one argument.
# This is similar to this pointer in C++ and this reference in Java.


#  When we call a method of this object as myobject.method(arg1, arg2), 
#  this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – 
# this is all the special self is about.






