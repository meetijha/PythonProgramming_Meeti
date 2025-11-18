# Explicit type conversion, developer does it
#we use functions like int() boolean() float() for type casting

a=10
b=5.5
sum=int(a+b) #int function is used here for casting
print(sum, type(sum))

sum1=2+3.0 #Type conversion
sum2=int(2+3.0)# Type casting
print(sum1, type(sum1))
print(sum2, type(sum2))