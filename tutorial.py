import sys
import random

fortunes = ["Zombies eat brains, you're safe.",
            "Psst! They're being paid to love you",
            "Error 404: Fortune not found",
            "A conclusion is simply the place where you got tired of thinking",
            "You think it's a secret, but they know"]

def print_fortune():
    index = random.randrange(0, len(fortunes)) # Random number between 0 and the length of fortunes
    print("Your fortune is: " + fortunes[index])

def print_hello(name) :
    print(f"Greetings peasant {name}")

if __name__ == '__main__':
    random.seed()
    print("(\\(\\")
    print("(-.-)")
    print("o_(\")(\")")
    player_name = input("The fortune bunny asks for your name, peasant? Do speak up!\n")
    print_hello(player_name)
    print_fortune()

    sys.exit(0)
