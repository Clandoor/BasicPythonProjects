"""Following code is a simple calculator, yet might be an effective way to implement it using functions within dictionaries.
Please make sure 'art.py' and this main file are in same folder or same location to avoid providing relative path.
"""

from art import logo


def addition(numberOne, numberTwo):
    return numberOne + numberTwo


def substraction(numberOne, numberTwo):
    return numberOne + numberTwo


def multiplication(numberOne, numberTwo):
    return numberOne * numberTwo


def division(numberOne, numberTwo):
    return numberOne / numberTwo


def calculator():
    print(logo)
    numberOne = float(input("Enter the Number One: "))

    for symbol in operations:
        print(symbol)

    shouldContine = True

    while shouldContine:
        operator = input("Pick an Operation: ")
        numberTwo = float(input("Enter the Next Number: "))
        calculate = operations[operator]
        result = calculate(numberOne, numberTwo)
        print(f"{numberOne} {operator} {numberTwo} = {result}\n")

        usersChoice = input(
            f"Type 'y' to continue calcuating with {result}, or type 'n' to start a new calculation from the beginning: "
        ).lower()

        if usersChoice == "y":
            numberOne = result
        else:
            shouldContine = False
            print("")
            calculator()


operations = {
    "+": addition,
    "-": substraction,
    "*": multiplication,
    "/": division
}

calculator()
