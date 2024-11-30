
def grade(a):
    if a>=75 and a<=100:
        return "Grade A"
    elif a>=60 and a<=74:
        return "Grade B"
    elif a>=35 and a<=59:
        return "Grade C"
    else:
        return "Fail"

gr=int(input("enter your marks out of 100 : "))
print(grade(gr))
