import random

#Generate a random choice
print("Welcome to the Rock Paper Scissors Game!")
game_var = ["rock", "paper", "scissors"]


#Initialize the game
retry_game = False

while not retry_game:
    pc_var = random.choice(game_var)
    user_guess = input("Please enter one of the following (rock, paper, scissors):  ")


    if user_guess == pc_var:
        print(f"You have selected {user_guess} and they have selected {pc_var}")
        print(" >>> Draw")

    elif (
            (user_guess == "rock" and pc_var == "scissors") or
            (user_guess == "paper" and pc_var == "rock") or
            (user_guess == "scissors" and pc_var == "paper")
    ):
        print(f"You have selected {user_guess} and they have selected {pc_var}")
        print(" >>> Won")
    else:
        print("Lose")



