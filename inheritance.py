#class -----consist of relevent attributes and methods
'''
class A:
    def p(self,n):
        print(f"hello, {n}")
obj=A()
obj.p("Roshani")
'''
'''
class A:
    def __init__(self,n):
        self.name=n
    def p(self):
        print(f" Hello {self.name}")
obj=A("Roshani")
obj.p()
'''
#Single inheritance
'''
class A:   #Parent class
    def p(self):
        print(f" Hello, Good morning!!")
class B(A):     #Child class
    pass
obj=B()
obj.p()
'''
#Multilevel inheritance
'''
class A:             #parent class of B
    def games(self):
        print("Games")
class B(A):             #parent class of C and child class of A
    def travel(self):
        print("travel")
class C(B):             #Child class of B
    def learn(self):
        print("learn")
print("A")
obj=A()     #---------------A can access the properties and methods of class A only
obj.games()

print("B")
obj=B()     #---------------B can access the properties and methods of class A & B
obj.games()
obj.travel()

print("C")
obj=C()     #---------------C can access the properties and methods of class A & B & C
obj.games()
obj.travel()
obj.learn()
'''
#Hierarchical inheritance
'''
class area:
    def ar(self):
        print('I am inside area class')

class rect(area):
    def r(self):
        area.ar(self)
        print('I am Rectangle')
class sqr(area):
    def s(self):
        area.ar(self)
        print('I am Square')
class circle(area):
    def c(self):
        area.ar(self)
        print('I am Circle')

re=rect()
re.r()
sq=sqr()
sq.s()
cir=circle()
cir.c()
'''
#Multiple inheritance
'''
class father:
    def f(self):
        print("Father")
    def display(self):
        print("hello f")
class mother:
    def m(self):
        print("Mother")
    def display(self):
        print("hello m")
class child(mother,father):
    def c(self):
        print("child")
    def display(self):
        #super().display()   #----------calls the function of parent class which is mentioned first
        father.display(self)
        mother.display(self)
        print("hello c") 
obj=child()
obj.c()
obj.f()
obj.m()
obj.display()
'''
#Data Abstraction--------------------------------------------------------------------------------------------------------------------------------
'''
is hiding complex details and showing only neccesary features eith the help of abstract classes and interfaces..
the ABC modelu i.e, abstract based class is used for defining such classes
the Abstracyt based class is a class that cantnot be instantiated and typically include one or more abstract methods
that must be implemented in sub classes
'''
'''
from abc import ABC,abstractmethod #-------inbulit class

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,r):
        self.radius=r
    def area(self):
        return 3.14*self.radius*self.radius
c=circle(3)
print(c.area())
'''













































        









