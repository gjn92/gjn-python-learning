# Python Self-Learning Journey

This repository showcases my journey of learning Python, starting from simple beginner projects like printing 'Hello World' to more complex projects. Each project represents a step forward in my understanding of Python programming concepts and my progress in becoming a proficient Python developer.

## Table of Contents
- [Introduction](#introduction)
- [Projects](#projects)
  - [Project 1: Hello World](#project-1-hello-world)
  - [Project 2: Basic Calculator](#project-2-basic-calculator)
  - [Project 3: Mad Libs Game](#project-3-mad-libs-game)
  - [Project 4: Number Guessing Game](#project-4-number-guessing-game)
  - [Project 5: Rock Paper Scissors Game](#project-5-rock-paper-scissors-game)
  - [Project 6: To-Do List Application](#project-6-to-do-list-application)
    - [Project 7: Simple Unit Converter](#project-7-simple-unit-converter)
  - [More Projects](#more-projects)
- [Contributing](#contributing)
- [License](#license)

## Introduction

I began my Python learning journey with the goal of building a strong foundation in programming. This repository is a collection of my projects that document my growth, starting with the basics and gradually moving to more advanced topics. It serves as a portfolio of my work and a testament to the skills I've gained through self-study.

## Projects

### Project 1: Hello World

This is my very first Python project, where I learned how to print text to the console. It may be simple, but it's a fundamental step in any programmer's journey.

#### Usage

To run the project, simply execute the following command in your terminal:

```sh
python hello_world.py
```

This will print:

```
Hello World
```

#### Features

- Prints 'Hello World' to the console.
- Serves as an introduction to Python syntax.

### Project 2: Basic Calculator

This project is a simple calculator that takes user input and performs basic arithmetic operations such as addition, subtraction, multiplication, and division.

#### Code

```python
# get numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# convert to strings to numbers
num1 = float(num1)
num2 = float(num2)

# ask for the operation
operation = input("Enter the operations (+, -, *, /): ")

# perform calculations
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid Operation"

print(result)
```

#### Usage

To run the project, execute the following command in your terminal:

```sh
python basic_calculator.py
```

Follow the prompts to enter numbers and select the desired operation.

#### Features

- Performs addition, subtraction, multiplication, and division.
- Demonstrates the use of user input and basic arithmetic operations.

### Project 3: Mad Libs Game

This project is an interactive Mad Libs game where the user provides words to fill in the blanks and create a fun story.

#### Code

```python
# welcoming to the game
print("Welcome to the Mad Libs Generator Game!")
print("Let's get started")

# get inputs for the game
place = input("Give me a place: ")
adj = input("Now give me an adjective: ")
noun = input("Lastly, give me a noun: ")

# generate the final output
print("Thank you for your input! Let's see the final output.")

output = f"Today I went to the {place}. It was very {adj} and I saw a {noun}."

print(output)
```

#### Usage

To run the project, execute the following command in your terminal:

```sh
python mad_libs.py
```

Follow the prompts to enter words, and enjoy the resulting story.

#### Features

- Interactive game that takes user input to create a story.
- Demonstrates string concatenation and user input handling.

### Project 4: Number Guessing Game

This project is a number guessing game where the user tries to guess a randomly generated number between 1 and 10.

#### Code

```python
import random

# Generate a random number
number_guess = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")

# Initialize the guessing game to keep track if guessed correctly
guess = False
attempt = 0

# Start the guessing game
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
            print("You have guessed too HIGH! Try again")
        elif user_guess < number_guess:
            attempt = attempt + 1
            print("You have guessed too LOW! Try again")
```

#### Usage

To run the project, execute the following command in your terminal:

```sh
python number_guessing_game.py
```

Follow the prompts to guess the number, and see if you can guess correctly within the given attempts.

#### Features

- Generates a random number between 1 and 10.
- User has up to 5 attempts to guess the correct number.
- Provides feedback on whether the guess is too high or too low.

### Project 5: Rock Paper Scissors Game

This project is a Rock Paper Scissors game where the user plays against the computer.

#### Code

```python
import random

# Generate a random choice
print("Welcome to the Rock Paper Scissors Game!")
game_var = ["rock", "paper", "scissors"]

# Initialize the game
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
```

#### Usage

To run the project, execute the following command in your terminal:

```sh
python rock_paper_scissors.py
```

Follow the prompts to play against the computer, and see if you can win!

#### Features

- User plays against the computer.
- Generates a random choice for the computer.
- Determines if the user wins, loses, or ties based on the rules of Rock Paper Scissors.

### Project 6: To-Do List Application

This project is a simple to-do list application that allows the user to add, view, and remove tasks from a list.

#### Code

```python
# list to store the task
tasks = []

# menu to add, view, remove and exit todolist

while True:
    menu = input("Type one of the following: 1. Add Task, 2. View Tasks, 3. Remove Tasks, 4. Exit: ")
    if menu == "4":
        print(f"You have exited from the program")
        break # This stops the loop

    elif menu == "3":
        print(tasks)
        td_rm = input("What task do you want to remove?: ")
        tasks.remove(td_rm)
        print(f"You have successfully removed {td_rm}")
        print(tasks)

    elif menu == "2":
        print(tasks)

    elif menu == "1":
        add_td = input("What task do you want to add to the list: ")
        tasks.append(add_td)
        print(f"You have added {add_td} to the list")
        print(tasks)

    else:
        print("Invalid option, please try again!")
```

#### Usage

To run the project, execute the following command in your terminal:

```sh
python todo_list.py
```

Follow the prompts to add, view, or remove tasks from your to-do list.

#### Features

- Allows the user to add tasks to the to-do list.
- View the current tasks.
- Remove tasks from the list.
- Simple menu-driven interface.

### Project 7: Simple Unit Converter

This project is a simple unit converter that can convert weight, temperature, and length between different units.

#### Code

```python
# Welcome Page
print("Welcome to the Simple Unit Converter!")

print("We can help you convert your units.")

# functions for weight converter
def convert_weight(value, unit):
    if unit.lower() == "lb":
        return round(value * 0.453592, 2), "kg"
    elif unit.lower() == "kg":
        return round(value / 0.453592, 2), "lb"

def convert_temp(value, unit):
    if unit.lower() == "c":
        return round((value * 9/5) + 32, 2), "F"
    elif unit.lower() == "f":
        return round((value - 32) * 5/9, 2), "C"

def convert_length(value, unit):
    if unit.lower() == "miles":
        return round(value * 0.621371, 2), "KM"
    elif unit.lower() == "km":
        return round(value * 1.60934, 2), "MILES"

while True:
    unit = input("Enter your unit you wish to be converted (lb/kg) or (C/F) or (miles/km) or (q) to exit: ").upper()

    if unit.lower() == "q":
        print("You have ended the app! Goodbye")
        break
        # stops the loop

    value = float(input("Enter the value you wish to convert: "))

    if unit.lower() in ["lb", "kg"]:
        print("You have selected Weight.")
        result_weight, target_unit = convert_weight(value, unit)
        print(f"{value} {unit} in {target_unit.upper()} is {result_weight}")

    elif unit.lower() in ["c", "f"]:
        print("You have selected Temperature.")
        result_temp, target_unit = convert_temp(value, unit)
        print(f"{value} {unit} in {target_unit.upper()} is {result_temp}")

    elif unit.lower() in ["miles", "km"]:
        print("You have selected Length.")
        result_length, target_unit = convert_length(value, unit)
        print(f"{value} {unit} in {target_unit.upper()} is {result_length}")

    else:
        print("Invalid option, please try again!")
```

#### Usage

To run the project, execute the following command in your terminal:

```sh
python unit_converter.py
```

Follow the prompts to convert between different units of weight, temperature, and length.

#### Features

- Converts weight between pounds and kilograms.
- Converts temperature between Celsius and Fahrenheit.
- Converts length between miles and kilometers.
- Simple menu-driven interface.

### More Projects

As I continue learning, I will add more projects here. Each project will demonstrate different concepts, including:
- Working with lists, tuples, and dictionaries
- Developing small scripts and utilities
- Adding user interfaces for ease of use
- Exploring data analysis and visualization

## Contributing

If you would like to contribute, feel free to fork the repository and submit a pull request. I'm always open to suggestions, improvements, and new ideas that can enhance my learning experience.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

