# GUESS THE NUMBER

import sys
import random


def generate_random_number():
    return random.randrange(1, 100)


def evaluation(guess, random_n):
    if guess > random_n:
        print(f"Wrong! Lower, the number is!")
    elif guess < random_n:
        print(f"Wrong! Higher, the number is!")
    else:
        print(f"Well done! Correct, your guess is!")


def end_of_game(tries):
    if tries > 7:
        print(f"{tries} tries, you needed. Practice more, you must!")
    elif tries > 1:
        print(f"Good! Only {tries} tries to find the correct number, you needed.")
    else:
        print(f"Marvelous! Only once, you needed to try.\nA great Jedi master, one day you will become!")


if __name__ == '__main__':
    random.seed()

    print("*" * 61)
    print(f"Welcome youngling! The \"Guess the number\" game, we will play!")
    print(f"Use the Force to find the correct number, you must!")
    print(f"A hint, I will give: between 1 and 100, the umber is.")

    random_number = int(generate_random_number())
    number_guessed = int(0)
    number_of_tries = int(0)

    # Uncomment line below for testing purposes
    # print(random_number)

    while random_number != number_guessed:
        number_guessed = int(input("\nGuess the number, you must:"))
        evaluation(number_guessed, random_number)
        number_of_tries += 1

    end_of_game(number_of_tries)

    sys.exit(0)
