# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
from re import sub

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    max_guesses = 6
    max_warnings = 3

    word_length = len(secret_word)
    word_length_unique = len(set(secret_word))

    available_letters = "abcdefghijklmnopqrstuvwxyz"

    guessed_word = secret_word
    guessed_word_underscored = "_" * len(secret_word)

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", word_length, "letters long.")
    print("You have", max_warnings, "warnings left.")

    remaining = max_guesses
    warnings = max_warnings
    while remaining > 0:
        pluralized = "guess"
        if remaining > 1:
            pluralized = "guesses"

        print("-------------")
        print("You have", remaining, "guesses left.")
        print("Available letters:", available_letters)

        guess = input("Please guess a letter: ").lower()

        if not guess.isalpha():
            warnings -= 1
            print(
                "Oops! That is not a valid letter. You have",
                warnings,
                "warnings left:",
                guessed_word_underscored.lower(),
            )
            continue

        if available_letters.find(guess) == -1:
            if warnings <= 0:
                print(
                    "Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",
                    guessed_word_underscored.lower(),
                )
                remaining -= 1
                continue
            else:
                warnings -= 1
                print(
                    "Oops! You've already guessed that letter. You have",
                    warnings,
                    "warnings left:",
                    guessed_word_underscored.lower(),
                )
                continue

        position = guessed_word.find(guess)
        if position > -1:
            for l in range(0, len(guessed_word)):
                if guessed_word[l] == guess:
                    guessed_word = (
                        guessed_word[:l]
                        + guessed_word[l].upper()
                        + guessed_word[l + 1 :]
                    )
            guessed_word_underscored = sub("[a-z]", "_", guessed_word)
            print("Good guess:", guessed_word_underscored.lower())

            # Check if full word has been guessed
            if guessed_word_underscored.lower() == secret_word:
                score = remaining * word_length_unique
                print("Congratulations, you won!")
                print("Your total score for this game is:", score)
                exit()
        else:
            if guess in "aeiou":
                # Vowels lose two
                remaining -= 2
            else:
                remaining -= 1
            print(
                "Oops! That letter is not in my word:", guessed_word_underscored.lower()
            )

        # Remove from available letters
        available_position = available_letters.find(guess)
        available_letters = (
            available_letters[:available_position]
            + available_letters[available_position + 1 :]
        )

    print("-----------")
    print("Sorry, you ran out of guesses. The word was:", secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """

    if len(my_word) != len(other_word):
        return False

    # Check if repeat values haven't been found
    if len(set(my_word)) != len(set(other_word)):
        return False

    ok = True
    for n in range(0, len(my_word)):
        if my_word[n] == "_":
            continue
        if my_word[n] != other_word[n]:
            ok = False
            break

    return ok


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    print(match_with_gaps("te_t", "tact"))  # False
    print(match_with_gaps("a__le", "banana"))  # False
    print(match_with_gaps("a__le", "apple"))  # True
    print(match_with_gaps("a_ple", "apple"))  # False

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)
