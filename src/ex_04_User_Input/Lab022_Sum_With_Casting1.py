a=int(10.9) # Valid as conversion is float to int
b=int(input("Enter 2nd Number")) #10
#If we feed 10.9 here it gives error as String 10.9 cant be added to int
#invalid literal for int() with base 10: '10.9'

c=float(input("Enter 3rd Number")) #10.9
sum=a+b+c
print(sum)
#enter 10.9 here and its valid