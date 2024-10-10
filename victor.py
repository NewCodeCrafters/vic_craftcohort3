# This app makes you know ones name, age, gender and date of birth and tells your age in 5 year's time

# Step one - Greet the user and ask their name
print("Welcome my friend, Please what is your name")
username = input()

# Step two - Greet the user by name and ask for their age 
print(f"Hello dear {username}, How old are you?")
userage = int(input())

# Step three - Greet the user by name and ask for their date of birth
print(f"Hello {username}, What is your date of birth?")

# Step four - Greet the user by name and tell them their age in next 5 year's time
if userage <18:
    print(f"Dear {username}, Sorry you are an underage, You will be {userage+5} years old in 5 year's time")
elif userage <=30:
    print(f"Hello {username}, You're a young adult. You will be {userage+5} years old in the next 5 years")
elif userage <=45:
    print(f"Hello dear {username}, You're a senior man hehe. You will be {userage+5} years old in 5 year's time.")
elif userage <=75:
    print(f"Hello Dear {username}, You're getting old not gonna lie hehe. You will be {userage+5} years old in 5 year's time")
else:
    print(f"Hello Dear {username} You are an old man/woman. You will be {userage+1} years old in next 5 years")

# Step five - Greet the user by name and ask their gender
print(f"Dear {username},What's your Gender? Male or Female or Gay or Les?")