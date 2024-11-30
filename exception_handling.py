'''
a=10
b=0
print(a/b)  #ZeroDivisionError: division by zeros
'''
'''
try:
    l=[2,3,4,5]
    print(l[5])   #instead of giving an erroe to user it will execute except part of the code.
except:
    print("Index out of range")
'''

try:
    l=[2,3,4,5]
    print(l[1])

    a=10
    b=1
    print(a/b)

    s=int('8a')
    print(s)
    
except IndexError as e:
    print("Index out of range")
except ZeroDivisionError as e:
    print("can not divide by zero")
except Exception as e:          #Exception is the parent class for all kind of errors
    print("common error")
    print(e)  #prints the error
else:
    print("execute only if No error in code")
finally:
    print("executes even when the error is there in code")
