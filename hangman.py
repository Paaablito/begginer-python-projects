import random

from words import wordss
import string

def get_valid_word(wordss):
    word = random.choice(wordss)
    while '-' in word or ' ' in word:
        word = random.choice(wordss)

    return word.upper()



def hangman():
    word = get_valid_word(wordss)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        print('You have ', lives, 'Left. You have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1
                print('You have written a wrong number')

        elif user_letter in used_letters:
            print('You have already used that character, Please try again.')

        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print('You died!')
    else:
        print("You win! The word is ", word)

hangman()
