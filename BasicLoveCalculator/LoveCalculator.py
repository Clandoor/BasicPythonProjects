""" Following program calculates how fit a couple is together in terms of LOVE. """

print("Welcome to the Love Calculator! <3")
nameOne = input("What is your name? \n")
nameTwo = input("What is your partner's name? \n")

combinedNames = nameOne + nameTwo
combinedNames = combinedNames.lower()

occOfT = combinedNames.count("t")
occOfR = combinedNames.count("r")
occOfU = combinedNames.count("u")
occOfE1 = combinedNames.count("e")

occurenceOfTrue = occOfT + occOfR + occOfU + occOfE1

occOfL = combinedNames.count("l")
occOfO = combinedNames.count("o")
occOfV = combinedNames.count("v")
occOfE2 = combinedNames.count("e")

occurenceOfLove = occOfL + occOfO + occOfV + occOfE2

loveScore = int(str(occurenceOfTrue) + str(occurenceOfLove))

if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like a DYNAMITE!!")

elif loveScore > 40 and loveScore < 50:
    print(f"Your score is {loveScore}, you are alright together.")

else:
    print(f"Your score is {loveScore}.")
