from random import randint

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
GOAL = randint(1, 100)


def check_plural(p_attempts):
    if p_attempts > 1:
        return "attempts"
    else:
        return "attempt"


def wrong_answer(p_guess, p_attempts):
    if p_guess > GOAL:
        print("Too high.")
    else:
        print("Too low.")
    if p_attempts - 1 > 0:
        print("Guess again.")
    return p_attempts - 1


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        return EASY_ATTEMPTS
    elif difficulty == "hard":
        return HARD_ATTEMPTS


def game():
    print("Welcome to the Number Guessing Game!\n"
          "I'm thinking of a number between 1 and 100.")

    attempts = set_difficulty()

    while attempts > 0:
        print(f"You have {attempts} {check_plural(attempts)} remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess != GOAL:
            attempts = wrong_answer(guess, attempts)
        else:
            print(f"You got it! The answer was {GOAL}.")
            return

    print("You've run out of guesses, you lose.")


game()
# easy - 10 attempts
# hard - 5
# display number of left attempts
# say if your guess is too high or too low

