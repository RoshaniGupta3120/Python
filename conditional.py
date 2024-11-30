'''
age=int(input("Enter your age :"))
if age>=18:
    print("Adult")
elif age>=13 and age<=17:
    print("Teenager")
else:
    print("Child")


total_share=int(input("enter total number of shares: "))
purchsed_price=int(input("enter purchsed price of shares: "))
current_price=int(input("enter current price of shares: "))
diff=current_price-purchsed_price
if diff>=400:
    shr=70/100*total_share
    print("70% of share: ", shr)
elif diff>=200 and diff<=399:
    shr=50/100*total_share
    print("50% of share: ", shr)
else:
    shr=20/100*total_share
    print("20% of share: ", shr)
'''
'''
fruits = ["apple", "banana", "mango"]
cust_fruit=input("Which fruit do you want to purchase : ")
if cust_fruit in fruits:
    print(cust_fruit, " is available")
else:
    print(cust_fruit, " is  not available")
'''
'''
for i in range(2,41,2):
    print(i)

for i in range(1,21):
    print(f"2 X {i} = {2*i}")
'''
for i in range(40,1,-2):
    print(i)
