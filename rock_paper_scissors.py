# This app plays "Rock, Paper, Scissors game with the user"

# Initiate Computer's choice
import random
choice_list =('Rock', 'Paper','Scissors')
app_choice = random.choice(choice_list) # App chooses from the list


# Initiate User's Choice
user_choice = input("Welcome to the game. Rock Paper or Scissors?: "). capitalize()



# Entry validation 
while user_choice not in ('Rock', 'Paper', 'Scissors'):
    user_choice = input("Invalid Entry. Enter Rock, Paper or Scissors: "). capitalize()

# Compare user entry and app choice and determine winner.

if user_choice == app_choice:
    print(f"It's a draw hehe! We both chose {app_choice}!")
elif(
    user_choice == "Rock" and app_choice == "Scissors" or 
    user_choice == "Scissors" and app_choice == "Paper" or
    user_choice == "Paper" and app_choice == "Rock"
):
    print(f"You won! You chosen {user_choice} and I chose {app_choice}. ")
else:
    print(f"I won! You chose {user_choice} and I chose {app_choice}.")