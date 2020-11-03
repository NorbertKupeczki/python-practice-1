# HANGMAN

import sys
import random


def get_random_word():
    return list_of_words[random.randrange(0, len(list_of_words))]


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


def init_player_word(word):
    for i in range(len(word)):
        player_word.append("_")


def search_in_secret_word(char):
    element = 0
    match = False
    for i in secret_word:
        if i == char:
            match = True
            player_word[element] = char
        element += 1
    used_letters.append(char)
    if not match:
        return False
    else:
        return True


def check_conditions():
    if lives == 0:
        print("\nGAME OVER")
        return True
    elif secret_word == ''.join(player_word):
        print("\nCONGRATULATIONS, YOU WON!")
        return True
    else:
        return False


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

if __name__ == '__main__':
    print("=" * 18)
    print("Welcome to HANGMAN")
    print("=" * 18)
    random.seed()

    lives = 6
    game_is_over = False
    secret_word = get_random_word()
    # print(secret_word)
    player_word = []
    used_letters = []
    init_player_word(secret_word)

    draw_hangman(lives)

    while not game_is_over:

        player_input = input("> Please chose a letter:")

        match_found = search_in_secret_word(player_input)

        if not match_found:
            lives -= 1

        game_is_over = check_conditions()
        draw_hangman(lives)

    sys.exit(0)
