from game_data import data
import art
import random

game_should_continue = True
score = 0
account_b = random.choice(data)

def format_data(account):
    """format the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, in {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """" Take a user's guess and the follower counts and returns if the got it right """
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(art.logo)
while game_should_continue:
    # Generate a random account from the game data
    account_a = account_b               # took a long time, b is first declared at the top and will not be updated later in while
    account_b = random.choice(data)
    if account_a == account_b:
        account_b == random.choice(data)


    print(f"Compare A: {format_data(account_a)}")
    print(art.vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess,
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(art.logo)
    # check if user is correct
    ## Get follower count of each account
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_account, b_follower_account)
    # give user a feedback on their guess.
    # score keeping

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Finale score is {score}")
        game_should_continue = False


