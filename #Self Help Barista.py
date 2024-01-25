#Self Help Barista
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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def insert_money():
    #return total money inserted
    print("Insert your coins")
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.1
    total += int(input("How many nickels?:")) * 0.05
    total += int(input("How many pennies?:")) * 0.01
    return total

def check_transaction(payment, drink_cost):
    #return true if payment is enough, return false if not enough
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here's your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("You did not have enough money. Here's your money back.")
        return False


is_on = True

while is_on is True:
    customer_choice = input("What would you like? (espresso/latte/cappucino): ")
    if customer_choice == "off":
        is_on = False
    elif customer_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[customer_choice]
        if check_resources(drink["ingredients"]):
            payment = insert_money()
            check_transaction(payment, drink['cost'])
