
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
            
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

t = Triangle()
# t.inputSides()


# multiple in inheritance
# class child(parent1, parent2)





# constructor in inheritance

# super() --> super method ne parent class che sagle method accerss karu shkto 

# class A:
# class B(A) 
#   class B madhe constructor nasel tarch to class A cha constructor call karel
#   class B madhe tycha constructor asel tar to class A chya constructor la call nahi karnar

#Ex. 
class TempA:
    def __init__(self):
        print("constructor of A")
    def method1(self):
        print("calling method 1")
    def method2(self):
        print("calling method 2")
        
class TempB(TempA):
    def method3(self):
        print("calling method 1")
    def method4(self):
        print("calling method 2")
        
ob1 = TempB()
# output ---> constructor of A


# B madhe constructor asel tar B chech call hote 
# parent che call karnysathi 'super()' mthod vaprtat

#Ex. 
class TempAA:
    def __init__(self):
        print("constructor of A")
    def method1(self):
        print("calling method 1")
    def method2(self):
        print("calling method 2")
        
class TempBB(TempAA):
    def __init__(self):
        print("init/constructor of of B")
    def method3(self):
        print("calling method 1")
    def method4(self):
        print("calling method 2")
        
ob1 = TempBB()
# init/constructor of of B




# constructor in multiple inheritance
class A:
    def __init__(self) -> None:
        print("Constructor of A")
    def method1(self):
        print("method 1 in A")

class B:
    def __init__(self) -> None:
        print("Constructor of B")
    def method1(self):
        print("method 1 in B")

class C(A, B):
    def __init__(self) -> None:
        print("calling construcor of c")
    # pass


ob1 = C()
# calling construcor of c

# c madhe init method nasel tar to constructor chya order pramane construco call karto
# Ex Class C madhe __init__ nasel tar to A chya constructor la call karel
# A madhe nasel tar mag B la jail

# ani same for methods 
# yala apn 'METHOD RESOLUTION ORDER' manto 
# LEFT -> RIGHT




