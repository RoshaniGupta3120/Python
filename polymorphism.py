#Polymorphism---------------------------------------------------------- 
'''
class Animal:
    def sound(self):
        pass
class cat(Animal):
    def sound(self):   #---method overrindinng: redefing the function again
        print("meow")
class cow(Animal):
    def sound(self):
        print("moo")
ca=cat()
co=cow()
ca.sound()
co.sound()
'''
'''
from abc import ABC,abstractmethod

class Animal:
    @abstractmethod  #------------making sound() function a abstract method that means it is necessary to redefine it again in child class
    def sound(self):
        pass
class cat(Animal):
    def sound(self):   #---method overrindinng: redefing the function again
        print("meow")
class cow(Animal):
    def sound(self):
        print("moo")
ca=cat()
co=cow()
ca.sound()
co.sound()
'''
#Method Overloading-------------------------------------------------------------------------------
class math:
    def add(self,*args):
        print(sum(args))
    def add(self,a,b,c=0):
        print(a+b+c)
x=math()
x.add(4,3)
x.add(6,4,5,6,45,8)



























