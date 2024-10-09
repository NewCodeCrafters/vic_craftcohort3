# This app allows you to create a username, password and askes you to login with it

# create username and password 
print('Hello user, create your user name')
username = input()
print("Awesome! now enter a password")
password = input()

# Login with the username and password created
print("....................................................................")
print("You have successfully signed up. Please log in with your credentials")
print("....................................................................")
userlogin = input ("Enter user name here: ")
# if userlogin == username:
#    print("Nice one")
#    userpassword = input("Enter Password: ")
#    if userpassword == password:
#       print("Access Granted")
#    else:
#       print("Wrong Password! Try again")
# else:
#    # print("Wrong Password.. Try again")

while userlogin != username:
    print("Wrong username, Please try again!")
    userlogin=input()
userpassword = input("Please enter your password: ")
while userpassword != password:
    print("Oops! Wrong Password, Please try again")
    userpassword = input()
print(f"Nice work, {username}. Access Granted!")