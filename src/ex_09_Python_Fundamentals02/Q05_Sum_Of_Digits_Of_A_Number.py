def sum_of_digits(n):
 sum=0
 while n>0:
    sum=sum + n%10
    n=int (n/10)
 return sum

n=int(input("Enter number : "))
sum=sum_of_digits(n)
print("Sum of digits of number : ",sum)