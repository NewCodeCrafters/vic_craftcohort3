# This app thinks of a ramdom colour and prompt the user to guess what the colour is. It check to see if the user's guess matches the colour it thinks about as well as counts the number of guesses

import random as r

colour_list = ('red', 'green', 'blue', 'yellow', 'black', 'orange', 'white', 'grey', 'purple') # A list of colours the app chooses from.

# App chooses a ramdom colour
app_choice =r.choice(colour_list)

# Define the player guess counter
guesses = 0

# Prompt user to guess the colour
while True:
    print("I am thinking of a colour my friend, Guess what it is!")
    user_guess = input() # This stores the user's guess

    if user_guess != app_choice:
        print("You guessed Wrong. Try again dude!")
        guesses = guesses + 1
        continue
    else:
        break

print(f"You guessed right. It took you {guesses} guesses")