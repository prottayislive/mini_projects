import random
from words import word_list
import string


def get_word(word):
    """Getting a word from wordlist in words.py"""
    word = random.choice(word_list)
    return word.upper()


def hangman():
    word = get_word(word_list)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    while len(word_letters) > 0:
        print('Used:', ''.join(used_letters))
        list_letters = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ''.join(list_letters))
        # getting input
        user_input = input('Guess a letter: ').upper()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
        elif user_input in used_letters:
            print('You already chose this letter')
        else:
            print('invalid character. Go again')
    print(f' Yes the word is {word}')


hangman()
