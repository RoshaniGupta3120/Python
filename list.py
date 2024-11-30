'''
l=list(range(1,11))
m=[]
for i in l:
    m.append(i+10)     #.......m.insert(i-1,i+10)
print(m)
'''
'''
l=[12,19,20,200,45,34,40,65,79,1,5,3]
m=[]
for i in l:
    if i%2!=0:
        m.append(i)
print(m)
'''

#List comprehension---------------------
'''
l=[11,19,20,200,45,34,40,65,79,1,5,3]
#m=[i for i in l if(i%2==1)]
m=[i if i%2==1 else 0 for i in l]
print(m)

l=list(range(1,11))
m=[i**2 for i in l]
print(m)
'''

#list of list
'''
l=[[1,2,3,10],[4,5,6,11],[7,8,9,12],[13,14,15,16]]
print(l[1][0] #indexing
print(l[1:3][1:3])  #slicing
'''

#tuple-----------
'''
t=(1,2,3,4,5)
print(type(t))
print(t)
t1=tuple(range(1,11))
print(t1)
l=list(t)
print(l)
l.append(89)
t=tuple(l)
print(t)
'''
#set--------------------

s={1,2,3,4,5,5,5,5}
print(type(s))
print(s)
s1={}
print(type(s1))

s.add(50)
s.discard(1)  #won't give error if it don't fild the given value in
s.remove(1)
print(s)











