def print_digits_if_a_number(n):
    while n>0:
        print(n%10)
        n=int(n/10)

n=int(input("Enter n : "))
print_digits_if_a_number(n)
