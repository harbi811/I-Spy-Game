import pytest

import play
from categories import Categories


# defining error class
class NoMoreInputs(Exception):
    "Raised when no more inputs are available"

    def __init__(self, message):
        self.message = message


# class for mocking user input and function output
class MockUserInterface:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def input(self, message=None):
        if len(self.inputs) > 0:
            return self.inputs.pop()
        else:
            raise NoMoreInputs("No more inputs provided")

    def output(self, message=None):
        self.outputs.append(message)


# setting up test data using fixtures
# will be used as a parameter more than once
@pytest.fixture
def test_data():
    test_chosen_category = vars(Categories())["fruits"]

    return test_chosen_category


# user provides correct category
def test_choose_category_correct_category(test_data):
    ui = MockUserInterface(inputs=["fruits"])

    chosen_category, category_name = play.choose_category(ui)

    assert chosen_category == test_data

    assert len(ui.outputs) == 1
    assert "Successfully" in ui.outputs[0]


# user provides incorrect category
def test_choose_category_incorrect_category(test_data, capsys):
    ui = MockUserInterface(inputs=["bananas"])

    # asserting Exceptions
    with pytest.raises(NoMoreInputs) as exception_info:
        chosen_category, category_name = play.choose_category(ui)

        # no category is expected
        assert chosen_category == None

        # verify that exception was raised, function exception raised
        # if exception in test is raised
        assert "I am sorry" in ui.output[0]
        assert "Please choose one of these categories" in ui.output[0]
        assert "Enter the name of your category" in ui.output[0]

    assert exception_info.type == NoMoreInputs
    assert "No more inputs provided" in str(exception_info.value)


# test choose_letter_word
def test_choose_letter_word(test_data):
    secret_letter, secret_word = play.choose_letter_word(test_data)

    # both secret_word and secret_letter are strings
    assert isinstance(secret_letter, str)
    assert isinstance(secret_word, str)

    # secret_letter is one string
    assert len(secret_letter) == 1

    # secret-word is more than one letter long
    assert len(secret_word) > 1

    # first letter of secret_word
    assert secret_word[0] == secret_letter


# user makes correct guess
def test_computer_play_correct_guesses(test_data):
    # mock guesses by the player
    ui = MockUserInterface(inputs=["banana"])
    chosen_category = test_data
    secret_letter = "b"
    secret_word = "banana"
    category_name = "fruits"

    play.computer_play(
        ui, category_name, chosen_category, secret_letter, secret_word
    )

    assert (
        f"I spy with my little eye a(n) {category_name[:-1]} "
        f"that begins with the letter {secret_letter}" in ui.outputs[0]
    )
    assert "Yes, you are correct" in ui.outputs[1]


# a few incorrect guesses
def test_computer_play_few_incorrect_guesses(test_data):
    # mock guesses by the player
    ui = MockUserInterface(inputs=["cat", "blackberry", "beaver", "boot"])
    chosen_category = test_data
    secret_letter = "b"
    secret_word = "banana"
    category_name = "fruits"

    with pytest.raises(NoMoreInputs) as exception_info:
        play.computer_play(
            ui, category_name, chosen_category, secret_letter, secret_word
        )
        assert f"Your word must begin with {secret_letter}" in ui.outputs[0]
        assert "No, please try again" in ui.outputs[0]
        assert "The first letters of my word are" in ui.outputs[0]

    assert (
        f"I spy with my little eye a(n) {category_name[:-1]} that begins with "
        f"the letter {secret_letter}" in ui.outputs[0]
    )
    assert exception_info.type == NoMoreInputs
    assert "No more inputs provided" in str(exception_info.value)


# wuth many incorrect guesses
def test_computer_play_many_incorrect_guesses(test_data):
    # mock guesses by the player
    ui = MockUserInterface(
        inputs=["cat", "blackberry", "beaver", "boot", "blank", "blue"]
    )
    chosen_category = test_data
    secret_letter = "b"
    secret_word = "banana"
    category_name = "fruits"

    play.computer_play(
        ui, category_name, chosen_category, secret_letter, secret_word
    )
    assert (
        f"I spy with my little eye a(n) {category_name[:-1]} that begins "
        f"with the letter {secret_letter}" in ui.outputs[0]
    )

    assert "No, please try again" in ui.outputs[1]
    assert "The first letters of my word are" in ui.outputs[2]

    assert "You have made too many guesses" in ui.outputs[-2]
    assert f"My word was {secret_word}" in ui.outputs[-1]


# test get_user_starting_letter
def test_get_user_starting_letter_available_key(test_data):
    ui = MockUserInterface(inputs=["a"])

    user_starting_letter = play.get_user_starting_letter(ui, test_data)

    assert user_starting_letter == "a"


def test_get_user_starting_letter_few_unavailable_keys(test_data):
    ui = MockUserInterface(inputs=["x", "x"])
    chosen_category = test_data

    with pytest.raises(NoMoreInputs) as exception_info:
        user_starting_letter = play.get_user_starting_letter(
            ui, chosen_category
        )

        assert (
            "My database does not have words that begin with" in ui.outputs[0]
        )
        assert "Please choose another letter" in ui.outputs[0]
    assert exception_info.type == NoMoreInputs
    assert "No more inputs provided" in str(exception_info.value)


def test_get_user_starting_letter_many_unavailable_keys(test_data):
    ui = MockUserInterface(inputs=["x", "x", "x", "x"])
    chosen_category = test_data

    user_starting_letter = play.get_user_starting_letter(ui, chosen_category)

    assert "My database does not have words that begin with" in ui.outputs[0]
    assert "Please choose another letter" in ui.outputs[1]

    assert (
        "You have entered an unavailable letter too many times"
        in ui.outputs[-1]
    )


# test computer_guess_words, returns boolean
# mock scenarios where
# makes correct guess
# runs out of words


@pytest.mark.parametrize(
    "chosen_category, user_starting_letter, used_words, expected_bool",
    [
        (
            {
                "a": [
                    "apple",
                    "apricot",
                    "avocado",
                    "ackee",
                    "ackee",
                    "acai",
                    "abiu",
                    "ambarella",
                ],
                "b": ["banana", "blackberry", "blueberry"],
            },
            "a",
            ["apple"],
            True,
        ),
        (
            {
                "a": ["apple", "apricot", "avocado"],
                "b": ["banana", "blackberry", "blueberry"],
            },
            "b",
            ["banana", "blackberry", "blueberry"],
            False,
        ),
    ],
)
def test_computer_guess_word(
    chosen_category, user_starting_letter, used_words, expected_bool
):
    # mock user response - yes or no
    ui = MockUserInterface(inputs=["yes"])

    success = play.computer_guess_word(
        ui, chosen_category, user_starting_letter, used_words
    )

    if success == True:
        assert "Is your secret word" in ui.outputs[0]
        assert "Hooray, I made the right guess in" in ui.outputs[1]
    else:
        assert "I am out of words" in ui.outputs[0]


# test_computer_guess_word - runs out of guesses
def test_computer_guess_word_many_guesses(test_data):
    mock_input = ["no"] * 6
    ui = MockUserInterface(inputs=mock_input)

    chosen_category = test_data
    user_starting_letter = "a"
    used_words = []

    success = play.computer_guess_word(
        ui, chosen_category, user_starting_letter, used_words
    )

    assert success == False
    assert "Is your secret word" in ui.outputs[0]
    assert "Apologies, I am unable to guess your word" in ui.outputs[-1]


# test user_provide_word
# def test_user_provide_word_correct_word(ui, user_starting_letter,
#                                                        user_words):
#     # mock user word
#     ui = MockUserInterface(inputs=["banana"])
#     user_starting_letter = "b"
#     user_words = []

#     play.user_provide_word(ui, user_starting_letter, user_words)
#     assert "What was your word" in ui.outputs[1]
# assert "Your secret word must begin with the letter" in ui.outputs[-1]


# test_user_play function
def test_user_play(test_data):
    # input for different functions
    mock_input = ["a", "yes"][::-1]  # reverse list
    ui = MockUserInterface(inputs=mock_input)

    category_name = "fruits"
    chosen_category = test_data

    play.user_play(ui, category_name, chosen_category)
    assert "It is your turn to play" in ui.outputs[0]
    assert "Is your secret word" in ui.outputs[2]
    assert "Hooray" in ui.outputs[-1]
