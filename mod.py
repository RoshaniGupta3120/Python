'''
import module
print(module.add(3,4))
print(module.sub(3,4))
print(module.mul(3,4))
print(module.div(3,4))
print(module.fact(5))
'''
'''
from module import *  #importing every thing from that module
print(add(3,4))       # no need to mention module name for every function
print(sub(3,4))
print(mul(3,4))
print(div(3,4))
print(fact(5))
'''
#-------inbuilt module----------

from math import *  
print(factorial(6))

import random
print(random.randint(1,11))
