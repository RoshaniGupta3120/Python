'''
a='Hello World'
print(a[4]) #Indexing
print(a[::2]) #slicing
print(a[::-2])
print(a[:5])
'''
'''
a=input("enter a word : ")
if a==a[::-1]:
    print("it is Palindrome")
else:
    print("it is not Palindrome")
'''
'''
a=" Hello World "
print(a.upper())
print(a.lower())
print(a.strip())
print(a)
print(a.startswith(" "))
'''

#List-----------

l=[1,2,3,4,5]
#print(type(l))
m=list()
#print(m)
l.insert(2,3)
print(l)
p=[7,6,8,9]
l.extend(p)
print(l)
m=l.pop()
print(l)
print(m)
l.remove(5)
print(l)
l.extend([4,6,9,9])
print(l)
print(l.count(9))
l.sort()
print(l)
l.reverse()
print(l)
l.clear()
print(l)
