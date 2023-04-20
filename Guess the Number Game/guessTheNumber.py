"""Following code is an implementation of a game.
A random number between 1 and 100 is chosen by the machine. You as a user have to make guesses.
The temperature determines how close you're to the number
Foe example: The closer you get to the number, the HOTTER it gets. Similarly, further you get away from the number, the COLDER it gets.
Make your guesses based on that judgement.

Also make sure 'art.py' and this main file are in the same folder / location.

To generate your own logo or ASCII art, please go to the website 'www.patorjk.com/software' and select ASCII Art Generator.
"""

import random
from art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def compareTheNumbers(randomNumber, attempts):
    """Checks the answer against the user's guess
    Returns the amount of attempts user has left"""

    correctInput = True

    while correctInput:
        usersGuess = int(input("Guess the Number: "))
        if usersGuess < 0 or usersGuess > 100:
            correctInput = True
            print("Please select the number in appropriate range. Try again.")
        else:
            correctInput = False

    if randomNumber == usersGuess:
        print(
            f"You got it! You win! The number which I guessed was {randomNumber}."
        )
        return 0

    elif ((randomNumber - 3) < usersGuess) and (
        (randomNumber + 3) > usersGuess):
        print("Its STEAMING! You seem so close!")
        attempts -= 1
        print(f"You have {attempts} attempts remaining.\n")

    elif ((randomNumber - 6) < usersGuess) and (
        (randomNumber + 6) > usersGuess):
        print("Its very HOT!")
        attempts -= 1
        print(f"You have {attempts} attempts remaining.\n")

    elif ((randomNumber - 11) < usersGuess) and (
        (randomNumber + 11) > usersGuess):
        print("Its HOT!")
        attempts -= 1
        print(f"You have {attempts} attempts remaining.\n")

    elif ((randomNumber - 16) < usersGuess) and (
        (randomNumber + 16) > usersGuess):
        print("Its warm")
        attempts -= 1
        print(f"You have {attempts} attempts remaining.\n")

    elif ((randomNumber - 21) < usersGuess) and (
        (randomNumber + 21) > usersGuess):
        print("Its cold!")
        attempts -= 1
        print(f"You have {attempts} attempts remaining.\n")

    elif ((randomNumber - 31) < usersGuess) and (
        (randomNumber + 31) > usersGuess):
        print("Its very cold! You seem far.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining.\n")

    elif ((randomNumber - 41) < usersGuess) and (
        (randomNumber + 41) > usersGuess):
        print("Its chilling! You seem very far.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining.\n")

    else:
        print("Too far!")
        attempts -= 1
        print(f"You have {attempts} attempts remaining.\n")

    if attempts == 0:
        print("You lose :/")

    return attempts


print(logo)
print("Welcome to the Number Guessing Game!\n")
print(
    "I am thinking of a number between 1 and 100. Can you find out what that number is? :D\n"
)
randomNumber = random.randint(1, 100)
difficultyLevel = input("Choose the difficulty level: 'easy' or 'hard'? ")

if difficultyLevel == 'easy':
    attempts = EASY_LEVEL_ATTEMPTS

elif difficultyLevel == 'hard':
    attempts = HARD_LEVEL_ATTEMPTS

else:
    print("Invalid Selection. Please try again.")
    attempts = 0

#For testing purposes
#print(f"Shhhh, the number is {randomNumber}.")

print(f"\nYou have total {attempts} attempts.")

while attempts != 0:
    attempts = compareTheNumbers(randomNumber, attempts)
