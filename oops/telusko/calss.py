
# Lec 3

    # making class using 'class' keyword
class Computernew:
    def __init__(self) -> None:
        self.age = 20
    def compare(self, other):
        if(self.age == other.age):
            print("They are same")
            return True
        print("they are diff")
        return False

#lec 3
comp1 = Computernew()
print(id(comp1)) # address find karte
#140706896569536

comp2 = Computernew()
print(id(comp2)) # address find karte
#139747271055200

comp1.compare(comp2)





class Computer: 
    #lec 1
    def config(self):
        print("config is 16Gb, i5")

# lec 1
comp1 = Computer()

print(type(comp1)) 
# <class '__main__.Computer'>

# how to access methods and attributes
Computer.config(comp1)
# i5, 16gb, 1TB

#OR
comp1.config()
#i5, 16gb, 1TB

#SELF self reffers to an object which we are passing




# Lect 2
class Computer123:
    # lec 2
    def __init__(self, cpu, ram) -> None:
        self.cpu = cpu
        self.ram = ram
    #lec 1
    def config(self):
        print("config is ", self.ram, self.cpu)

comp1 = Computer123("i5", 16)

comp1.config()
    # config is  16 i5
    

    
# there are two types of variable in CLASS   
# 1. instance variable 
#     - seperate for each OBJECT
#     - 

# 2. class variable(global variable)
#     - only one variable of class
#     - all the objets shares the same variable

    
from unicodedata import name


class car1:
    # this is global variable
    # class variable
    tyre = 4
    
    def __init__(self) -> None:
        # objects variables
        self.color = "Blue"
        self.model = "m14"
c1 = car1()
print(c1.color, c1.tyre)
# Blue 4

# we can change class variable only by class name
car1.tyre = 5
print(c1.color, c1.tyre)
# Blue 5





# TYPES OF METHODS

# 1. instance method 
#     objects sathi aste 
#     yat apan 'self(object)' keyword pathvto
    

# 2. class method 
#     class chya data la manupulate karnysathi vaprto
#     yat apn 'cls(class)' pathvto
#     '@classmethod' he decorator lavave lagte 

# 3. static method 
#     kahich arguments nahi pathvat 
#     hya method cha class and object shi kahi attributes access hot nastat
#     '@staticmethod' he decorator lavave lagte


class Methods:
    schoolname = "COEP"
    
    def __init__(self, name) -> None:
        self.name = name 
    
    # instances method 
    def getname(self):
        print(self.name)
        return self.name
    
    @classmethod
    def getclassmethod(cls):
        print(cls.schoolname)
        return cls.schoolname
    
    @staticmethod
    def randomstatic():
        print("static method")
        return 0
    
m1 = Methods("shu")
m1.getname()
Methods.getclassmethod()
Methods.randomstatic()




# INNER CLASS IN PYTHON
# class inside a class in python 

# A class defined in another class is known as an inner class or nested class. 
# If an object is created using child class means inner class then the object can also be used by parent class or root class. 
# A parent class can have one or more inner classes but generally inner classes are avoided.

# create a Student class
class Student:

    # constructor method
    def __init__(self, name):
        # object attributes
        self.name = name
        self.lap = self.Laptop()

    def show(self):
        print("Name:", self.name)
        self.lap.display()

    # create Laptop class
    class Laptop:
        def __init__(self):
            self.name = 'HP'
            self.code = '024avc'

        def display(self):
            print("Name:", self.name)
            print("Code:", self.code)

# create Student class object
outer = Student("shu")

# method calling
outer.show()

# create a Laptop
# inner class object
g = outer.lap

# inner class method calling
g.display()


