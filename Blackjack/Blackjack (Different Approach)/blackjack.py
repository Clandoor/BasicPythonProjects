""" Following is a bit different implementation of the blackjack game. Its sligthly larger and bigger than the previous one, but yet still different. One might be better than the other. Code might seem bit complicated as compared to the earlier implementation.
Please make sure 'art.py' is in the same folder / location as this main file.
"""

import random
import os
from art import logo


def pickRandomCard(cards):
    """Picks a random card from the array cards and returns that random value picked"""
    return random.choice(cards)


def checkBlackJack(anyCards):
    """Checks whether blackjack occured or not"""
    if sum(anyCards) == 21 and len(anyCards) == 2:
        return True


def printDetails(usersCardList, computersCardList, usersTotal, computersTotal):
    """Prints the details once the game has ended."""
    print(f"  Your final hand: {usersCardList}, final score: {usersTotal}")
    print(
        f"  Computer's final hand: {computersCardList}, final score: {computersTotal}"
    )


def usersTurn(cards, usersCardList, computersCardList):
    """Function for user to select cards and their turn"""
    usersChoice = input("Type 'y' to draw another card or type 'n' to pass: ")
    print()
    
    #If user says yes, then it will ask user to choose again, otherwise simply return the total.
    if usersChoice == 'y':
        usersCardList.append(pickRandomCard(cards))
        usersTotal = sum(usersCardList)
        computersTotal = sum(computersCardList)
        
        #Rule of the game, a flexibility for someone who chose a card and got an ACE
        if 11 in usersCardList and usersTotal > 21:
            usersCardList.remove(11)
            usersCardList.append(1)
            usersTotal = sum(usersCardList)
            
        #Checking for blackjack
        isBlackJack = checkBlackJack(usersCardList)
        if isBlackJack:
            printDetails(usersCardList, computersCardList, usersTotal,
                         computersTotal)
            print("Blackjack!! User won!")
            return 0

        if usersTotal == 21:
            printDetails(usersCardList, computersCardList, usersTotal,
                         computersTotal)
            print("You win!")
            return False

        elif usersTotal > 21:
            printDetails(usersCardList, computersCardList, usersTotal,
                         computersTotal)
            print("You lose :/")
            return False

        else:
            print(f"  Computer's first card: {computersCardList[0]}")
            print(
                f"  Your current hand: {usersCardList}, final score: {usersTotal}"
            )
            usersTurn(cards, usersCardList, computersCardList)
    
    else:
        usersTotal = sum(usersCardList)
        return usersTotal


def computersTurn(cards, usersCardList, computersCardList, usersTotal):
    """Function for the computer once user no longer continues picking cards"""
    computersTotal = sum(computersCardList)
    
    #Rule of the game, a flexibility for someone who chose a card and got an ACE
    if 11 in computersCardList and computersTotal > 21:
        computersCardList.remove(11)
        computersCardList.append(1)
        computersTotal = sum(computersCardList)
        
    #Checking for blackjack
    isBlackJack = checkBlackJack(computersCardList)
    if isBlackJack:
        printDetails(usersCardList, computersCardList, usersTotal,
                     computersTotal)
        print("Blackjack!! Computer won!")
        return 0
    
    #In this case, according to the game rules, the dealer has to keep choosing cards till the sum is greater than 16.
    if computersTotal < 17:
        computersCardList.append(pickRandomCard(cards))
        computersTurn(cards, usersCardList, computersCardList, usersTotal)

    elif computersTotal == 21:
        printDetails(usersCardList, computersCardList, usersTotal,
                     computersTotal)
        print("You lose :/")
        return 0

    elif computersTotal > 21:
        printDetails(usersCardList, computersCardList, usersTotal,
                     computersTotal)
        print("Computer exceeded over 21. You win!!")
        return 0

    elif computersTotal > usersTotal:
        printDetails(usersCardList, computersCardList, usersTotal,
                     computersTotal)
        print("You lose :/")
        return 0

    elif computersTotal < usersTotal:
        printDetails(usersCardList, computersCardList, usersTotal,
                     computersTotal)
        print("You win!")
        return 0

    else:
        printDetails(usersCardList, computersCardList, usersTotal,
                     computersTotal)
        print("Woah, its a DRAW!")
        return 0


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
usersChoice = input(
    "Do you want to play game of Blackjack? Yes for 'y' and 'n' for No")

if usersChoice == 'y':
    os.system('cls')
    print(logo)
    playGame = True

    usersCardList = []
    computersCardList = []

    for _ in range(2):
        usersCardList.append(pickRandomCard(cards))
        computersCardList.append(pickRandomCard(cards))

    usersTotal = sum(usersCardList)

    print(
        f"  Your cards: {usersCardList}, Current score: {sum(usersCardList)}")
    print(f"  Computer's first card: {computersCardList[0]}")

    if usersTotal == 21:
        print("Blackjack!! You win!")

    else:
        usersTotal = usersTurn(cards, usersCardList, computersCardList)

        #usersTotal is also used in such a way that if it returns False, then the game has ended and we can end.
        if usersTotal != False:
            usersTotal = sum(usersCardList)
            computersTurn(cards, usersCardList, computersCardList, usersTotal)

      
