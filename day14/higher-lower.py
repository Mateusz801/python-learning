from game_data import data
import art
import random


COMMAND = 'cls'


def compare(a_entry, b_entry):
    if a_entry.get('follower_count') > b_entry.get('follower_count'):
        return 'A'
    else:
        return 'B'


def print_entry(entry):
    """Takes an entry in of dictionary type and prints formatted data from it"""
    return f"{entry.get('name')}, {entry.get('description')}, from {entry.get('country')}."


def higher_lower():
    print(art.logo)
    game = True
    score = 0
    a = random.choice(data)

    while game:
        print(f"Compare A: {print_entry(a)}")
        print(art.vs)

        b = random.choice(data)
        while a == b:
            b = random.choice(data)

        print(f"Against B: {print_entry(b)}.")

        answer = input("Who has more followers? Type 'A' or 'B': ").upper()

        if answer != 'A' and answer != 'B':
            print("Wrong answer, disqualification.")
            game = False
        elif answer != compare(a, b):
            print(f"Wrong answer. Your ultimate score is: {score}")
            game = False
        else:
            score += 1
            print(f"You got it right! Current score: {score}")
            # If the right answer will be A, it stays as it is
            if answer == 'B':
                a = b


higher_lower()
# ask a user which has more followers
# compare against pick
# get the one with more followers as answer A
# pick random next sth

# fail - "Sorry, that's wrong number. Score: your_score"
