# range() - sequence generator
# range(5) --> 0 to 4
# range has 3 parameters (start, stop, step)

# default value of start is 0 and step is 1

# so range(5) means --> 0,1,2,3,4
# range(1,6) --> 1,2,3,4,5
#range(1,10,2) --> 1,3,5,7,9

for i in range(5):
    print(i) #0,1,2,3,4

print()

for i in range(1,6):
    print(i)#1,2,3,4,5

print()
for i in range(2,11,2):
    print(i) #2,4,6,8,10