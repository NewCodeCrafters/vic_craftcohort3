# This app askes you your name, age and tell you your age in 1 year's time 

# Step one - Greet the user and ask their name 
print("Welcome, Please! What is your name?")
username = input()

# Step two, Greet the user and ask their age
print(f"Hello! {username}, How old are you?")
userage = int(input())

# Step three, Tell the user their age next year
if userage < 18:
    print(f"Dear {username} You are minor. You will be {userage+1}, years old next year.")
elif userage <=30:
    print(f"Dear {username} You are young adult. You will be {userage+1} year's old next year.")
elif userage <=45:
    print(f"Dear {username} You are a middle-aged. You will be {userage+1}, year's old next year!.")
elif userage <=75:
    print(f"Dear {username} You are getting old hehe. You will be {userage+1} year's old next year")
else:
    print(f"Dear {username}, You are getting old sorry hehe. You will be {userage+1} year's old next year")