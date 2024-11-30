'''
x=int(input("Enter a number : "))
y=int(input("Enter another number : "))
def add():
    print("Sum of given numbers is : ", x+y)
def sub():
    print("Substraction of given numbers is : ", x-y)
def multiply():
    print("Multiplication of given numbers is : ", x*y)

add()
sub()
multiply()
'''
'''
def input_n():
    a=int(input("Enter a number : "))
    b=int(input("Enter another number : "))
    return a,b
def add():
    x,y = input_n()
    print("Sum of given numbers is : ", x+y)
def sub():
    x,y = input_n()
    print("Substraction of given numbers is : ", x-y)
def multiply():
    x,y = input_n()
    print("Multiplication of given numbers is : ", x*y)

add()
sub()
multiply()
'''
'''
def input_n():
    a=int(input("Enter a number : "))
    b=int(input("Enter another number : "))
    return a,b
def add(x,y):  #parametrized funtion,,,, receiving parameter
    print("Sum of given numbers is : ", x+y)
m,n=input_n()
add(m,n)  #given paramters
'''
'''
l=[10,20,30,40,50]
def add(a):
    sum=0
    for i in a:
        sum+=i
    return sum
def pr(a):
    for i in a:
        print(i)
s=add(l)
print(s)
pr(l)
'''
#defalut arguments from right to left
'''
def f(x=0,y=0,z=0,p=0,q=0,r=0):
    print(x,y,z,p,q,r)

f(1,2)
'''

#variable length arguments-------------------
'''
def f(*args):
    print(*args)
f(1,2,3,"s",4,5)  # we can pass n number of arguments with "*args"
'''
#**kwargs-------------
'''
def f(**kwargs):
    print(kwargs)
    return kwargs
    
a=f(id=1,name="Rosh")
print(a)
'''
#------------------------------
'''
x=0
def f():
    global x  # updating the value in already made global value
    x=5
f()
print(x)
'''
'''
def f(a):
    return a**2
x=int(input("enter a number : "))
sq=f(x)
print(f"Square of given number is : {sq} ")
'''
#lambda function---------
'''
sq = lambda y:y**2
x=int(input("enter a number : "))
print(f"Square of given number is : {sq(x)} ")
'''
'''
a= lambda a,b,c,d,e:a+b+c+d+e
addition=a(1,3,7,9,4)
print(addition)
'''
#map()-----------------------
'''
l=list(range(1,11))
print(list(map(lambda i:i**2, l))) #iterate on list l
'''
#filter()
'''
l=list(range(1,11))
print(list(filter(lambda i:i%2==0, l))) #iterate on list l
'''
#zip()
'''
l=list(range(1,11))
a=list(range(11,19))
print(list(zip(l,a)))
print(tuple(zip(l,a)))
print(dict(zip(l,a)))
print(set(zip(l,a)))
'''











                                                                      














