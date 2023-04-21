"""Following code is a simulation of "Higher Lower Game". Select the entity which you think has more followers or fans out of the two options presented on the screen. If your choice is correct, then your score is incremented by one unit, or else if your choice is wrong, game gets over displaying your final score.
Make sure the other files are saved in the same location / folder as the first file.
"""

import random
import os
from art import vs, logo
from game_data import data


def usersDecision():
    """Asks the user for the choice"""
    usersChoice = input("Who has more followers? Type 'A' or 'B': ") 
    return usersChoice


def checkSameEntry(alreadyOccured, secondIndex):
    """Checks whether the same data has appeared or not in past. If so, then choses a new one"""
    sameEntry = True
    while sameEntry:
        secondIndex = random.randint(0, lastIndex)
        if secondIndex in alreadyOccured:
            sameEntry = True
        else:
            sameEntry = False

    return secondIndex


def compareRecords(firstIndex, secondIndex, score):
    """Compares the amount of followers and increments the value of score by one unit if needed"""
    if data[firstIndex]['follower_count'] > data[secondIndex]['follower_count']:
        score += 1
        os.system('cls')
        print(logo)
        print(f"You're right! Your score is {score}")
        return score

    else:
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        return 'END'
        

def check(firstIndex, secondIndex, alreadyOccured, score):
    """Asks the user for the input and displays appropriate statements"""
    print(f"Compare A: {data[firstIndex]['name']}, a {data[firstIndex]['description']}, from {data[firstIndex]['country']}")

    print(vs)

    print(f"\nAgainst B: {data[secondIndex]['name']}, a {data[secondIndex]['description']}, from {data[secondIndex]['country']}\n")
        
    usersChoice = usersDecision()

    if "A" == usersChoice.upper():
        score = compareRecords(firstIndex, secondIndex, score)
        if score == 'END':
            return
            
        firstIndex = secondIndex
        
        #Appends the next value to this list to make sure it does not repeat
        alreadyOccured.append(secondIndex)
        secondIndex = checkSameEntry(alreadyOccured, secondIndex)
        check(firstIndex, secondIndex, alreadyOccured, score)
        
    elif "B" == usersChoice.upper():
        score = compareRecords(secondIndex, firstIndex, score)
        if score == 'END':
            return
            
        firstIndex = secondIndex
        
        #Appends the next value to this list to make sure it does not repeat
        alreadyOccured.append(secondIndex)
        secondIndex = checkSameEntry(alreadyOccured, secondIndex)
        check(firstIndex, secondIndex, alreadyOccured, score)
            
    else:
        print("Invalid Selection.")
        return 


lastIndex = len(data) - 1
firstIndex = random.randint(0, lastIndex)
secondIndex = random.randint(0, lastIndex)
alreadyOccured = []
alreadyOccured.append(secondIndex)

print(logo)
check(firstIndex, secondIndex, alreadyOccured, score = 0)
