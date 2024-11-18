import random

#Generate a random number
number_guess = random.randint(1,10)

print("Welcome to the Number Guessing Game!")

#Initialize the guessing game to keep track if guessed correctly
guess = False
attempt = 0

#Start the guessing game
while not guess:
    if attempt >= 5:
        print("You have used up all your attempts today!")
        break
    else:
        user_guess = int(input("What is your number: "))
        if user_guess == number_guess:
            attempt = attempt + 1
            print("You have guessed correctly!")
            guess = True
            print(f"Your number of attempts: {attempt}")
        elif user_guess > number_guess:
            attempt = attempt + 1
            print("You have guessed to HIGH! Try again")
        elif user_guess < number_guess:
            attempt = attempt + 1
            print("You have guessed to LOW! Try again")

