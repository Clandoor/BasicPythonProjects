"""The following is a "Hangman Game". To know more in detail how the game works, please visit: 
'https://hangmanwordgame.com/'  OR  'https://en.wikipedia.org/wiki/Hangman_(game)'
Please make sure in whichever IDE you run this code, make sure all the files are saved in the same folder so they are accessible directly without giving the relative path.
"""


import random
from hangmanArt import logo, stages
from hangmanWords import wordList 

"""Alternatively, one can just import the whole module file, but need to mention the module name whenever one is accessing the data inside that specific module.
For example hangmanArt.stages whenever one wants to use 'stages' list.
"""

print(logo)

#Can also use chosenWord = wordList[random.randint(0, 2)]
chosenWord = random.choice(wordList)

playerLives = 6
endOfGame = False
chosenWordLength = len(chosenWord)
displayingList = []

for i in range(chosenWordLength):
    displayingList += "_"

"""Potentially a better approach would be using the condition 
while "_" not in displayingList: 
"""

while not endOfGame:
    isCorrectGuess = False
    usersGuess = input("Guess a letter: ").lower()
    
    while usersGuess in displayingList:
        print(f"{usersGuess} already guessed. Please try again.\n")
        print(f"{' '.join(displayingList)}\n")
        usersGuess = input("Guess a letter: ").lower()
    
    for i in range(chosenWordLength):
        if chosenWord[i] == usersGuess:
            displayingList[i] = usersGuess
            isCorrectGuess = True

    """Can also use -> if usersGuess not in chosenWord:
    """
    if not isCorrectGuess:
        playerLives -= 1
        print(f"{usersGuess} is not in the right guess. You lose a life :/")
        print(f"\nYou now have {playerLives} lives left.")
        print(stages[playerLives])
        print("\n" + f"{' '.join(displayingList)}\n")
        
        if playerLives == 0:
            print("Oh no! Hangman died :/")
            print("You lose!")
            endOfGame = True
        
    else:
        print("\n" + f"{' '.join(displayingList)}\n")
        print("Correct Guess! Nice work!")
        
        if "_" not in displayingList:
            endOfGame = True
            print("Impressive! You have saved the hangman! You win!")
