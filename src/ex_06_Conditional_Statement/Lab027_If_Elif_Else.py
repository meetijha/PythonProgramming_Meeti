age=int(input("What is your age? "))

if age<13:
    print("Child")
elif 13 <= age < 18: # can aslo be written as(age>=13 and age<18)
    print("teenager")
else:
    print("adult")