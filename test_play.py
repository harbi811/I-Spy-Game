from io import StringIO

import pytest

import play
from categories import Categories


# setting up test data using fixtures
# will be used as a parameter more than once
@pytest.fixture
def test_data():
    test_chosen_category = vars(Categories())["fruits"]

    return test_chosen_category


def test_choose_category(monkeypatch, test_data):
    user_input = StringIO("fruits\n")

    # how to mock user input through monkeypatching
    # https://holgerkrekel.net/2009/03/03/monkeypatching-in-unit-tests-done-right/
    # https://gist.github.com/GenevieveBuckley/efd16862de9e2fe7adfd2bf2bef93e02
    # https://pavolkutaj.medium.com/simulating-single-and-multiple-inputs-using-pytest-and-monkeypatch-6968274f7eb9

    monkeypatch.setattr("sys.stdin", user_input)

    # calling function being tested
    chosen_category, category_name = play.choose_category()

    # is it the expected dictionary
    assert chosen_category == test_data

    # check if chosen_category returns a dict and category_name is a string
    assert isinstance(chosen_category, dict)


def test_choose_letter_word(test_data):
    secret_letter, secret_word = play.choose_letter_word(test_data)

    assert isinstance(secret_letter, str)
    assert isinstance(secret_word, str)
    assert len(secret_letter) == 1
    assert len(secret_word) > 1


# allows one to define multiple sets of arguments and fixtures at the test function
# list parameters as a string and their corresponding values in tuples within a list
@pytest.mark.parametrize(
    "category_name, chosen_category,secret_letter, secret_word",
    [
        (
            "fruits",
            {
                "a": [
                    "apple",
                    "apricot",
                    "avocado",
                    "ackee",
                    "acai",
                    "abiu",
                    "ambarella",
                ],
                "b": ["banana", "blackberry", "blueberry", "boysenberry", "bilberry"],
                "c": ["cherry", "coconut", "clementine", "cantaloupe", "cranberry"],
            },
            "b",
            "blackberry",
        ),
        (
            "animals",
            {
                "a": ["aardvark", "antelope", "alpaca", "anaconda", "anteater"],
                "b": ["bear", "buffalo", "bat", "beaver", "baboon"],
                "c": [
                    "cat",
                    "crocodile",
                    "chimpanzee",
                    "camel",
                    "crab",
                    "cockroach",
                    "capybara",
                ],
            },
            "c",
            "cat",
        ),
    ],
)
def test_computer_play(
    category_name, chosen_category, secret_letter, secret_word, capsys, monkeypatch
):
    # mock guess by the player
    user_guess = "blackberry"
    monkeypatch.setattr("builtins.input", lambda _: user_guess)
    # monkeypatch.setattr("sys.stdin", user_guess), raises AttributeError: 'str' object has no attribute 'readline'

    # call computer_play function
    play.computer_play(category_name, chosen_category, secret_letter, secret_word)

    # what to test in the function - printed statements?
    # using capsys
    # During test execution any output sent to stdout and stderr is captured
    # Only writes to Python files sys.stdout and sys.stderr will be captured
    captured_statements = capsys.readouterr()
    # statements in captured_statements.out and captured_statements.err

    assert (
        f"I spy with my little eye a(n) {category_name[:-1]} that begins with the letter {secret_letter}"
        in captured_statements.out
    )

    if user_guess != "blackberry":
        assert "You have made too many guesses" in captured_statements.out
        assert f"My word was {secret_word}" in captured_statements.out
    else:
        # assert "Yes, you are correct" in captured_statements.out
        assert f"Your word must begin with {secret_letter}"

    # how to cater for multiple guesses - does monkeypatch take care of this
    # how to test number of guesses and clues?


# test get_user_starting_letter
def test_get_user_starting_letter(test_data, monkeypatch, capsys):
    user_letter = "a"
    monkeypatch.setattr("builtins.input", lambda _: user_letter)
    # underscore as a variable name is usually a name for an ignored variable

    user_starting_letter = play.get_user_starting_letter(test_data)

    captured_statements = capsys.readouterr()

    assert user_starting_letter == "a"

    if user_letter not in test_data.keys():
        assert (
            f"My database does not have words that begin with {user_starting_letter}"
            in captured_statements.out
        )
        assert "Please choose another letter" in captured_statements.out
    else:
        # no statement is printed when function is successful
        pass


# test computer_guess_words
# mock scenarios where success == True, success == False
# mock where all words are used up


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
                    "acai",
                    "abiu",
                    "ambarella",
                ],
                "b": ["banana", "blackberry", "blueberry", "boysenberry", "bilberry"],
            },
            "a",
            ["apple", "ackee", "acai"],
            True,
        ),
        (
            {
                "a": [
                    "apple",
                    "apricot",
                    "avocado",
                    "ackee",
                    "acai",
                    "abiu",
                    "ambarella",
                ],
                "b": ["banana", "blackberry", "blueberry", "boysenberry", "bilberry"],
            },
            "b",
            ["blueberry", "boysenberry"],
            False,
        ),
    ],
)
def test_computer_guess_word(
    chosen_category,
    user_starting_letter,
    used_words,
    expected_bool,
    monkeypatch,
    capsys,
):
    # mock user response - yes or no
    user_input = "yes"
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    success = play.computer_guess_word(
        chosen_category, user_starting_letter, used_words
    )

    captured_statements = capsys.readouterr()

    if success == expected_bool:
        assert "Hooray, I made the right guess in" in captured_statements.out
    else:
        assert "Apologies, I am unable to guess your word" in captured_statements.out

        # how about I am out of words


# test user_provide_word


def test_user_provide_word(monkeypatch, capsys):
    # mock user word
    user_input = "banana"
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    user_starting_letter = "b"
    user_words = []

    play.user_provide_word(user_starting_letter, user_words)

    captured_statements = capsys.readouterr()

    assert "What was your word?" in captured_statements.out
    assert "Your secret word must begin with  the letter" not in captured_statements.out


# test function for user_play
# test inner logic too


def test_user_play(capsys, test_data, monkeypatch):
    # mock user input because this function requires starting letter
    user_starting_letter = "a"
    monkeypatch.setattr("builtins.input", lambda _: user_starting_letter)

    category_name = "fruits"
    chosen_category = test_data

    play.user_play(category_name, chosen_category)

    captured_statements = capsys.readouterr()

    assert "It is your turn to play" in captured_statements.out
    assert "to my guesses" in captured_statements.out
    assert "Is your word" in captured_statements.out
