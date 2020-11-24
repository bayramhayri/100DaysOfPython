from game_data import data
import random
from subprocess import call
import os


def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

# Format the account data


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")


def check_answer(guess, a_followers, b_followers):
    if follower_count_a > follower_count_b:
        return guess == "a"
    else:
        return guess == "b"


score = 0
game_should_contiue = True
account_b = random.choice(data)
# Make the game repeatable
while game_should_contiue:
    # Generate random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    # def get_random_account():
    #     """Get data from random account"""
    #     return random.choice(data)
    print(f"Compare A: {format_data(account_a)}.")
    print(f"Compare B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower count for each account
    # Check user is right
    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]

    is_correct = check_answer(guess, follower_count_a, follower_count_b)

    # Clear the screen between rounds
    clear()

    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_contiue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
