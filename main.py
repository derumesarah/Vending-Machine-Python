tea_price = 2.0
coffee_price = 2.5
cocoa_price = 2.0

Z0 = float(input("Please insert money (Coffee = 2,5$, Cocoa = 2$, Tea = 2$):\n"))
print(f"You have inserted: {Z0}$")

while True:
    Z1 = input("Please choose between coffee, cocoa, or tea (write down your choice):\n").lower()

    if Z1 == "tea":
        while Z0 < tea_price:
            missing_amount = tea_price - Z0
            print(f"Not enough money. Please insert at least {missing_amount}$ more.")
            Z0 += float(input("Please insert the missing amount:\n"))
        print("Enjoy your tea")
        Z0 -= tea_price
        print(f"Your change is: {Z0}$")

    elif Z1 == "coffee":
        while Z0 < coffee_price:
            missing_amount = coffee_price - Z0
            print(f"Not enough money. Please insert at least {missing_amount}$ more.")
            Z0 += float(input("Please insert the missing amount:\n"))
        Z3 = input("Coffee with or without milk?\n").lower()
        if Z3 == "with milk":
            print("Enjoy your coffee with milk")
        elif Z3 == "without milk":
            print("Enjoy your coffee without milk")
        else:
            print("Invalid selection.")
        Z0 -= coffee_price
        print(f"Your change is: {Z0}$")

    elif Z1 == "cocoa":
        while Z0 < cocoa_price:
            missing_amount = cocoa_price - Z0
            print(f"Not enough money. Please insert at least {missing_amount}$ more.")
            Z0 += float(input("Please insert the missing amount:\n"))
        print("Enjoy your cocoa")
        Z0 -= cocoa_price
        print(f"Your change is: {Z0}$")

    else:
        print("Invalid selection. This machine only dispenses tea, coffee, and cocoa.")

    next = input("Would you like to place another order? (yes/no): ").lower()

    if next != 'yes':
        if Z0 > 0:
            print(f"Your change is: {Z0}$")
        break


