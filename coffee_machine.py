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
UNITS = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g"
}

def add():
    """Prompts user to add resources and update the resources dictionary."""
    while True:
        resource = input("What resource would you like to add? (water/milk/coffee):  ").lower()
        if resource not in resources:
            print ("Resource not found. Please enter the resource again.")
            continue
        amount = int(input("What's the amount you like to add?  "))
        resources[resource] += amount
        is_continue = input("Do you want to add more resources? Y or N   ")
        if is_continue == "n":
            break


def report():
    """Displays the items in the resources dictionary"""
    for resource, amount in resources.items():
        if resource == "money":
            print (f"{resource.title()}: ${amount:.2f}")
        else:
            print(f"{resource.title()}: {amount}{UNITS[resource]}")


def machine_maintenance():
    """prompts user to choose a maintenance operation."""
    while True:
        choice = input("What would you like to do? (Report/Add)").lower()
        if choice != "report" and choice != "add":
            print ("Sorry, please repeat that again.")
            continue
        elif choice == "report":
            report()
            break
        elif choice == "add":
            add()
            break
    while True:
        choice = input("What would you like to do? (Report/Add)").lower()
        if choice != "report" and choice != "add":
            print ("Sorry, please repeat that again.")
            continue
        elif choice == "report":
            report()
            break
        elif choice == "add":
            add()
            break

def coins_calc(quarters, dimes, nickles, pennies):
    """calculates and returns entered coins total"""
    return quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
def money_processing (total, cost):
    if total > cost:
        resources["money"] += cost
        print (f"Here is your change: ${total - cost:.2f}")
        return True
    elif cost > total:
        print (f"Sorry, that's not enough money. Money refunded.")
        return False
    else:
        resources["money"] += cost
        return True
    
def price_calc(order):
    """prompts user to enter coins and interacts with the amount the user entered"""
    cost = MENU[order]['cost']
    print("Please insert coins.")
    q = (int(input("How many quarters?")))
    d = (int(input("How many dimes?")))
    n = (int(input("How many nickles?")))
    p = (int(input("How many pennies?")))
    total = coins_calc(q, d, n, p)
    if money_processing(total,cost):
        return True


def is_resources_insufficient(order):
    """checks if any of the resources insufficient to make the order"""
    ing = MENU[order]["ingredients"]
    low_resource = []
    for item, amount in ing.items():
        if amount > resources[item]:
            low_resource.append(item)
    if low_resource:
        for item in low_resource:
            print (f"Sorry, there is not enough {item}.")
        return True
    return False


def making_coffee(coffee):
    """subtracting the order ingredients from the resources dictionary"""
    ing = MENU[coffee]["ingredients"]
    for item, amount in ing.items():
        resources[item] -= ing[item]
    return f"Here is your {coffee} ☕️ Enjoy!"


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0}


while True:
    user_order = input("What would you like? (espresso/latte/cappuccino/maintenance):  ").lower()
    if user_order == "maintenance":
        machine_maintenance()
        continue
    elif user_order == "off":
        break
    elif user_order not in MENU:
        print ("Sorry, this order is not in the menu.")
        continue
    else:
        if is_resources_insufficient(user_order):
            continue
        price_msg = price_calc(user_order)
        if not price_msg:
            continue
        print(making_coffee(user_order))

