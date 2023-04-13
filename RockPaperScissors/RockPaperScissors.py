""" The following code is the implementation of the basic python knowledge in order to make the famous 'Rock, Paper and Scissors' game.
"""


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameImages = [rock, paper, scissors]
print("The Ultimate Game has begun!!!")
usersChoice = int(input("Choose 0 for Rock, 1 for Paper and 2 for Scissors! "))

#Need to make sure whether the given input by the user is valid or not.
if usersChoice < 0 or usersChoice > 2:
  print("Invalid Selection. Please try again :/")

else:
  print(f"\nYou chose... {gameImages[usersChoice]}")
  computersChoice = random.randint(0, 2)
  print(f"Computer Chose... {gameImages[computersChoice]}")
  
  #Draw Condition. In this case, the program can just end without executing the else part
  if usersChoice == computersChoice:
    print("Its a DRAW!")
  
  #If the game is not draw, then obviously one of the player will win
  #There are multiple ways to approach this logic.
  else:
    if usersChoice == 0:
      if computersChoice == 1:
        print("You lose :(")
      else:
        print("You win!")
    
    elif usersChoice == 1:
      if computersChoice == 0:
        print("You win!")
      else:
        print("You lose :(")
    
    else:
      if computersChoice == 1:
        print("You win!!")
      else:
        print("You lose :(")
