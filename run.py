import random
from random_words import words


def display_title():
    title = [
        "┓┏┏┓┳┓┏┓┏┳┓┓┏┏┓┳┳┓┏┓┳┓",
        "┣┫┣┫┃┃┃┓ ┃ ┣┫┣ ┃┃┃┣┫┃┃",
        "┛┗┛┗┛┗┗┛ ┻ ┛┗┗┛┛ ┗┛┗┛┗",
        "======================"
    ]


def get_word():
    word = random.choice(words)
    return word.upper()


def intro():
    introduction = [

    ]


def play_game(word):
    word_completion = "_" * len(word)
    guess = False
    guess_letters = []
    guess_words = []
    steps = 6
    print(display_title)
    print(intro)
    print(display_hangman(steps))
    print(word_completion)
    print("\n")