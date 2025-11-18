'''
Type conversion allowed among compatible data type
int to float
float to int
int to bool

Type conversion is implicit type of conversion
'''

a=10
b=5
print(a/b, type(a/b))
# implicitly int is converted to float

sum=5 +10.0 #int 5 is converted to float
print(sum, type(sum))
