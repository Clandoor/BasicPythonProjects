"""
Following code is a simple implementation of a coffee machine. Read the file attached in the folder for more details.
The functions return 'True' and 'False' in such a way depending upon the situation which controls the while loop running.
Be sure to 'readme' file to get to know more specifics.
"""

PRICE_OF_ESPRESSO = 1.50
PRICE_OF_LATTE = 2.50
PRICE_OF_CAPPUCCINO = 3.00

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "moneyInsideMachine": 0
}


def displayDetails():
    """Displays the updated list of ingredients"""
    print(f"Water: {resources['water']} ml\nMilk: {resources['milk']} ml\nCoffee: {resources['coffee']} g\nMoney: ${resources['moneyInsideMachine']}")
    return True


def checkResources(usersChoice):
    """Checks whether ingredients are enough to make the coffee or not. If so, then user is further prompted with $"""
    if usersChoice == '1':
        if resources['water'] < 50:
            print("Sorry, not enough water to make the coffee.\n")
            return False
        elif resources['coffee'] < 18:
            print("Sorry, not enough coffee at the moment to make Espresso.\n")
            return False
        else:
            askAndProcessCoins(usersChoice)
            return True

    elif usersChoice == '2':
        if resources['water'] < 200:
            print("Sorry, not enough water to make the coffee.\n")
            return False
        elif resources['milk'] < 150:
            print("Sorry, not enough milk to make the coffee.\n")
            return False
        elif resources['coffee'] < 24:
            print("Sorry, not enough coffee at the moment to make Espresso.\n")
            return False
        else:
            askAndProcessCoins(usersChoice)
            return True

    else:
        if resources['water'] < 250:
            print("Sorry, not enough water to make the coffee.\n")
            return False
        elif resources['coffee'] < 24:
            print("Sorry, not enough coffee at the moment to make Espresso.\n")
            return False
        elif resources['milk'] < 100:
            print("Sorry, not enough milk to make the coffee.\n")
            return False
        else:
            askAndProcessCoins(usersChoice)
            return True


def askAndProcessCoins(usersChoice):
    """Asks the user for the money, processes the money, returns the changes and displays the appropriate message"""
    print("Please insert the coins: ")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    usersMoney = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    if usersChoice == '1':
        if usersMoney >= PRICE_OF_ESPRESSO:
            resources['water'] -= 50
            resources['coffee'] -= 18
            change = usersMoney - PRICE_OF_ESPRESSO
            resources['moneyInsideMachine'] += PRICE_OF_ESPRESSO
            print(f"Enjoy your Espresso!\n${format(change, '.2f')} change.\n")
        else:
            print("Sorry, that's not enough money. Money refunded.\n")

    elif usersChoice == '2':
        if usersMoney >= PRICE_OF_LATTE:
            resources['water'] -= 200
            resources['milk'] -= 150
            resources['coffee'] -= 24
            change = usersMoney - PRICE_OF_LATTE
            resources['moneyInsideMachine'] += PRICE_OF_LATTE
            print(f"Enjoy your Latte!\n${format(change, '.2f')} change.\n")
        else:
            print("Sorry, that's not enough money. Money refunded.\n")

    else:
        if usersMoney >= PRICE_OF_CAPPUCCINO:
            resources['water'] -= 250
            resources['milk'] -= 100
            resources['coffee'] -= 24
            change = usersMoney - PRICE_OF_CAPPUCCINO
            resources['moneyInsideMachine'] += PRICE_OF_CAPPUCCINO
            print(f"Enjoy your Cappuccino!\n${format(change, '.2f')} change.\n")
        else:
            print("Sorry, that's not enough money. Money refunded.\n")

    return True


"""In appropriate situations, the functions will return 'False' and the loops will end based on those situations.
"""
shouldKeepGoing = True

while shouldKeepGoing:
    print("1. Espresso\n2. Latte\n3. Cappuccino")
    usersEntry = input("What would you like? Please select from the following: Choose number only: ")

    if usersEntry == '1':
        shouldKeepGoing = checkResources(usersEntry)

    elif usersEntry == '2':
        shouldKeepGoing = checkResources(usersEntry)

    elif usersEntry == '3':
        shouldKeepGoing = checkResources(usersEntry)

    elif usersEntry == 'report':
        shouldKeepGoing = displayDetails()
        print()

    elif usersEntry == 'off':
        shouldKeepGoing = False

    else:
        print("Invalid Selection. Please try again.")
