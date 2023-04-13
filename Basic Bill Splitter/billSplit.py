""" The following program is a tip calculator. It calculates tips based on your total bill at a restaurant and calculates how much does each person needs to pay including the tip at the end.
"""

print("Welcome to the Tip Calculator!")

"""input taken and stored is always in string format, so we have to convert it into the format which we want"""

totalBill = float(input("What was your total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? Please don't add '%' sign while inputting "))

peopleToSplit = int(input("How many people are there to split the bill? "))

finalBill = totalBill + ((totalBill * tip) / 100)
billPerPerson = format(finalBill / peopleToSplit, ".2f")

finalMessage = f"Each Person should pay ${billPerPerson}"
print(finalMessage)
