# GUESS THE NUMBER

import sys
import random


def generate_random_number():
    return random.randrange(1, 100)


def evaluation(guess, random_n):
    if guess > random_n:
        print("Wrong! Lower, the number is!")
    elif guess < random_n:
        print("Wrong! Higher, the number is!")
    else:
        print("Well done! Correct, your guess is!")


def end_of_game(tries):
    if tries > 7:
        print(f"{tries} tries, you needed. Practice more, you must!")
    elif tries > 1:
        print(f"Good! Only {tries} tries to find the correct number, you needed.")
    else:
        print("Marvelous! Only once, you needed to try.\nA great Jedi master, one day you will become!")


def player_input():
    inpt = input("\nGuess the number, you must:")
    while not inpt.isdigit():
        inpt = input("A number, you must guess:")
    return int(inpt)


if __name__ == '__main__':
    random.seed()

    print("*" * 61)
    print("Welcome youngling! The \"Guess the number\" game, we will play!")
    print("Use the Force to find the correct number, you must!")
    print("A hint, I will give: between 1 and 100, the umber is.")

    random_number = generate_random_number()
    number_guessed = 0
    number_of_tries = 0

    # Uncomment line below for testing purposes
    # print(random_number)

    while random_number != number_guessed:

        number_guessed = player_input()
        evaluation(number_guessed, random_number)
        number_of_tries += 1

    end_of_game(number_of_tries)

    sys.exit(0)
