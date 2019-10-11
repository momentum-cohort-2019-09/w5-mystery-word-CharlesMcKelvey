import random
import re
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
letters = 'abcdefghijklmnopqrstuvwxyz'


def demon_game():
    # Run all of the logic here
    game_over = False
    letters_guessed = []  # Key will be letters guessed, value will be word_list
    difficulty = set_difficulty(input(
        'What kind of adventure would you like? You may choose "easy", "medium", or "hard".').lower())
    word_list = get_Word_List(difficulty)
    while not game_over:
        guessed_letter = input('Give us a guess:   ').lower()
        word_list = filter_word_list(word_list, guessed_letter)


def set_difficulty(choice):
    """ Allowing the player to set the difficulty of the game (easy, medium, hard) """
    if choice == 'easy':
        return choice
    elif choice == 'medium':
        return choice
    elif choice == 'hard':
        return choice
    else:
        return set_difficulty(input('Type "easy", "medium", and "hard"').lower())


def get_Word_List(difficulty):
    """ Grab the initial word list dependent upon the difficulty of the word """
    if difficulty == 'easy':
        with open('words.txt') as file_words:
            words = file_words.read().splitlines().lower()
            word_list = []
            for word in words:
                if 4 <= len(word) <= 10:
                    word_list.append(word)
            return word_list
    elif difficulty == 'medium':
        with open('words.txt') as file_words:
            words = file_words.read().splitlines().lower()
            word_list = []
            for word in words:
                if 10 <= len(word) <= 16:
                    word_list.append(word)
            return word_list
    elif difficulty == 'hard':
        with open('words.txt') as file_words:
            words = file_words.read().splitlines().lower()
            word_list = []
            for word in words:
                if 16 <= len(word) <= 24:
                    word_list.append(word)
            return word_list


def filter_word_list(word_list, letter_guessed):
    """ Filter down the word list and, dependent upon what the guessed word  """
    # Given the word_list that is available, check each position where the guessed letter could be,
    #  saving each list of words to a list and then comparing length when you've fully combed through
    lists = []
    for word in word_list:
        list = []
        if letter_guessed in word:
            pass
    # RegEx fun!
    re.match(/(letter_guessed)/)
    return word_list

# ---------- Start ---------------
# demon_game()
