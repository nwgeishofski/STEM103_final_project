import random

# define hangman class
class Hangman:
    def __init__(self, selected_word):
        self.winning_word = selected_word
        self.guessed_letters = []
        self.body_parts = ["Head", "Torso", "r_arm", "l_arm", "r_leg", "l_leg", "shoes"]
        self.body_parts_drawn = 0

# function add parts to "drawing"
    def add_drawn_part(self):
        self.body_parts_drawn += 1

# function check if game is lost
    def game_lost(self):
        return self.body_parts_drawn >= len(self.body_parts)

# function check if game is won
    def game_won(self):
        for letter in self.winning_word:
            if letter not in self.guessed_letters:
                return False
        return True
    
# function display current word progress
    def display_word_progress(self):
        display_word = []
        for letter in self.winning_word:
            if letter in self.guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")
        print (" ".join(display_word))


            