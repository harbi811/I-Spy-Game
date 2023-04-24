# I spy game

import random
import time

# word dictionary
words_dict = {
    'a': ['apple', 'ant', 'airplane', 'apricot', 'alligator', 'acorn', 'arrow'],
    'b': ['ball', 'banana', 'book', 'blue', 'bee', 'butterfly', 'bread'],
    'c': ['cat', 'cup', 'car', 'cake', 'camel', 'candy', 'candle'],
    'd': ['dog', 'duck', 'donut', 'dolphin', 'door', 'drum', 'dragon'],
    'e': ['egg', 'elephant', 'ear', 'eel', 'engine', 'elbow', 'earth'],
    'f': ['flower', 'fish', 'flag', 'fire', 'frog', 'fox', 'fan'],
    'g': ['grape', 'goose', 'goat', 'gift', 'giraffe', 'guitar', 'garlic'],
    'h': ['hat', 'hand', 'heart', 'hippo', 'horse', 'hamburger', 'helicopter'],
    'i': ['ice', 'igloo', 'island', 'insect', 'ice cream', 'iron', 'iguana'],
    'j': ['jacket', 'jam', 'jellyfish', 'jet', 'jeans', 'jester', 'jigsaw'],
    'k': ['kangaroo', 'kite', 'key', 'kiwi', 'king', 'koala', 'ketchup'],
    'l': ['lion', 'lemon', 'leaf', 'lollipop', 'lizard', 'lighthouse', 'lamb'],
    'm': ['monkey', 'moon', 'mouse', 'muffin', 'mountain', 'mushroom', 'motorcycle'],
    'n': ['nest', 'nose', 'nut', 'needle', 'necklace', 'night', 'net'],
    'o': ['orange', 'octopus', 'ocean', 'ostrich', 'owl', 'onion', 'olive'],
    'p': ['pig', 'pizza', 'pear', 'peacock', 'penguin', 'pencil', 'pumpkin'],
    'q': ['queen', 'quilt', 'quail', 'quartz', 'question', 'quiver', 'quiet'],
    'r': ['rabbit', 'rainbow', 'rose', 'robot', 'rhino', 'ring', 'rocket'],
    's': ['sun', 'snake', 'star', 'snowman', 'squirrel', 'spider', 'smile'],
    't': ['tree', 'tiger', 'trumpet', 'turtle', 'tomato', 'teapot', 'table'],
    'u': ['umbrella', 'unicorn', 'ukulele', 'under', 'up', 'uncle', 'usher'],
    'v': ['violin', 'van', 'vase', 'volcano', 'vegetable', 'vest', 'vacuum'],
    'w': ['watermelon', 'whale', 'wagon', 'wheel', 'worm', 'witch', 'window'],
    'x': ['xylophone', 'xylophone', 'x-ray', 'xenophobia', 'xanthan', 'xenon', 'xerography', 'xenarthra'],
    'y': ['yellow', 'yoyo', 'yacht', 'yak', 'yawn', 'yogurt', 'yo-yo'],
    'z': ['zebra', 'zoo', 'zealot', 'zipper', 'zucchini', 'zeppelin', 'zero', 'zesty']
    }

userWords = []

def displayIntro():
    print('''"I Spy" is a simple game where one person chooses a word and gives 
    a clue starting with "I spy with my little eye something that begins with...". 
    The other players take turns guessing the word based on the clue given for
    a given number of times until someone guesses correctly.''')

    time.sleep(4)

    print()

    print('''In this game, each player is allowed a maximum of 7 guesses. You will
    be playing against the computer. Do not worry, I have access to a limited number
    of words. In the future, I will have access to all words of the English language''')

    print()

    time.sleep(4)


def chooseLetterWord():

    letterIndex = random.randint(0, 25)
    startingLetter = list(words_dict.keys())[letterIndex]
    wordIndex =  random.randint(0, len(words_dict[startingLetter])-1)
    word = words_dict[startingLetter][wordIndex]

    return startingLetter, word



def computerPlay():

    # generate secret letter
    secretLetter, secretWord = chooseLetterWord()
    time.sleep(2)

    # get user input
    print()
    print("I spy with my little eye, something that begins with the letter", secretLetter)
    print()
    print("Please write the word in lower case characters")
    print()
    

    userGuesses = 0

    while userGuesses <= 7:
        
        playerInput = input()
        
        userGuesses += 1

        if playerInput[0] == secretLetter: # test first letter of user input

            if playerInput == secretWord: # improve so that 'computer' does not reuse the previous word
                print("Yes, you are correct")
                break
            else:
                print("No, please try again")
                print()

        else:
            print("Your word must begin with ", secretLetter)
    else:
        print("You have made too many guesses")
        print("My word was ", secretWord)


def userPlay():
    print()
    print("It is your turn to play, Please type in the first letter of your word")

    print()

    userStartingLetter = input()
    computerGuesses = 0
    words_available = words_dict[userStartingLetter] + userWords

    while computerGuesses <= 7:

        computerGuesses += 1

        usedWords = []


        wordGuess = None

        while wordGuess not in  usedWords:
            wordGuessIndex = random.randint(0, len(words_available)-1) # improve so that a previously guessed word is not returned, sample without replacement
            wordGuess = words_available[wordGuessIndex]
            usedWords.append(wordGuess)

        else:
            new_words_available = list(set(words_available) - set(usedWords))
            # new_words_available = [words_available[i] for i in availableIndices]
            wordGuessIndex = random.randint(0, len(new_words_available)-1) # think about situations where you are out of words, what happens?
            wordGuess = new_words_available[wordGuessIndex]
            usedWords.append(wordGuess)


        print('Is your secret word ' + str(wordGuess) + ' ?')
        time.sleep(2)
        print('Please type "yes / y" or "no / n"')
        userResponse  = input()  # rename this variable

        if userResponse == "yes" or userResponse == 'y':
            print("Hooray, I made the right guess in " + str(computerGuesses) + " attempt(s)") # do you want to refine this for number of attempts?
            

            break
        elif userResponse == "no" or userResponse == "n":
            pass

    else:
        print("Apologies, I am unable to guess your word")
        time.sleep(2)
        print("What was your word?")
        userWord = input()
        print("")
        userWords.append(userWord)



playAgain = 'yes'

displayIntro()

while playAgain == 'yes' or playAgain == 'y':

    computerPlay()
    userPlay()
    print()
    print('Do you want to play again? (yes or no)')
    print()
    playAgain = input()
    print()
else:
    print("Thank you for playing with me")
