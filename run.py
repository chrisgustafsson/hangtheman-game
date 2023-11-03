import random
from random_words import words


def display_title():
    title = [
        "┓┏┏┓┳┓┏┓┏┳┓┓┏┏┓┳┳┓┏┓┳┓",
        "┣┫┣┫┃┃┃┓ ┃ ┣┫┣ ┃┃┃┣┫┃┃",
        "┛┗┛┗┛┗┗┛ ┻ ┛┗┗┛┛ ┗┛┗┛┗",
        "======================"]


def get_word():
    word = random.choice(words)
    return word.upper()


def intro():
    introduction = [
        "Welcome to a classic game of Hangman!",
        "No difference in rules even though the name difference.",
        "In Swedish (creators main language) it is called hang the man.",
        "Hence where the game got it's name. Just guess a letter to start",
        "The aim is to find the word before you are hung!"]


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
    while not guess and steps > 0:
        guesses = input("Make a guess of a letter or word:\n").upper()
        if len(guesses) == 1 and guesses.isalpha():
            if guesses in guess_letters:
                print("You already guessed this letter silly", guesses)
            elif guesses not in word:
                print(guesses, "This letter is not in the word. Try again!")
                steps -= 1
                guess_letters.append(guesses)
            else:
                print("Amazing, well done", guesses, "is there!")
                guess_letters.append(guesses)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guesses]
                for index in indices:
                    word_as_list[index] = guesses
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guess = True      
        elif len(guesses) == len(word) and guesses.isalpha():
            if guesses in guess_words:
                print("You already guessed the word silly", guesses)
            elif guesses != word:
                print(guesses, "is not the word we look for!")
                steps -= 1
                guess_words.append(guesses)
            else:
                guess = True
                word_completion = word
        else:
            print("Invalid input, please guess a letter or word.")
            print(display_hangman(steps))
            print(word_completion)
            print("\n")


def display_hangman(steps):
    stages = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="
    ]
    return stages[steps]


def main():
    word = get_word()
    play_game(word)
    while input ("Would you like to play again? (yes/no) ").upper() == "YES":
        word = get_word()
        play_game(word)


if __name__ == "__main__":
    main()