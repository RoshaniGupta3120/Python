#recursion----------a function caliing itself is known as recursion
'''
def f(n):
    if (n==0) or (n==1):
        return 1
    else:
        return n*f(n-1)    
print(f(6))
'''
def p(x,n):
    if n==0:
        return 1
    else:
        return x*p(x,n-1)

print(p(2,3))
 
