# I spy game

# import modules
import play
import time
import importlib
import random
import dictionaries

def displayIntro():

    print('''In this game, each player is allowed a maximum of 5 guesses. You will
    be playing against the computer. Do not worry, I have access to a limited number
    of words. In the future, I will have access to all words of the English language''')

    print()

    time.sleep(3)

    print('''In this game, you can choose between four categories. The categories
    available are "fruits", "places", and "animals". If you up to the challenge, choose
     "expert" ''')



playAgain = 'yes'

displayIntro()

while playAgain == 'yes' or playAgain == 'y':

    print()
    print("Which category would you like to play")
    dict_name = input().lower()

    chosenCategory = play.chooseCategory(dict_name)
    
    # generate secret letter
    secretLetter, secretWord = play.chooseLetterWord(chosenCategory)

    play.computerPlay(dict_name, chosenCategory, secretLetter, secretWord)

    # computer continues to play the same category
    play.userPlay(dict_name, chosenCategory)
    print()
    print('Do you want to play again? (yes or no)')
    print()
    playAgain = input()
    print()
else:
    print("Thank you for playing with me")
