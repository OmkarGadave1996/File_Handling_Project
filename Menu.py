from Admin_Menu import *
from User_Menu import *
from User import User
import os
print("\t\t1.Admin")
print("\t\t2.User")
choice = int(input("Enter your choice :"))
if(choice == 1):
    for i in range(1,4) :
            Enter_Admin_id = input("Enter login id : ")
            Enter_Password = input("Enter password : ")
            if(Enter_Admin_id == "Admin" and Enter_Password == 'Admin@123'):
                for i in range(1,4) :
                    import random
                    captcha = random.randint(1000,9999)
                    print(captcha)
                    captcha_input = int(input("Enter vaild captcha"))
                    if(captcha == captcha_input) :
                        print("Admin Menu: ")
                        os.system("python Admin_Menu.py")  
                        break              
                    else :
                        print("Invalid credential")
            else :
                print("Invalid credential")
elif(choice==2):
    print("\t\t1.Existing User")
    print("\t\t2.New User")
    Input = int(input("Enter your choice :"))

    if(Input == 1):
        Enter_Admin_id = input("Enter login id : ")
        Enter_Password = input("Enter password : ")
        with open("User.txt","r") as fp:
            users = fp.readlines()
            for user in users:
                if (Enter_Admin_id and Enter_Password) in user:
                    import random
                    captcha = random.randint(1000,9999)
                    print(captcha)
                    captcha_input = int(input("Enter vaild captcha: "))
                    if(captcha == captcha_input) :
                        print("User Menu: ")
                        os.system("python User_Menu.py") 
                    else :
                        print("Invalid credential")
            else :
                print("User not Present")
                                        
    elif(Input == 2):
        Enter_Admin_id = input("Enter login id : ")
        Enter_Password = input("Enter password : ")
        U = User(Enter_Admin_id,Enter_Password)
        with open("User.txt","a") as fp:
            fp.write(str(U))
else:
    print("Invalid Login!")