from ingredients import *


# Check the input should be an int for the money
def insertMoney(inputString):
    while True:
        try:
            mon = int(input(inputString))
            break
        except ValueError:
            print()
    return mon


# The Program will never end until the user input 'off'
while True:
    # Check if the user input is right: espresso, latte, cappuccino, off, report
    while True:
        try:
            select = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if (
                select == "espresso"
                or select == "latte"
                or select == "cappuccino"
                or select == "off"
                or select == "report"
            ):
                break
        except ValueError:
            print("Invalid input. Please choose (espresso/latte/cappuccino): ")
    # IF the user input is 'off' the program stops
    if select == "off":
        break
    # When the user enters “report” to the prompt, a report should be generated that shows the current resource values.
    elif select == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    # User wants espresso
    elif select == "espresso":
        # Check for water, espresso needs 50ml of water
        if MENU[select]["ingredients"]["water"] < 50:
            print("Sorry there is not enough water")
        # Check for coffee, espresso needs 18g of coffee
        elif MENU[select]["ingredients"]["coffee"] < 18:
            print("Sorry there is not enough coffee")
        else:
            quarters = insertMoney("Insert quarters: ")
            dimes = insertMoney("Insert dimes: ")
            nickles = insertMoney("Insert nickles: ")
            pennies = insertMoney("Insert pennies: ")
            money = (
                (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
            )
            if money < 1.5:
                print("Sorry that's not enough money. Money refunded.")
                money = 0
            else:
                if money > 1.5:
                    refund = money - 1.5
                    print(f"Here is ${round(refund, 2)} dollars in change.")
                print()
                print("Report before purchasing espresso:")
                print(f"Water: {resources['water']}ml")
                print(f"Coffee: {resources['coffee']}g")
                print("Money: $0")
                print()
                resources["water"] -= 50
                resources["coffee"] -= 18
                print("Report after purchasing espresso:")
                print(f"Water: {resources['water']}ml")
                print(f"Coffee: {resources['coffee']}g")
                money -= refund
                print(f"Money: ${money}")
                print()
                print("Here is your espresso. Enjoy!")
                money = 0

    # User wants Latte
    elif select == "latte":
        # Check for water, Latte needs 50ml of Water
        if MENU[select]["ingredients"]["water"] < 200:
            print("Sorry there is not enough water")
        # Check for coffee, Latte needs 18g of Milk
        elif MENU[select]["ingredients"]["milk"] < 150:
            print("Sorry there is not enough milk")
        # Check for coffee, Latte needs 18g of coffee
        elif MENU[select]["ingredients"]["coffee"] < 24:
            print("Sorry there is not enough coffee")
        else:
            quarters = insertMoney("Insert quarters: ")
            dimes = insertMoney("Insert dimes: ")
            nickles = insertMoney("Insert nickles: ")
            pennies = insertMoney("Insert pennies: ")
            money = (
                (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
            )
            if money < 2.5:
                print("Sorry that's not enough money. Money refunded.")
                money = 0
            else:
                if money > 2.5:
                    refund = money - 2.5
                    print(f"Here is ${round(refund, 2)} dollars in change.")
                print()
                print("Report before purchasing latte:")
                print(f"Water: {resources['water']}ml")
                print(f"Milk: {resources['milk']}ml")
                print(f"Coffee: {resources['coffee']}g")
                print("Money: $0")
                print()
                resources["water"] -= 200
                resources["milk"] -= 150
                resources["coffee"] -= 24

                print("Report after purchasing latte:")
                print(f"Water: {resources['water']}ml")
                print(f"Milk: {resources['milk']}ml")
                print(f"Coffee: {resources['coffee']}g")
                money -= refund
                print(f"Money: ${money}")
                print()
                print("Here is your latte. Enjoy!")
                money = 0
    # User wants cappuccino
    elif select == "cappuccino":
        # Check for water, cappuccino needs 50ml of Water
        if MENU[select]["ingredients"]["water"] < 250:
            print("Sorry there is not enough water")
        # Check for coffee, cappuccino needs 18g of Milk
        elif MENU[select]["ingredients"]["milk"] < 100:
            print("Sorry there is not enough milk")
        # Check for coffee, cappuccino needs 18g of coffee
        elif MENU[select]["ingredients"]["coffee"] < 24:
            print("Sorry there is not enough coffee")
        else:
            quarters = insertMoney("Insert quarters: ")
            dimes = insertMoney("Insert dimes: ")
            nickles = insertMoney("Insert nickles: ")
            pennies = insertMoney("Insert pennies: ")
            money = (
                (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
            )
            if money < 3.0:
                print("Sorry that's not enough money. Money refunded.")
                money = 0
            else:
                if money > 3.0:
                    refund = money - 3.0
                    print(f"Here is ${round(refund, 2)} dollars in change.")
                print()
                print("Report before purchasing cappuccino:")
                print(f"Water: {resources['water']}ml")
                print(f"Milk: {resources['milk']}ml")
                print(f"Coffee: {resources['coffee']}g")
                print("Money: $0")
                print()
                resources["water"] -= 250
                resources["milk"] -= 100
                resources["coffee"] -= 24

                print("Report after purchasing cappuccino:")
                print(f"Water: {resources['water']}ml")
                print(f"Milk: {resources['milk']}ml")
                print(f"Coffee: {resources['coffee']}g")
                money -= refund
                print(f"Money: ${money}")
                print()
                print("Here is your cappuccino. Enjoy!")
                money = 0
