class human:
    #def attribute(a):
        #a.name=input("Enter your name : ")
        #a.age=int(input("Enter your age : "))
    def __init__(self):        #--------Constructor------- 
        print("Human object is created")
        self.name=input("Enter your name : ")
        self.age=int(input("Enter your age : "))
    #def greetings(g):
        #print(f"Hello {g.name} .")
    def __str__(self):        #----------converts objects into strings----
        return f"Hello {self.name}, your age is {self.age} ."
    def dance(self):
        print("show your fav step and dance")
    def draw(s):
        print("show your drawings")
    def __del__(self):        #------destructor-------
        print(f"{self.name} is deleted")

rosh=human()   #object created
print(id(rosh))
#rosh.attribute()
#rosh.greetings()
print(rosh)
rosh.dance()
rosh.draw()
del rosh
rosh.dance()  #---error (rosh is not defined) as the object is deleted----
