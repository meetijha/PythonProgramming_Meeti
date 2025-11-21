import math

f=float(input("Enter the value of f : "))

wholeNum=int(f)
decimalNum=int ((f-wholeNum)*100)

print("Integer part : ",wholeNum)
print("fraction part : .",decimalNum) #gives little error due to rounding

#another way

num=input("Enter another number :")
integer,fraction=num.split('.')
print("Integer part : ",integer)
print("fraction part : .",fraction)
