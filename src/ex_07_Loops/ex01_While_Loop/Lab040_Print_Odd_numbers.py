i=1

while(i<=10):
    print(i) # Printing all odd num
    i+=2 # We avoided if statement here

# Another way
print("Another way")
i=1
while(i<=10):
    if(i%2==0):
        i += 1
        continue
    print(i)
    i+=1