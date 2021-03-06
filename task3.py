# HANGMAN by Norbert Kupeczki

import sys
import random


list_of_words = ["snake",
                 "python",
                 "amiga",
                 "terminator",
                 "mandalorian",
                 "playstation",
                 "nintendo",
                 "controller",
                 "console",
                 "witcher",
                 "atari",
                 "cyberpunk",
                 "roleplay",
                 "commodore",
                 "hangman",
                 "arcade",
                 "cartridge",
                 "mario",
                 "programmer",
                 "gamer"]


# Return a random word from a list of words and casts it to upper()
def get_random_word():
    return list_of_words[random.randrange(0, len(list_of_words))].upper()


# Draw the hangman. The graphics and text changes based on lives left
def draw_hangman(lives_left):
    print(" _____")
    print(" |   |", end="")
    if not game_is_over:
        print(f"   Lives left: {lives_left}")
    else:
        print("")
    if lives_left > 5:
        print(" |")
    else:
        print(" |   O")
    if lives_left > 4:
        print(" |")
    elif lives_left > 3:
        print(" |   |")
    elif lives_left > 2:
        print(" |  /|")
    else:
        print(" |  /|\\")
    if lives_left > 1:
        print(" |")
    elif lives_left > 0:
        print(" |  /")
    else:
        print(" |  / \\")
    print(" |")
    print("_|_____")
    print("^" * 7)
    if not game_is_over:
        print("Your word:", end=" ")
        print(''.join(player_word))
        print("Used letters:", end=" ")
        print(', '.join(used_letters))


# Fills the player_word list with underscores equal to the length of the secret word
def init_player_word(word):
    for i in range(len(word)):
        player_word.append("_")


# Searches the secret word for the letters guessed, and updates the player_word based on matches
# If the input is more than 1 character long, it checks the whole secret word for match
def search_in_secret_word(guess):
    element = 0
    match = False
    is_new = False

    # Checks the used letters list and asks new input if the player uses an already used letter
    while not is_new and used_letters:
        if guess in used_letters:
            guess = input("> You already tried this, try something else:").upper()
        else:
            is_new = True

    # If there is a match, updates the player_word based on the index where the match was in the secret word
    if len(guess) == 1:
        for i in secret_word:
            if i == guess:
                match = True
                player_word[element] = guess
            element += 1
        used_letters.append(guess)
    else:
        if guess == secret_word:
            player_word[:len(guess)] = guess
            match = True
        else:
            print("Sorry, this is not the correct word!")

    if not match:
        return 1
    else:
        return 0


# Check game conditions
def check_conditions():
    if lives == 0:
        print("\nGAME OVER")
        print(f"The correct word was: {secret_word}")
        return True
    elif secret_word == ''.join(player_word):
        print("\nCONGRATULATIONS, YOU WON!")
        return True
    else:
        return False


def play_again():
    again = input("Do you want to play again? (Y/N)").upper()
    while not (again == "Y" or again == "N"):
        again = input("Do you want to play again? (Y/N)").upper()

    if again == "Y":
        return True
    else:
        print("\n" + "=" * 27)
        print("Thank you for playing, bye!")
        print("=" * 27)
        return False


if __name__ == '__main__':
    playing = True

    while playing:
        print("\n" + "=" * 18)
        print("Welcome to HANGMAN")
        print("=" * 18)
        random.seed()

        lives = 6
        game_is_over = False
        secret_word = get_random_word().upper()
        player_word = []
        init_player_word(secret_word)
        used_letters = []
        draw_hangman(lives)

        while not game_is_over:

            player_input = input("> Please choose a letter, or guess the word:").upper()

            lives -= search_in_secret_word(player_input)

            game_is_over = check_conditions()

            draw_hangman(lives)

        playing = play_again()

    sys.exit(0)
