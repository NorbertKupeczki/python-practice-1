# GUESS THE NUMBER by Norbert Kupeczki

import sys
import random


def generate_random_number():
    return random.randrange(1, 100)


# Function to evaluate the player's guess and give them feedback
def evaluation(guess, random_n):
    if guess > random_n:
        print("Wrong! Lower, the number is!")
    elif guess < random_n:
        print("Wrong! Higher, the number is!")
    else:
        print("Well done! Correct, your guess is!")


# Feedback on the player's performance based on how many times they had to try to find the number
def end_of_game(tries):
    if tries > 7:
        print(f"{tries} tries, you needed. Practice more, you must!")
    elif tries > 1:
        print(f"Good! Only {tries} tries to find the correct number, you needed.")
    else:
        print("Marvelous! Only once, you needed to try.\nA great Jedi master, one day you will become!")


# Asking for a player input + validation
def player_input():
    p_input = input("\nGuess the number, you must:")
    while not p_input.isdigit():
        p_input = input("A number, you must guess:")
    return int(p_input)


def guess_the_number():
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

    # Keep looping until the player finds the correct number
    while random_number != number_guessed:
        number_guessed = player_input()
        evaluation(number_guessed, random_number)
        number_of_tries += 1

    # End of game message to the player
    end_of_game(number_of_tries)


if __name__ == '__main__':
    guess_the_number()
    sys.exit(0)
