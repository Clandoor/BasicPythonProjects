"""Following code depicts how Caesar Cipher works. Potentially more functionality and improvements in the code.
"""

from art import logo

print(logo)


def caesar(userText, key, decision):
    finalText = ""

    if decision == 'decode':
        key *= -1

    for letter in userText:
        if letter not in alphabet:
            finalText += letter
        else:
            indexOfLetter = alphabet.index(letter)
            newIndex = ((indexOfLetter + key) + 26) % 26
            finalText += alphabet[newIndex]

    print("\n" + f"The {decision}d text is: {finalText}")


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

shouldContinue = True

while shouldContinue:
    print("Do you want to Encrypt or Decrypt?")
    direction = input("Type 'encode' for Encrypt or 'decode' for Decrypt: ")

    text = input("Enter your Message here:\n").lower()
    shift = int(input("Type the Key:\n"))

    caesar(userText=text, key=shift, decision=direction)

    print("\nDo you want to use the Cipher again?")
    usersChoice = input("Type Yes or No: ").lower()

    if usersChoice == "no":
        shouldContinue = False

    print()

print("Goodbye. Take care.")
