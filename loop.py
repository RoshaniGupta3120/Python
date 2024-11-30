'''
num=int(input("Enter a number : "))
fact=1
sum=0
for i in range(1,num+1):
    fact*=i
    sum+=i
print(f" factorial of {num} is {fact}")
print(f" Sum of {num} is {sum}")
'''
'''
num=int(input("Enter a number : "))
i=0
fact=1
sum=0
while i<=num:
    i+=1
    fact*=i
    sum+=i
print(f" factorial of {num} is {fact}")
print(f" Sum of {num} till 1 is {sum}")
'''
'''
for i in range(1,5):
    for j in range(10,15):
        print(j, end=" ")
    print()
'''
'''
for i in range(1,5):
    for j in range(10,15):
        print(i, end=" ")
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print(i, end=" ")
    print()


for i in range(1,5):
    for j in range(10,i+10):
        print(j, end=" ")
    print()

for i in range(1,6):
    for j in range(i):
        print(12, end=' ')
    print()
'''
#09/11/2024
'''
n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
'''
'''
n=5
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num, end=' ')
        num+=1
    print()
'''
'''
for i in range(65,69):
    for j in range(65,i+1):
        print(chr(j), end=' ')
    print()

i=68
for i in range(4,0,-1):
    for j in range(65,65+i):
        print(chr(j), end=' ')
    print()
'''
#11/11/2024
i=1
while i<=5:
    print(i)
    i+=1
