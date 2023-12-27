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
}

RESOURSES = {
    "water": 400,
    "milk": 200,
    "coffee": 300,
    "money": 0
}


def print_report():
    print(f"Water: {RESOURSES['water']}ml")
    print(f"Milk: {RESOURSES['milk']}ml")
    print(f"Coffee: {RESOURSES['coffee']}g")
    print(f"Money: {RESOURSES['money']}€")

def make_coffee(coffee_type):

    ingredients = MENU[coffee_type]["ingredients"]

    for ingredient in ingredients:
        if ingredients[ingredient] > RESOURSES[ingredient]:
            print("Sorry insufficent resources")
            return


    two_euro = int(input("how many 2€ coins "))
    one_euro = int(input("how many 1€ coins "))
    fifty_cents = int(input("how many 50 cent coins "))

    sum = two_euro*2 + one_euro + fifty_cents*0.5
    if sum < MENU[coffee_type]["cost"]:
        print("Sorry insufficent funds")
        return
    
    change = sum - MENU[coffee_type]["cost"]
    RESOURSES["money"] += MENU[coffee_type]["cost"]

    for ingredient in ingredients:
        RESOURSES[ingredient] -= ingredients[ingredient]

    print(f"Here is {change} in change.")
    print(f"Enjoy your {coffee_type}")


while True:

    cmd = input("What would you like? (espresso/latte/cappuccino): ")

    if cmd == "off":
        break
    elif cmd == "report":
        print_report()
    elif cmd == "espresso":
        make_coffee("espresso")
    elif cmd == "latte":
        make_coffee("latte")
    elif cmd == "cappuccino":
        make_coffee("cappuccino")