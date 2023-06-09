# I spy game

# import modules
import time

import play


def display_intro():
    print(
        """In this game, each player is allowed a maximum of 5 guesses. You will
    be playing against the computer. Do not worry, I have access to a limited number
    of words. In the future, I will have access to all words of the English language"""
    )

    print()

    time.sleep(3)

    print(
        """In this game, you can choose between four categories. The categories
    available are "fruits", "places", and "animals". If you up to the challenge, choose
     "expert" """
    )


play_again = "yes"

display_intro()

while play_again == "yes" or play_again == "y":
    print()

    chosen_category, category_name = play.choose_category()

    # generate secret letter and word
    secret_letter, secret_word = play.choose_letter_word(chosen_category)

    # computer plays first
    play.computer_play(category_name, chosen_category, secret_letter, secret_word)

    # user continues to play the same category
    play.user_play(category_name, chosen_category)

    print()
    print("Do you want to play again? (yes or no)")
    print()
    play_again = input()
    print()
else:
    print("Thank you for playing with me")
