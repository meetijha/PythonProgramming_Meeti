def PrimeNumber(n):
    for i in range(2,n):
        if n%i==0:
            return False

        return True

n=int(input("Enter number: "))
if PrimeNumber(n):
    print("Prime number")
else:
    print("Not Prime number")