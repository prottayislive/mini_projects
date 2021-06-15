import random
from words import word_list
import string


def get_word(word):
    """Getting a word from wordlist in words.py"""
    word = random.choice(word_list)
    return word.upper()


def hangman():
    lives = 6
    word = get_word(word_list)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    while len(word_letters) > 0 and lives > 0:
        print(f'You have {lives} left')
        print('Used:', ''.join(used_letters))
        list_letters = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ''.join(list_letters))
        # getting input
        user_input = input('Guess a letter: ').upper()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives = lives - 1
                print('letter is not in word')
        elif user_input in used_letters:
            print('You already chose this letter')
        else:
            print('invalid character. Go again')
    if lives == 0:
        print(f'You died! The word was {word}')
    else:
        print(f' Congratulations! The word is {word}!')


hangman()
