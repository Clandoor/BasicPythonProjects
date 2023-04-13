"""Following is a simple implementation of if and else statements. Using that knowledge, a simple game has been created where the story moves based on the decision which the individual makes at any point in the story.
Keeping the simplicity in mind, any one decision will lead to 'Game Over' and rest of the decisions will make the story go forward.
"""


"""Following ASCII art is availabe from the website https://ascii.co.uk/art/
"""
print('''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
                \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\www/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')

print("THE ADVENTURE BEGINS!!!")
print("Welcome to Treasure Island!!")
print("Your mission is to find the hidden treasure!\n") 

pathWay = input("You're on a path which is forked further. Left one leads deep into the woods and other leads to the swamp. Which way do you wish to continue?\n \nChoose 'left' or 'right': ").lower()

if pathWay == "left":
  print("\nYou shiver your way across the dense woods, your senses heightened as never before. Suddenly, you stumble upon a lake. Do you want to wait for the boat or do you wish to swim your way accross?")
  crossLake = input("\nChoose 'wait' or 'swim': ").lower()

  if crossLake == "wait":
    print("\nYou manage to somehow get on the boat and make it to the other side of the lake. You enter the caves inside the mountains with your body shivering.")
    print("\nYou encounter three sages each wearing a red, yellow and a blue tunic.")
    tunicColor = input("\nPick the sages whom you want to follow along.\nChoose 'red', 'yellow' or 'blue': ").lower()

    if tunicColor == "red":
      print("\nThe Sage unleashes their almighty rage on you thereby leaving you burnt in ashes while your soul endlessly roams around the caves till the end of time. Game Over.")
  
    elif tunicColor == "blue":
      print("\nThe Sage hypnotizes you leaving you in their control thereby making you their puppet for the rest of the iternity. Game Over.")
  
    else:
      print("\nThe Sage guides you towards the hidden treasure as you fulfil your destiny! Congratulations! You have succeeded!!")
    
  else:
    print("\nYou feel your body paralyzed by some mysterious force. You're started to consumed by the depth of the lake slowly being engulfed within the never ending abyss.\nGame Over.")
      
else:
  print("\nThe evil elves in the swamps consume you! Game Over.")
