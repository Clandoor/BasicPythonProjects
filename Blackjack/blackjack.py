import random
from art import logo
import os


def calculateScore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def pickRandomCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cardDrawn = random.choice(cards)
    return cardDrawn


def compare(usersScore, computersScore):
    if usersScore == computersScore:
        return "Draw"

    elif computersScore == 0:
        return "Computer has BLACKJACK! You lose."

    elif usersScore == 0:
        return "User has BLACKJACK! You lose."

    elif usersScore > 21:
        return "Your score is above 21. You lose."

    elif computersScore > 21:
        return "Computer's score is above 21. You win!"

    elif usersScore > computersScore:
        return "You win!"

    else:
        return "You lose"


def mainGame():
    print(logo)
    userCards = []
    computerCards = []
    isGameOver = False

    for _ in range(2):
        userCards.append(pickRandomCard())
        computerCards.append(pickRandomCard())

    while not isGameOver:
        userScore = calculateScore(userCards)
        computersScore = calculateScore(computerCards)
        print(f"  Your cards: {userCards}, Current score: {userScore}")
        print(f"  Computer's cards: {computerCards[0]}")

        if userScore == 0 or computersScore == 0 or userScore > 21 or userScore == 21:
            isGameOver = True
        else:
            usersChoice = input(
                "Type 'y' to draw another card or type 'n' to pass: ")
            if usersChoice == 'y':
                userCards.append(pickRandomCard())
            else:
                isGameOver = True

    while computersScore != 0 and computersScore < 17:
        computerCards.append(pickRandomCard())
        computersScore = calculateScore(computerCards)

    print(f"  Your final hand: {userCards}, final score: {userScore}")
    print(
        f"  Computer's final hand: {userCards}, final score: {computersScore}")
    print(compare(userScore, computersScore))


while input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    os.system('cls')
    mainGame()
