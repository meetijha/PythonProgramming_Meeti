username=input("Enter username : ")
password=input("Enter password : ")

if(username=="admin" and password=="pass"):
    print("Login Successful!")
elif(username!="admin"):
    print("Wrong username!")
else:
    print("Wrong password!")
