username=input("Enter your username: ")
password=input("Enter your password: ")

if username=="admin" and password=="pass" :
    print("Welcome Admin")
else: # Below is nested if else statement
    if(username!="admin"):
        print("Wrong username")
    else: print("Wrong password")