import random

# function choose word
def choose_word(word_list):
    selected_word = random.choice(word_list)
    return selected_word
    

# function get guess
def get_guess():
    while True:
        current_guess = input("Please guess a letter: ")
        current_guess = current_guess.lower()
        if len(current_guess) != 1:
            current_guess = input(("Please guess a single letter: "))
        elif not current_guess.isalpha():
            current_guess = input("Please enter a valid letter: ")
        else:
            return current_guess


# function display guessed letters
def display_guessed_letters(guessed_letters):
    print ("Guessed letters: "), guessed_letters()

# function ask if playing again
def ask_play_again():
    play_again = input("Would you like to play again? (y/n) ")
    return play_again