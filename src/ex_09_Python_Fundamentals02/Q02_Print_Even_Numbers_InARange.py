def print_even_numbers(a,b):
   for i in range(a,b+1):
       if i%2==0:
           print(i)

a=int(input("Enter start range : "))
b=int(input("Enter end range : "))
print_even_numbers(a,b)


