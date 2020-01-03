"""
Games can help you kill time when you’re bored - and here we don’t
mean smartphone games, but the classic paper-and-pencil ones.
However, we aren’t inviting you to kill time: on the contrary, we
offer to write a game and improve your programming skills. In this
project, you will work on the Hangman, a game where the player is
supposed to guess a word letter by letter. Make a program that plays
Hangman with you - and good luck with the guessing!
"""

import random
import string

print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(words)
mask = list('-' * len(random_word))

attempts = 8
typed = []

while True:
    command = input('Type "play" to play the game, "exit" to quit: ')

    if command == 'exit':
        break
    elif command == 'play':
        while True:
            if ''.join(mask) == random_word:
                print('You guessed the word!\nYou survived!\n')
                break

            if attempts == 0:
                print('You are hanged!\n')
                break

            print('\n' + ''.join(mask))
            letter = input('Input a letter:')

            if len(letter) != 1:
                print('You should print a single letter')
                continue

            if letter not in string.ascii_lowercase:
                print('It is not an ASCII lowercase letter')
                continue

            if letter in typed:
                print('You already typed this letter')
                continue

            typed.append(letter)
            indexes = [i for i in range(len(random_word)) if letter == random_word[i]]
            if indexes:
                for i in indexes:
                    mask[i] = random_word[i]
            else:
                print('No such letter in the word')
                attempts -= 1
