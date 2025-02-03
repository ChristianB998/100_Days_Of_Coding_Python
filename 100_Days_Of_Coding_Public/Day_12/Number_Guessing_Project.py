import random

# is inefficient -> revise it later if i not forget it in the future

game_is_on = True
EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5

def game(counter):
    random_number = random.randint(0, 100)
    answer = ""
    while random_number != answer:
        if counter == 0:
            print(f"You have zero attempts left.")
            print("\n" * 20)
            answer = random_number # I set this to break the while loop.
        elif counter >= 1:
            print(f"You have {counter} tries left.")
            answer = int(input("Make a guess: "))
            print(f"Random number is: {random_number}")
            compare(random_number, answer)
            counter -= 1


def compare(numb, answer):
    if numb > answer:
        return print("Too low.")
    elif numb < answer:
        return print("Too high.")
    else:
        return print(f"You got it! The answer was {answer}")

def game_go():
    counter = 1
    while game_is_on:
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard'")

        if difficulty == "easy":
            counter = EASY_LEVEL_TURN
            game(counter)

        elif difficulty == "hard":
            counter = HARD_LEVEL_TURN
            game(counter)
        else:
            print(f"You have a typo. Please enter 'easy' or 'hard' in the next selection.")
            print("\n" * 15)

game_go()






