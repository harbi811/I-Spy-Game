import random
import time

from categories import Categories
from formatting import Colour

# import word category when specified by the user
# user chooses to play fruits, animal or places or random_words


def choose_category():
    chosen_category = None

    # request user to enter category until no exception
    while chosen_category is None:
        category_name = input("Enter the name of your category: ").lower()

        try:
            cat_dicts = vars(Categories())
            chosen_category = cat_dicts[category_name]

        except KeyError:
            print(
                f"{Colour.yellow} I am sorry, {category_name} is not available \n Please choose one of these categories, {list(cat_dicts.keys())}\n {Colour.end}"
            )

    print(f"{Colour.green} Successfully imported {category_name} category {Colour.end}")
    return chosen_category, category_name


# choose letter and word from chosen_category
def choose_letter_word(chosen_category):
    starting_letter = random.choice(list(chosen_category.keys()))
    word = random.choice(chosen_category[starting_letter])

    return starting_letter, word


# function for the user to guess the computer's word
def computer_play(category_name, chosen_category, secret_letter, secret_word):
    time.sleep(2)

    print()
    if category_name != "expert":
        print(
            f"I spy with my little eye a(n) {category_name[:-1]} that begins with the letter {secret_letter}"
        )
    else:
        print(
            f"I spy with my little eye an object that begins with the letter {secret_letter}"
        )

    print()

    user_guesses = 0
    clues = 2
    max_clues = len(secret_word) // 2 + 1

    while user_guesses <= 5:
        player_input = input("Enter your guess: ")
        print()

        user_guesses += 1

        # test the first letter of user input
        if player_input[0].lower() != secret_letter:
            print(
                f"{Colour.red} Your word must begin with {secret_letter} {Colour.end}"
            )

        # provide clues to the player after 2 fails
        elif player_input != secret_word:
            print(f"{Colour.blue} No, please try again {Colour.end}")
            print()

            if clues < max_clues:
                print(
                    f"{Colour.cyan} The first letters of my word are {secret_word[:clues]} {Colour.end}"
                )
                clues += 1
            else:
                print(
                    f"{Colour.cyan} The first letters of my word are {secret_word[:clues]} \n My word also ends with {secret_word[-1]} {Colour.end}"
                )

        else:
            print(f"{Colour.green} Yes, you are correct {Colour.end}")

            # break out of while loop if the player does not all available guesses
            break
    else:
        print(f"{Colour.red} You have made too many guesses {Colour.end}")
        print(f"{Colour.bold} My word was {secret_word} {Colour.end}")


# Function to get the user's starting letter
def get_user_starting_letter(chosen_category):
    unavailable_key = 0
    keys_available = list(chosen_category.keys())

    while unavailable_key <= 3:
        user_starting_letter = input("Enter the first letter of your word: ").lower()

        if user_starting_letter in keys_available:
            return user_starting_letter
        else:
            unavailable_key += 1
            print()
            print(
                f"My database does not have words that begin with {user_starting_letter}"
            )
            print(f"Please choose another letter")

    print(f"You have entered an unavailable letter too many times")


# Function for the computer to make guesses
def computer_guess_word(chosen_category, user_starting_letter, used_words):
    computer_guesses = 0
    words_available = chosen_category[user_starting_letter]

    while computer_guesses <= 5:
        computer_guesses += 1
        new_words_available = list(set(words_available) - set(used_words))

        if len(new_words_available) < 1:
            print(f"{Colour.cyan} I am out of words {Colour.end}")
            break
        else:
            word_guess = random.choice(new_words_available)
            used_words.append(word_guess)

        print(f"Is your secret word {str(word_guess)} ?")
        time.sleep(2)
        user_response = input().lower()

        if user_response == "yes" or user_response == "y":
            print(
                f"{Colour.green} Hooray, I made the right guess in {str(computer_guesses)} attempt(s) {Colour.end}"
            )
            return True

    print(f"{Colour.cyan} Apologies, I am unable to guess your word {Colour.end}")
    return False


# Function for the user to provide their word
def user_provide_word(user_starting_letter, user_words):
    while True:
        print(f"{Colour.cyan} What was your word? {Colour.end}")
        user_word = input().lower()

        if user_word[0] == user_starting_letter:
            user_words.append(user_word)
            break
        else:
            print(
                f"{Colour.red} Your secret word must begin with the letter {user_starting_letter} you specified earlier {Colour.end}"
            )


# main function to control the user's turn
def user_play(category_name, chosen_category, user_words=[]):
    # user_words list is for words the computer fails to guess and are provided by the user
    # if the user continues to play, this list of words should be available and appended to

    print()

    if category_name != "expert":
        print(
            f"It is your turn to play. Please type in the first letter of your secret {category_name[:-1]}"
        )
    else:
        print(
            f"It is your turn to play. Please type in the first letter of your secret object"
        )

    print('Type "yes / y" or "no / n" to my guesses')
    print()

    # a character is returned here
    user_starting_letter = get_user_starting_letter(chosen_category)

    used_words = []

    # this is a Boolean
    success = computer_guess_word(chosen_category, user_starting_letter, used_words)
    if not success:
        user_provide_word(user_starting_letter, user_words)
    else:
        # all possible occurrences have been handled in the functions above
        pass
