import random
from functions import *
from hangmanclass import Hangman


# create word_list and play_again
word_list = ["hangman", "python", "washington", "everett", "snorlax", "bulbasaur"]
play_again = "y"

# in outer while loop

while play_again == "y":
    print("**********HANGPERSON**********")
    # select word
    winning_word = choose_word(word_list)
    
    # instantiate a hangman with word
    game = Hangman(winning_word)

    # inner while loop
    while not game.game_won() and not game.game_lost():

         # display output
        game.display_word_progress()
        print ("Guessed letters: ", game.guessed_letters)
        print ("body parts drawn: ", game.body_parts[:game.body_parts_drawn])

        # get guess
        guess = get_guess()

        # validate guess

        if guess in game.guessed_letters:
            print("That letter has already been guessed. ")
        else:
            game.guessed_letters.append(guess)

            if guess in game.winning_word:
                print("Correct guess!")
                print("\n")
            else:
                print("Incorrect guess!")
                game.add_drawn_part()

    # check if game is won
    if game.game_won():
         print("Congratulations, you win!")

    # check if game is lost
    if game.game_lost():
        print("You've lost!")
        print("The word was: " + game.winning_word)

    play_again = ask_play_again()
# end of game message

print("Thanks for playing.")

