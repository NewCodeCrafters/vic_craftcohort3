import random as r 
def get_user_choice():
    while True:
        userchoice = input("Rock, Paper, Scissors " ). capitalize()
        if userchoice in ["Rock", "Paper", "Scissors" ]:
            return userchoice
        continue

def get_app_choice():
    appchoice = ["Rock", "Paper", "Scissors" ]
    return r.choice(appchoice)

def determine_winner(userchoice, appchoice):
    print(f"You chose {userchoice} and I chose {appchoice}")

    if userchoice == appchoice:
        return "It's a draw"
    elif(
        userchoice == "Rock" and appchoice == "Scissors" or 
        userchoice == "Paper" and appchoice == "Rock" or
        userchoice == "Scissors" and appchoice == "Paper"
    ):
        return "You won"
    else:
        return "App won!"
    
def playgame():
    playername = input("Enter Player name: ")
    print(f"Welcome, {playername} Let's Play Now!")

    while True:
        rounds = int(input("How many games would you like to play? "))
        if (rounds >=2 and rounds <=10):
            for round in range(rounds):
                userchoice = get_user_choice()
                appchoice = get_app_choice()
                result = determine_winner(userchoice, appchoice)
                print(result)
        else:
            print(f"Enter a number between 2-10")
            continue
        playagain = input("Would you like to play again? ")
        if playagain == 'yes'.lower():
            continue
        else:
            break
    print(f"Bye {playername}. Thanks for playing.......")

playgame()