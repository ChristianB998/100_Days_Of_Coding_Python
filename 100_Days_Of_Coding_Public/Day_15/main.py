MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "ingredients": {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    },
    "money": 0,
}

machine_routine = True

def format_report(resources):
    """Format the report so that the output is in correct format"""
    key_water = "water"
    key_milk = "milk"
    key_coffee = "coffee"
    key_money = "money"
    print(f"{key_water}:  {resources['ingredients'][key_water]} ml")
    print(f"{key_milk}:   {resources['ingredients'][key_milk]} ml")
    print(f"{key_coffee}: {resources['ingredients'][key_coffee]} ml")
    print(f"{key_money}:  {float(resources[key_money])} $")

def check_resources(resources, users_input, proceed):
    """Check if resources are sufficient"""
    for item in resources["ingredients"]:
        if resources["ingredients"][item] >= MENU[users_input]["ingredients"][item]:
            proceed = True
            return print("Pleaser insert coins"), proceed
        else:
            proceed = False
            return print(f"Sorry there is not enough {item}"), proceed

def insert_money_and_check_amount(resources, users_input, summe):
    """quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01"""
    print(f"Please insert coins.")
    missing_money = True
    while missing_money:
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickles = int(input("How many nickles: "))
        pennies = int(input("How many pennies: "))
        summe = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
        if summe < (MENU[users_input]["cost"]):
            missing_amount = (MENU[users_input]["cost"]) - summe
            print(f"Missing money please insert the missing amount of ${round(missing_amount, 2)}")
        else:
            return summe

def calculate_return(summe, user_input):
    item_price = (MENU[users_input]["cost"])
    if summe >= item_price or summe == item_price:
        return summe - item_price
        # print(f"Rest: {rest}")
        # if rest > 0:
        #     quarter_return = int(rest // 0.25)
        #     rest = round(rest, 2) % 0.25
        #     print(f"Count of QuarterReturn: {quarter_return}")
        #
        #     dimes_return = int(rest // 0.1)
        #     rest = round(rest, 2) % 0.1
        #     print(f"Count of dimes return: {dimes_return}")
        #
        #     nickles_return = int(rest // 0.05)
        #     rest = round(rest, 2) % 0.05
        #     print(f"count of nickles return: {nickles_return}")
        #
        #     pennies_return = int(rest // 0.01)
        #     rest = round(rest, 2) % 0.01
        #     print(f"Count of pennies return: {pennies_return}")
    elif summe < item_price:
        rest = item_price - summe
        print(f"You inserted not enough coins please add ${rest}")
        return calculate_return(rest, user_input)

def update_dict(users_input, MENU, resources, rest):
    for item in resources["ingredients"]:
        #if resources["ingredients"][item] >= MENU[users_input]["ingredients"][item]:
        resources["ingredients"][item] = resources["ingredients"][item] - MENU[users_input]["ingredients"][item]

    resources["money"] = resources["money"] + MENU[users_input]["cost"]

# Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
## check the users input
## After dink is served the prompt should be shown to the next customer again
while machine_routine:
    counter = 0
    proceed = True
    summe = 0
    users_input = input("What would you like? (espresso/latte/cappuccino): ")
# turn off the Machine by entering "off" -> Executions ends here
    if users_input == "off":
        machine_routine = False
# print report when entering "report" of the currently available resources
    elif users_input == "report":
        format_report(resources)
    # check if resources are sufficient
    elif users_input in ["espresso", "latte", "cappuccino"]:
        #check_resources(resources, users_input, proceed)
        for item in resources["ingredients"]:
            if resources["ingredients"][item] >= MENU[users_input]["ingredients"][item]:
                counter += 1
            else:
                print(f"Sorry there is not enough {item}")
        if counter == 3:
            summe = insert_money_and_check_amount(resources, users_input, summe)
            print(f"Summe: {summe}")
            rest = round(calculate_return(summe, users_input), 2)
            print(f"Here is your ${rest} change.")
            print(f"Please enjoy your {users_input}.")
            update_dict(users_input, MENU, resources, rest)
        elif counter < 3:
            print("Wait for service provider.")
    else:
        print(f"There was a typo you entered: {users_input}")
# Check if transaction is successful and report is updated

# make the coffee




