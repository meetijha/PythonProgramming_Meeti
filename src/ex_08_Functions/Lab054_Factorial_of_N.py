
def factorial_while(n):
 fact  =1;
 while(n>0):
    fact=fact*n;
    n-=1
 return fact

def factorial_for(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

n = int(input("Enter n : "))
print("Factorial =",factorial_while(n))
print("Factorial =",factorial_for(n))