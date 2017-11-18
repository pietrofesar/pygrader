""" hangman.py docstring
    Python 3.5 platform independent

    TODO:
      * modularize portions
      * clean up the exit process
      * divide modules into class assignments

    author: Rocco Pietrofesa
    date: 11/17/2017
"""
import os
import random

# text color constants
R = '\033[0;31m'  # red
BR = '\033[1;31m'  # bold red
G = '\033[0;32m'  # green
BG = '\033[1;32m'  # bold green
Y = '\033[0;33m'  # yellow
BY = '\033[1;33m'  # bold yellow
B = '\033[0;34m'  # blue
BB = '\033[1;34m'  # bold blue
P = '\033[0;35m'  # purple
BP = '\033[1;35m'  # bold purple
A = '\033[0;36m'  # aqua
BA = '\033[1;36m'  # bold aqua
X = '\033[0m'  # reset


def get_words(text_file):
    if os.path.isfile(text_file):
        # generate word list
        file = open(text_file, 'r')
        data = [each.strip().split(',') for each in file.read().split('\n')]
        # print(data)
        file.close()
        return data
    else:
        print('{}!ERROR! {}text file does not exist in working directory'.format(BR, X))


def set_secret(words):
    return words[random.randint(0, len(words) - 1)]


def get_guess(guessed):
    print('step1')
    while True:
        print('step2')
        letter = input('Guess a letter: ')
        print('step3')
        if letter in guessed:
            print('step4')
            pass
        if len(letter) != 1:
            print('step5')
            pass
        if not letter.isalpha():
            print('step6')
            pass
        else:
            print('step7')
            return letter
        del letter
    print('step8')


def set_pic(_turns):
    # hangman pics
    won = '|-----|\n|\n|    {}\\O/{}\n|     {}|{}\n-----{}/{}-{}\\{}'.format(BG, X, BG, X, BG, X, BG, X)
    turn_0 = '|-----|\n|     {}O{}\n|    {}/|\\{}\n|    {}/ \\{}\n--------'.format(BR, X, BR, X, BR, X)
    turn_1 = '|-----|\n|     {}O{}\n|    {}/|\\{}\n|    {}/{}\n--------'.format(BR, X, BR, X, BR, X)
    turn_2 = '|-----|\n|     {}O{}\n|    {}/|\\{}\n|\n--------'.format(BR, X, BR, X)
    turn_3 = '|-----|\n|     {}O{}\n|    {}/|{}\n|\n--------'.format(BR, X, BR, X)
    turn_4 = '|-----|\n|     {}O{}\n|     {}|{}\n|\n--------'.format(BR, X, BR, X)
    turn_5 = '|-----|\n|     {}O{}\n|\n|\n--------'.format(BR, X)
    turn_6 = '|-----|\n|\n|\n|\n--------'

    if _turns == 6:
        return turn_6
    elif _turns == 5:
        return turn_5
    elif _turns == 4:
        return turn_4
    elif _turns == 3:
        return turn_3
    elif _turns == 2:
        return turn_2
    elif _turns == 1:
        return turn_1
    elif _turns == 0:
        return turn_0
    else:
        return won


def main():
    # clear the screen
    os.system('clear')

    turns = 6
    game_won = False
    word, definition = set_secret(get_words('words.txt'))

    guessed_list = []
    correct_list = []
    for each in word:
        correct_list.append('-')

    while True:
        print(set_pic(turns))
        print('{}Definition: {}{}{}'.format(BA, A, definition, X))
        print('{}Correct: {}{}{}'.format(BP, P, ''.join(correct_list), X))
        print('{}Guessed: {}{}{}'.format(BB, B, ''.join(sorted(guessed_list)), X))

        while True:
            guess = input('{}Guess a letter: {}'.format(BY, X))
            if len(guess) == 1:
                if guess.isalpha():
                    if guess not in guessed_list:
                        break
            else:
                continue

        guessed_list.append(guess)

        did_guess = False
        for i, each in enumerate(word):
            if guess == each:
                did_guess = True
                correct_list[i] = each

        # clear the screen
        os.system('clear')

        if not did_guess:
            print('{}Your guess is not in the word :({}'.format(BR, X))
            turns -= 1
        else:
            print('{}You guessed correctly :){}'.format(BG, X))

        if ''.join(correct_list) == word:
                game_won = True
                break
        elif turns == 0:
            break
        else:
            continue
    # clear the screen
    os.system('clear')

    if game_won:
        print('{}You win! :){}'.format(BG, X))
        print(set_pic(7))
    else:
        print('{}You Lose! :({}'.format(BR, X))
        print(set_pic(turns))

    print('{}word: {}{}{}'.format(BA, A, word, X))
    print('{}definition: {}{}{}'.format(BP, P, definition, X))

if __name__ == "__main__":
    main()
