import time
import random
from categories import Categories

# import word category when specified by the user
# user chooses to play fruits, animal or places or random_words

def chooseCategory():   
    
    exception_occurred = True
    while exception_occurred:
        dict_name = input("Enter the name of your category: ").lower()
        
        try:
            
            cat_dicts = vars(Categories())
            chosenCategory = cat_dicts[dict_name]

            exception_occurred = False
            
        except KeyError:
            print(f"I am sorry, {dict_name} is not available")
            print(f"Please choose one of these categories, {list(cat_dicts.keys())}\n")
            
            exception_occurred = True

        else:    
            print(f"Successfully imported {dict_name} category")
            return chosenCategory, dict_name
    

# choose letter and word from chosen user_category
def chooseLetterWord(chosenCategory): 

    startingLetter = random.choice(list(chosenCategory.keys()))
    word = random.choice(chosenCategory[startingLetter])

    return startingLetter, word


# function for the user to guess the computer's word

def computerPlay(dict_name, chosenCategory, secretLetter, secretWord):

    time.sleep(2)

    print()
    if dict_name != "expert":
        print(f"I spy with my little eye a(n) {dict_name[:-1]} that begins with the letter {secretLetter}")
    else:
        print(f"I spy with my little eye an object that begins with the letter {secretLetter}")

    print()

    userGuesses = 0
    clues = 1
    max_clues = len(secretWord)//2 + 1 

    while userGuesses <= 5: 
        
        playerInput = input("Enter your guess: ")
        print()
        
        userGuesses += 1

        # test first letter of user input
        if playerInput[0].lower() == secretLetter:

            # # provide clues to the play after 2 fails
            while playerInput != secretWord:
                print("No, please try again")
                print()
                
                if clues < max_clues:
                    print(f"The first letters of my word are {secretWord[:clues]}")
                    clues += 1

                    if clues == max_clues:
                        print(f"My word also ends with {secretWord[-1]}")
                break
            else:
                print("Yes, you are correct")
                break
        else:
            print("Your word must begin with ", secretLetter)
    else:
        print("You have made too many guesses")
        print("My word was ", secretWord)



# function for the computer to guess the user's word

def userPlay(dict_name, chosenCategory):
    print()
    print('Please type "yes / y" or "no / n" to my guesses')

    if dict_name != "expert":
        print(f"It is your turn to play, Please type in the first letter of your secret {dict_name[:-1]}")
    else:
        print("It is your turn to play, Please type in the first letter of your secret object")

    print()

    # if the user continues to play, this list of words should be available
    # so that computer can use words previously guessed by user
    global userWords
    userWords = []

    computerGuesses = 0
    unavailableKey = 0

    # used to catch letters/keys that are not available in dictionary
    keys_available = list(chosenCategory.keys())
  

    while unavailableKey <= 3:
        userStartingLetter = input("Enter first letter of your word:  ").lower()
        
        if userStartingLetter in keys_available:
            words_available = chosenCategory[userStartingLetter] + userWords 

            while computerGuesses <= 5:

                computerGuesses += 1

                usedWords = []

                new_words_available = list(set(words_available) - set(usedWords))

                wordGuessIndex = random.randint(0, len(new_words_available)-1) # think about situations where you are out of words, what happens?
                wordGuess = new_words_available[wordGuessIndex]
                usedWords.append(wordGuess)


                print('Is your secret word ' + str(wordGuess) + ' ?')
                time.sleep(2)
                
                userResponse  = input()  # rename this variable


                
            #     if userResponse == "yes" or userResponse == 'y':
            #         print("Hooray, I made the right guess in " + str(computerGuesses) + " attempt(s)") # do you want to refine this for number of attempts?  

            #         break
            #     else:
            #         pass

            # else:
            #     print("Apologies, I am unable to guess your word")
            #     time.sleep(2)
            #     print("What was your word?")
            #     userWord = input().lower()

            #     if userWord[0] != userResponse:
            #         print(f"You secret word must begin with the letter {userResponse} you specified earlier")

            #     else:
            #         userWords.append(userWord)   
            break
        else:
            unavailableKey +=1

            print()
            print(f"Please choose another letter. My database of {dict_name} does not have words that begin {userStartingLetter}")
            print("Please choose another letter")

    else:
        print("You have entered the incorrect letter too many times")






