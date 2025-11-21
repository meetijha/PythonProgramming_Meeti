i=1;
while(i<=10):
    if(i%3==0):
        i += 1
        continue
    print(i) # Printing non multiples of 3
    i+=1

print("Outside the loop now...")