from main import resources, MENU

def check_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f'Sorry there is not enough {item}')
            return False
        else:
            return True

def process_coin():
    print("Please insert coins")
    quaters = input("What many quaters?: ")
    dimes = input("What many dimes?: ")
    nickles = input("What many nickles?: ")
    pennies = input("What many pannies?: ")
    total = int(quaters) * 0.25 + int(dimes) * 0.1 + int(nickles) * 0.05 + int(pennies) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print('Sorry that\'s not enough money. Money refunded')
        return False

def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}")

profit = 0
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino)")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])