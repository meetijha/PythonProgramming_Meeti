# starts with lambda keyword
# variable and then expression
sum1= lambda a,b,c:a+b+c
print(sum1(4,5,6))

# lambda is used to do simple tasks
#like in above Sum1 can be used like a function

avg=lambda a,b:(a+b)/2
print(avg(4,5))

# lambda functions are used for high order functions
'''
In high order function either parameter is a lambda function
or return type is a lambda function
eg:

def fun()
.....
....

here in fun() lambda function can be a parameter 
or return type can be a lambda function
'''