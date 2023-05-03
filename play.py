import time
import random
from categories import Categories

# import word category when specified by the user
# user chooses to play fruits, animal or places or random_words

def chooseCategory(dict_name):   
    try:
        
        cat_dicts = vars(Categories())
        chosenCategory = cat_dicts[dict_name]
        
    except KeyError:
        print(f"I am sorry, {dict_name} is not available")
        return None

    else:    
        print(f"Successfully imported {dict_name} category")
        return chosenCategory
    

# choose letter and word from chosen user_category
def chooseLetterWord(chosenCategory): 

    startingLetter = random.choice(list(chosenCategory.keys()))
    word = random.choice(chosenCategory[startingLetter])

    return startingLetter, word


# function for the user to guess the computer's word

def computerPlay(dict_name, chosenCategory, secretLetter, secretWord):

    time.sleep(2)

    # get user input
    print()
    if dict_name == "fruits":
        print(f"I spy with my little eye a fruit that begins with the letter {secretLetter}")
    elif dict_name == "animals":
        print(f"I spy with my little eye an animal that begins with the letter {secretLetter}")
    elif dict_name == "places":
        print(f"I spy with my little eye a place that begins with the letter {secretLetter}")
    elif dict_name == "expert":
        print(f"I spy with my little eye an object that begins with the letter {secretLetter}")

    print()

    userGuesses = 0

    while userGuesses <= 5:
        
        playerInput = input()
        
        userGuesses += 1

        # test first letter of user input
        if playerInput[0] == secretLetter:

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



# function for the computer to guess the user's word

def userPlay(dict_name, chosenCategory):
    print()
    print('Please type "yes / y" or "no / n" to my guesses')

    if dict_name in ["fruits", "animals", "places"]:
        print(f"It is your turn to play, Please type in the first letter of your secret {dict_name}(s)")
    elif dict_name == "expert":
        print("It is your turn to play, Please type in the first letter of your secret word")

    print()

    userWords =[]

    computerGuesses = 0
    unavailableKey = 0

    # catch letters/keys that are not available in dictionary
    keys_available = list(chosenCategory.keys())
  

    while unavailableKey <= 3:
        userStartingLetter = input("Enter first letter of your word:  ").lower()
        
        if userStartingLetter in keys_available:
            words_available = chosenCategory[userStartingLetter] + userWords # improve so that computer can use words previously guessed by user

            while computerGuesses <= 5:

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

            break
        else:
            unavailableKey +=1

            print()
            print(f"Please choose another letter. My database of {dict_name} does not have words that begin {userStartingLetter}")
            print("Please choose another letter")

    else:
        print("You have entered the incorrect letter too many times")






