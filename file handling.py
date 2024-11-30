#read mode---------------------------------------------------
'''
f=open("demo.txt","r") #r stands for read
print(f.tell())  # ----------printing the position of cursor
print(f.read())  #----------reading the file
print(f.tell())
print(f.read())
f.seek(4)  # -----------------changing the position of cursor
print(f.read())
f.seek(0)
print(f.readlines())  #------------convert the different lines into different elements of lists
'''
'''
f=open("demo.txt")
#print(f.readline())   #------return a single line
txt=f.readline()
while txt:
    print(txt)
    txt=f.readline()
'''
#Write mode------------------------------------------------------------------------
'''
#f=open("demo.txt","w")   #write mode----------over-writes the text
f=open("new_file.txt","w") # will create a new file
f.write("Hello, good Morning!!!!")
f.close() # in write mode it is neccessary to close the file after writing the text
'''

#Append mode------------------------------------------------------------------------
'''
f=open("new_file.txt","a") #append the text after existing text
f.write("Greetings from Roshani, Have a great dayyyy!!!")
f.close()
'''
#X mode----create a new file------------------------------------------------------------
'''
f=open("create.txt","x")
f.write("Hello, Good Morning!!!!")
f.close()
'''
#r+------ is for read and append
#w+----------write and read
#a+------append nd read
'''
with open("demo.txt","r+") as f:
    print(f.read())
    f.write("with clause demoooooo")
    f.seek(0)
    print(f.read())
'''
#text mode-by default mode--------------------------
'''
age=79
with open("demo.text","wt+") as f:  #text mode only takes string type of integer
    f.write(str(age))
'''


# to deal this we use serialization/deserialization using pickle module---------------

import pickle as p
a={1:"Apple",2:"Banana"}
with open("demo.txt","wb+") as f:   #b stands for binary mode-------------
    d=p.dumps(a)     # #serialization------convert a into binary code of a
    f.write(d)
    print(d)
    print(type(d))
    f.seek(0)
    data=p.loads(f.read())    # #deserialization------binary to normal datatype i.e., dictionary
    print(data)
    print(type(data))








































