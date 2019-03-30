#!/usr/bin/env python3.5
""" check1.py docstring

    This program will autocheck student problem sets for the python curriculum I've designed
    The problem sets are taken from numerous coureses and texts, I don't claim they are original.
    http://pexpect.sourceforge.net/pexpect.html - only works in Linux environment
    
    ****notes
        * spawn instead of spawnu shows unformatted strings for debugging
    
    :param file: the python file passed as a command line argument 
    :return None: each routine has a side effect, it prints the output and wether or not they were successful 

Todo:
    * implement the Exception thrown by try-except so that user can see it better
    * string slicing relies on hypothetical app.before strings; look for bugs while piloting grader, could produce exceptions
    * binary_search.py(beta status)
    * validate_functions.py(alpha status)
    * validate.py(beta status)
    
    
Author: Rocco Pietofesa
Date: 1/7/19

Please credit author for any use/modification of this base program
Please send donation to pietrofesar@gmail.com via PayPal if you find this useful

"""
import pexpect
import sys
import os
from subprocess import Popen, PIPE, STDOUT


# text color constants
R = '\033[0;31m'    # red
BR = '\033[1;31m'   # bold red
G = '\033[0;32m'    # green
BG = '\033[1;32m'   # bold green
Y = '\033[0;33m'    # yellow
BY = '\033[1;33m'   # bold yellow
B = '\033[0;34m'    # blue
BB = '\033[1;34m'   # bold blue
P = '\033[0;35m'    # purple
BP = '\033[1;35m'   # bold purple
A = '\033[0;36m'    # aqua
BA = '\033[1;36m'   # bold aqua
X = '\033[0m'       # reset

# searches for a file in the tree
def findInSubdirectory(filename, subdirectory=''):
    if subdirectory:
        path = subdirectory
    else:
        path = os.getcwd()
    for root, dirs, names in os.walk(path):
        if filename in names:
            return os.path.join(root, filename)
    raise 'File not found'


def find_nth(haystack, needle, n):
    """
    substring helper 
    :param haystack: string to be searched
    :param needle:   substring to find
    :param n:        desired occurence location of substring  
    :return i:       the index of the nth substring occurence 
    """
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)
    

def b_sanitize(before):
    """
    substring helper
    :param before:  app.before->string type
    :return parts:  a list of the lines or an empty list if error occured
    """
    parts = []
    try:
        parts = str(before).strip("b'").split('\r\n')
    except:
        pass
    return parts


def app_selector(option, file):
    """ input is name of program to grade, output is call to relevant autograde function
    :param option   : the name of the file entered into command line
    :param file     : absolute path to the file to be tested 
    """
    if option == 'ch1_1.py':
        return ch1_1(file)
    if option == 'ch1_2.py':
        return ch1_2(file)
    if option == 'ch1_3.py':
        return ch1_3(file)
    if option == 'ch1_4.py':
        return ch1_4(file)
    if option == 'ch1_5.py':
        return ch1_5(file)
    if option == 'slices.py':
        return slices(file)
    if option == 'madlib.py':
        return madlib(file)
    if option == 'hypotenuse.py': 
        return hypotenuse(file)
    if option == 'average.py': 
        return average(file)
    if option == 'polygon.py': 
        return polygon(file)
    if option == 'fahrenheit.py': 
        return fahrenheit(file)
    if option == 'report_card.py': 
        return report_card(file)
    if option == 'even_odd.py': 
        return even_odd(file)  
    if option == 'birth_month.py': 
        return birth_month(file) 
    if option == 'greedy.py': 
        return greedy(file)   
    if option == 'grade_book.py': 
        return grade_book(file) 
    if option == 'temperature.py': 
        return temperature(file) 
    if option == 'initials.py':
        return initials(file)
    options = ('left_stack', 'right_stack', 'pyramid')
    if any(routine in option for routine in options):
        return pyramid_stacks(file)
    if option == 'binary_search.py': 
        return binary_search(file)
    if option == 'validate.py':
        return validate(file)
    if option == 'validate_functions.py':
        return validate_functions(form)
    if option == 'quad_form.py':
        return quad_form_test()


def ch1_1(file):
    app = pexpect.spawn('python3 {}'.format(file))
    phrase = 'Welcome to Python\r\nWelcome to Computer Science\r\nProgramming is fun\r\n'
    # check the correctness of the submission
    try:
        app.expect_exact(phrase)
        # pass
        print('{}Output is correct!\n\n{}{}\n{}:) ch1_1.py == passed!{}'.format(BY, G, phrase, BY, X))
    # fail
    except:
        print('{}Expected output of:\n\n{}{}\n{}Actual output was:\n\n{}{}\n{}:( ch1_1.py == failed{}'
        .format(BY, R, phrase, BY, R, app.before, BY, X))
    if app.isalive:
            app.kill(2)
    

def ch1_2(file):
    app = pexpect.spawn('python3 {}'.format(file))
    phrase = 'FFFF  U    U  N    N\r\nF     U    U  NN   N\r\nFFFF  U    U  N N  N\r\nF     U    U  N  N N\r\nF      UUUU   N   NN\r\n'
    # check the correctness of the submission
    try:
        app.expect_exact(phrase)
        # pass
        print('{}Output is correct!\n\n{}{}\n{}:) ch1_2.py == passed!{}'.format(BY, G, phrase, BY, X))
    # fail
    except:
        print('{}Expected output of:\n\n{}{}\n{}Actual output was:\n\n{}{}\n{}:( ch1_2.py == failed{}'
        .format(BY, R, phrase, BY, R, app.before, BY, X))
    if app.isalive:
            app.kill(2)


def ch1_3(file):
    app = pexpect.spawn('python3 {}'.format(file))
    phrase = ' ---------\r\n|  O   O  |\r\n|    U    |\r\n|  \___/  |\r\n|         |\r\n ---------'
    # check the correctness of the submission
    try:
        app.expect_exact(phrase)
        # pass
        print('{}Output is correct!\n\n{}{}\n{}:) ch1_3.py == passed!{}'.format(BY, G, phrase, BY, X))
    # fail
    except:
        print('{}Expected output of:\n\n{}{}\n{}Actual output was:\n\n{}{}\n{}:( ch1_3.py == failed{}'
        .format(BY, R, phrase, BY, R, app.before, BY, X))
    if app.isalive:
            app.kill(2)


def ch1_4(file):
    app = pexpect.spawn('python3 {}'.format(file))
    phrase = '{0:7s}{1:7s}{2:s}\r\n'.format('a', 'a^2', 'a^3') + '{0:<7d}{1:<7d}{2:d}\r\n'.format(1, 1, 1) +\
                '{0:<7d}{1:<7d}{2:d}\r\n'.format(2, 4, 16) + '{0:<7d}{1:<7d}{2:d}\r\n'.format(3, 9, 27) + \
                '{0:<7d}{1:<7d}{2:d}\r\n'.format(4, 16, 64)
    # check the correctness of the submission
    try:
        app.expect_exact(phrase)
        # pass
        print('{}Output is correct!\n\n{}{}\n{}:) ch1_4.py == passed!{}'.format(BY, G, phrase, BY, X))
    # fail
    except:
        print('{}Expected output of:\n\n{}{}\n{}Actual output was:\n\n{}{}\n{}:( ch1_4.py == failed{}'
        .format(BY, R, phrase, BY, R, app.before, BY, X))
    if app.isalive:
            app.kill(2)
 
 
def ch1_5(file):
    app = pexpect.spawn('python3 {}'.format(file))
    phrase = str((9.5 *4.5-2.5*3)/(45.5-3.5))
    # check the correctness of the submission
    try:
        app.expect_exact(phrase)
        # pass
        print('{}Output is correct!\n\n{}{}\n{}:) ch1_5.py == passed!{}'.format(BY, G, phrase, BY, X))
    # fail
    except:
        print('{}Expected output of:\n\n{}{}\n{}Actual output was:\n\n{}{}\n{}:( ch1_5.py == failed{}'
        .format(BY, R, phrase, BY, R, app.before, BY, X))
    if app.isalive:
            app.kill(2)
 
    
def slices(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
        test suite for slices.py
    """
    # creates the app instance
    app = pexpect.spawnu('python3 {}'.format(file))
    phrase = 'Be\r\nyourself\r\neveryone\r\nelse\r\nis\r\nalready\r\ntaken\r\n'
    # check the correctness of the submission
    try:
        app.expect_exact(phrase)
        # pass
        print('{}Output is correct!\n\n{}{}\n{}:) slices.py == passed!{}'.format(BY, G, phrase, BY, X))
    # fail
    except:
        print('{}Expected output of:\n\n{}{}\n{}Actual output was:\n\n{}{}\n{}:( slices.py == failed{}'
        .format(BY, R, phrase, BY, R, app.before, BY, X))
    if app.isalive:
            app.kill(2)
     
     
def madlib(file):
        """
        :param file: the python file passed as a command line argument 
        :return None: 
        test suite for madlib.py
        """
        # words to enter
        words = ['<to>', '<adj>', '<verb1>', '<body_part>', '<num>', '<noun>', '<adverb>', '<verb2>', '<verb3>',
                '<pronouns>', '<author>']
        phrase = 'Dear <to>,\r\nYou are extremely <adj> and I <verb1> you.\r\n' \
                 'I want to kiss your <body_part> <num> times.\r\n' \
                 'You make my <noun> burn with desire.\r\n' \
                 'When I first saw you, I <adverb> <verb2> at you and fell in love.\r\n' \
                 'Will you <verb3> out with me?\r\n' \
                 'Don\'t let your parents discourage you, <pronouns> are just jealous.\r\n' \
                 'Yours forever, <author> :)\r\n'
        # creates the app instance
        app = pexpect.spawnu('python3 {}'.format(file))
        # enters the words
        for each in words:
            app.sendline(each)
        # check the correctness of submission
        try:
            app.expect_exact(phrase)
            # pass
            print('\n{}Output is correct!\n\n{}{}\n{}:) slices.py == passed!{}'
            .format(BY, G, phrase, BY, X))
        # fail
        except:
            print('\n{}Expected output of:\n\n{}{}\n{}Actual output was:\n\n{}{}{}:( slices.py == failed{}'
            .format(BY, R, phrase, BY, R, app.before, BY, X))
        if app.isalive:
            app.kill(2)


def greedy(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for greedy.py
    """
    # creates the app instance
    data_in = [3.84,  1.10, .30, .04]
    data_out = ['15 quarters, 0 dimes, 1 nickels, 4 pennies', '4 quarters, 1 dimes, 0 nickels, 0 pennies', '1 quarters, 0 dimes, 1 nickels, 0 pennies', '0 quarters, 0 dimes, 0 nickels, 4 pennies']
    
    for i, each in enumerate(data_in):
        app = pexpect.spawnu('python3 {}'.format(file))
        app.sendline(str(each))
        # check the correctness of submission
        try:
            app.expect_exact('{}'.format(data_out[i]))
            # pass
            print('{}Output is correct!\n\n{}{}{}\n\n{}:) greedy.py == passed{}'
            .format(BY, G, app.before, app.match, BY, X))
        # fail
        except:
            print('{}Expected output of:\n\n{}{}\n'.format(BY, R, data_out[i]))
            print('{}Actual output was:\n\n{}{}\n{}:( greedy.py == failed{}'.format(BY, R, app.before, BY, X))
        if app.isalive:
                app.kill(2) 

           
def hypotenuse(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for hypotenuse.py
    """
    phrase = ['Enter the side length:', 'The hypotenuse is ']
    data = ['3.1', '4.1', '5.14']
    # creates the app instance
    app = pexpect.spawnu('python3 {}'.format(file))
    app.sendline(data[0])
    app.sendline(data[1])
    # check the correctness of submission
    try:
        app.expect_exact(phrase[1] + data[2])
        # pass
        print('{}Output is correct!\n\n{}{}{}\n\n{}:) hypotenuse.py == passed{}'
        .format(BY, G, app.before, app.match, BY, X))
    # fail
    except:
        print('{}Expected output of:\n\n{}{}{}\n{}{}\n{}{}\n\n{}Actual output was:\n\n{}{}\n{}:( slices.py == failed{}'
        .format(BY, R, phrase[0], data[0], phrase[0], data[1], phrase[1], data[2], BY, R, app.before, BY, X))
    if app.isalive:
            app.kill(2)


def average(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for hypotenuse.py
    """
    grade = ['first', 'second', 'third', 'fourth']
    nums = ['78', '97', '86', '88', '87']
    # creates the app instance
    app = pexpect.spawnu('python3 {}'.format(file))
    app.sendline(nums[0])
    app.sendline(nums[1])
    app.sendline(nums[2])
    app.sendline(nums[3])
    # check the correctness of submission
    try:
        app.expect_exact('The average is 87')
        # pass
        print('{}Output is correct!\n\n{}{}{}\n\n{}:) average.py == passed{}'
        .format(BY, G, app.before, app.match, BY, X))
    # fail
    except:
        print('{}Expected output of:{}\n'.format(BY, R))
        for i, each in enumerate(grade):
            print('Enter the {} grade: {}'.format(grade[i], nums[i]))
        print('The average is 87')
        print('\n{}Actual output was:\n\n{}{}\n{}:( average.py == failed{}'.format(BY, R, app.before, BY, X))
    if app.isalive:
            app.kill(2)


def polygon(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for average.py
    """
    # creates the app instance
    app = pexpect.spawnu('python3 {}'.format(file))
    app.sendline('6')
    # check the correctness of submission
    try:
        app.expect_exact('The interior angles are 120.0 degrees.')
        # pass
        print('{}Output is correct!\n\n{}{}{}\n\n{}:) polygon.py == passed{}'
        .format(BY, G, app.before, app.match, BY, X))
    # fail
    except:
        print('{}Expected output of:\n\n{}Enter the number of sides: 6\nThe interior angles are 120.0 degrees.\n'.format(BY, R))
        print('{}Actual output was:\n\n{}{}\n{}:( polygon.py == failed{}'.format(BY, R, app.before, BY, X))
    if app.isalive:
            app.kill(2)
            

def fahrenheit(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for fahrenheit.py
    """
    data = [['0', '0.0'], ['100', '100.0'], ['32', '32.0'], ['212', '212.0']]
    phrase = ['Hai! Enter the temperature in degrees Fahrenheit: ', '{} degrees Fahrenheit is approximately {} degrees Celsius.']
    
    # creates the app instance
    app = pexpect.spawnu('python3 {}'.format(file))
    app.sendline(data[3][0])
    # check the correctness of submission
    try:
        app.expect_exact(phrase[1].format(data[3][1], data[1][1]))
        # pass
        print('{}Output is correct!\n\n{}{}{}\n\n{}:) fahrenheit.py == passed{}'
        .format(BY, G, app.before, app.match, BY, X))
    # fail
    except:
        print('{}Expected output of:\n\n{}{}{}\n{}\n{}\nActual output was:\n\n{}{}{}\n:( fahrenheit.py == failed{}'
        .format(BY, R, phrase[0], data[3][0], phrase[1].format(data[3][1], data[1][1]), BY, R, app.before, BY, X))
    if app.isalive:
            app.kill(2)
            

def report_card(file):
        """
        :param file: the python file passed as a command line argument 
        :return None: 
        test suite for fahrenheit.py
        """
        # words to enter
        data = ['Einstein', '99.8', '98.7', '95.3', '81.4', '75.0', '68.5']

        phrase = 'This is {}\'s report card.\r\n\r\n' \
         '6 sorted grades: [{}, {}, {}, {}, {}, {}]\r\n\r\n' \
         '{}\'s highest grade is {}.\r\n\r\n' \
         'The low grade of {} is being dropped.\r\n\r\n' \
         'Now {}\'s grades are [{}, {}, {}, {}, {}].\r\n\r\n' \
         '{}\'s average is now 90.0.\r\n\r\n'.format(data[0], data[6], data[5], data[4], data[3], data[2], data[1],
                                                     data[0], data[1], data[6], data[0], data[5],
                                                     data[4], data[3], data[2], data[1], data[0])
        # creates the app instance
        app = pexpect.spawnu('python3 {}'.format(file))
        # enters the words
        for each in data:
            app.sendline(each)
        # check the correctness of submission
        try:
            app.expect_exact(phrase)
            # pass
            print('\n{}Output is correct!\n{}{}\n{}{}:) report_card.py == passed\n{}'
            .format(BY, G, app.before, app.match, BY, X))
        # fail
        except:
            print(app.before)
            print('\n{}Expected output of:\n{}{}\n{}Actual output was:\n{}{}{}:( report_card.py == failed{}'
            .format(BY, R, phrase, BY, R, app.before[225:], BY, X))
        if app.isalive:
            app.kill(2)
            

def even_odd(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for even_odd.py
    """
    ok = 0
    test_data = [['2', 'even'], ['3', 'odd'], ['-1', 'odd'], ['-2', 'even']]
    for i in range(4):
        # creates the app instance
        app = pexpect.spawnu('python3 {}'.format(file))
        app.sendline('{}'.format(test_data[i][0]))
        # check the correctness of submission
        try:
            app.expect_exact('{} is an {} number.'.format(test_data[i][0], test_data[i][1]))
            # pass
            print('{}{}'.format(G, app.match))
            ok += 1
        # fail
        except:
            print('\n{}Expected output of:\n{}{} is an {} number\n{}Actual output was:\n{}{}{}'
            .format(BY, R, test_data[i][0], test_data[i][1], BY, R, app.before[19:], X))
        if app.isalive:
            app.kill(2)
    if ok == 4:
        print('{}:) even_odd.py == passed{}'.format(BY, X))
    else:
        print('{} even_odd.py == failed{}'.format(BY, X))


def birth_month(file):
    """ birth_month.py autograder """
    ok = 0
    checks = 12
    data = [['1', 'January'], ['2', 'February'], ['3', 'March'], ['4', 'April'], ['5', 'May'], ['6', 'June'], ['7', 'July'],
            ['8', 'August'], ['9', 'September'], ['10', 'October'], ['11', 'November'], ['12', 'December']]
    for i in range(checks):
        # creates the app instance
        app = pexpect.spawnu('python3 {}'.format(file))     
        app.sendline('{}'.format(data[i][0]))
        # check the correctness of submission
        try:
            app.expect_exact('You were born in {}.'.format(data[i][1]))
            # pass
            print('{}{}{}{}'.format(app.before, G, app.match, X))
            ok += 1
        # fail
        except:
            print(app.before[:53])
            print('{}:( Expected output of:\n{}You were born in {}.{}'.format(BY, R, data[i][1], X))
            print('{}Actual output was:{}{}{}'.format(BY, R, app.before[53:len(app.before)-2], X))
        if app.isalive:
            app.kill(2)
    if ok == checks:
        print('{}\n:) {} == passed{}'.format(BY, file, X))
    else:
        print('{}\n:( {} == failed{}'.format(BY, file, X))


def grade_book(file):
    """ grade_book.py autograder """
    ok = 0
    checks = 5
    data = [['92', 'A'], ['84', 'B'], ['76', 'C'], ['65', 'D'], ['64', 'F']]
    for i in range(checks):
        # creates the app instance
        app = pexpect.spawnu('python3 {}'.format(file))     
        app.sendline('{}'.format(data[i][0]))
        # check the correctness of submission
        try:
            app.expect_exact('{} is your letter grade.'.format(data[i][1]))
            # pass
            print('{}{}{}{}'.format(app.before, G, app.match, X))
            ok += 1
        # fail
        except:
            print(app.before[:27])
            print('{}Expected output of:\n{}{} is your letter grade.{}'.format(BY, R, data[i][1], X))
            print('{}Actual output was:\n{}{}{}'.format(BY, R, app.before[29:len(app.before)-2], X))
        if app.isalive:
            app.kill(2)
    if ok == checks:
        print('\n{}:) {} == passed{}'.format(BY, file, X))
    else:
        print('\n{}:( {} == failed{}'.format(BY, file, X))


def temperature(file): 
    """ temperature.py autograder """
    ok = 0
    checks = 4
    data = [['C', '212', '100.0'], ['C', '32', '0.0'], ['F', '100', '212.0'], ['F', '0', '32.0']]
    for i in range(checks):
        # creates the app instance
        app = pexpect.spawnu('python3 {}'.format(file))     
        app.sendline('{}'.format(data[i][0]))
        app.sendline('{}'.format(data[i][1]))
        # check the correctness of submission
        try:
            app.expect_exact('{}'.format(data[i][2]))
            # pass
            print('{}{}{}{}'.format(app.before, G, app.match, X))
            ok += 1
        # fail
        except:
            before = b_sanitize(app.before)
            print('{}\n{}'.format(before[0], before[1]))
            print('{}Expected output of:\n{}{}'.format(BY, R, data[i][2]))
            print('{}Actual output was:\n{}{}{}'.format(BY, R, before[2], X))
        if app.isalive:
            app.kill(2)
    if ok == checks:
        print('{}:) {} == passed{}'.format(BY, file, X))
    else:
        print('{}:( {} == failed{}'.format(BY, file, X))
  

def initials(file): # updated
    """initials.py autograder """
    ok = 0
    checks = 3
    data = [['albert percival wulfric brian dumbledore', 'APWBD'], ['ben franklin', 'BF'], ['broomhilda von shaft', 'BVS']]
    for i in range(checks):
        # creates the app instance
        app = pexpect.spawnu('python3 {}'.format(file))     
        app.sendline('{}'.format(data[i][0]))
        # check the correctness of submission
        try:
            app.expect_exact('{}'.format(data[i][1]))
            # pass
            print('{}{}{}{}'.format(app.before, G, app.match, X))
            ok += 1
        # fail
        except:
            index = str(app.before.encode('utf-8')).index(chr(92)) # finds first \r in app.before for slice
            print('{}'.format(app.before[:index-1]))
            print('{}Expected output of:\n{}{}{}'.format(BY, R, data[i][1], X))
            print('{}Actual output was:\n{}{}{}'.format(BY, R, app.before[index:len(app.before)-2], X))
        if app.isalive:
            app.kill(2)
    if ok == checks:
        print('{}:) {} == passed{}'.format(BY, file, X))
    else:
        print('{}:( {} == failed{}'.format(BY, file, X))


def pyramid_stacks(file):
    """pyramid_stacks.py autograder """
    ok = 0
    checks = 2
    
    if file == 'left_stack.py':
        data = [[3, '#\r\n##\r\n###\r\n'], [6, '#\r\n##\r\n###\r\n####\r\n#####\r\n######\r\n']]
    if file == 'left_stacks.py': 
        data = [[3, '##\r\n###\r\n####\r\n'], [6, '##\r\n###\r\n####\r\n#####\r\n######\r\n#######\r\n']]
    if file == 'right_stack.py':
        data = [[3, '  #\r\n ##\r\n###\r\n'], [6, '     #\r\n    ##\r\n   ###\r\n  ####\r\n #####\r\n######\r\n']]
    if file == 'right_stacks.py':
        data = [[3, '  ##\r\n ###\r\n####\r\n'], [6, '     ##\r\n    ###\r\n   ####\r\n  #####\r\n ######\r\n#######\r\n']]
    if file == 'pyramid.py':
        data = [[3, '  ##\r\n ####\r\n######\r\n'], [6, '     ##\r\n    ####\r\n   ######\r\n  ########\r\n ##########\r\n############\r\n']]
    if file == 'pyramid_hacker.py':
        data = [[3, '  /\\\r\n /  \\\r\n/____\\\r\n'], [6, '     /\\\r\n    /  \\\r\n   /    \\\r\n  /      \\\r\n /        \\\r\n/__________\\\r\n']]
    
    for i in range(checks):
        # creates the app instance
        app = pexpect.spawnu('python3 {}'.format(file))     
        app.sendline('{}'.format(data[i][0]))
        # check the correctness of submission
        try:
            app.expect_exact('{}'.format(data[i][1]))
            # pass
            print('{}{}{}{}'.format(app.before, G, app.match, X))
            ok += 1
        # fail
        except:
            print(app.before[:find_nth(app.before, '\r\n', 0)])
            print('{}Expected output of:\n{}{}{}'.format(BY, R, data[i][1], X))
            print('{}Acutal output was:\n{}{}{}'.format(BY, R, '\n'.join(b_sanitize(app.before)[1:]), X))
        if app.isalive:
            app.kill(2)
    if ok == checks:
        print('{}:) {} == passed{}'.format(BY, file, X))
    else:
        print('{}:( {} == failed{}'.format(BY, file, X))

        
def validate(file):
    """validate.py autograder 
    this needs to be gone over with test cases, still in beta
    """
    # creates the app instance
    app = pexpect.spawnu('python3 {}'.format(file))  
    ok = 0
    data = [3, -6, - 8.9, '$', '\r', 'pickles', 'C']
    for i, each in enumerate(data):
        app.sendline(str(data[i]))
        # checking alpha validation
        if each == 'C':
            # alpha passed
            print('{}{}{}{}'.format(app.match, BG, each, X))
            print('{}Alpha validation passed!\n{}'.format(G, X))
            data.reverse()
            # checking for numeric validation
            for i, each in enumerate(data):
                app.sendline(str(data[i]))
                if type(each) != str and 0 < each < 10:
                    #numeric passed
                    print('{}{}{}{}'.format(app.match, BG, each, X))
                    print('{}Numeric validation passed!\n{}'.format(G, X))
                    print('{}:) {} == passed!{}'.format(BY, file, X))
                # cycle numeric data test   
                else:
                    try:
                        app.expect_exact('Enter a positive number: ', timeout=1.5)
                        # pass
                        print('{}{}'.format(app.match, data[i]))
                    #fail
                    except Exception as e:
                        print('{}Numeric Validation Error\n\n{}{}{}'.format(BR, R, e, X))
                        print('{}:( {} == failed!{}'.format(BY, file, X))
                        break    
        # cycle alpha data test
        else:
            try:
                app.expect_exact('Enter a letter: ', timeout=1.5)
                # pass
                print('{}{}'.format(app.match, data[i]))
            # fail
            except:
                print('{}Alpha Validation Error\n\n{}{}{}'.format(BR, R, app.before, X))
                print('{}:( {} == failed!{}'.format(BY, file, X))
                break
    if app.isalive:
            app.kill(2)
            
            
def validate_functions(file):
    """validate_functions.py autograder """
    # creates the app instance
    app = pexpect.spawn('python3')
    app.sendline('from validate_functions import *')
    app.sendline('temp = test()')
    app.sendline('print(temp)')
    try:
        app.expect('test printed')
        print('yes the test has passed')
    except Exception as e:
        print(e)
    # print(app.before.decode("utf-8")) 
    print(app.after.decode("utf-8"))           
    '''
    pexpect.run('python3', timeout=3, events={'(?i)Python 3.4.3 (default, Nov 17 2016, 01:08:31)\n[GCC 4.8.4] on linux\nType "help",\
                                    "copyright", "credits" or "license" for more information.':'quit()'})
    '''

def binary_search(file):
    """ binary_search.py autograder """
    ok = 0
    checks = 4
    for i in range(checks):
        start = 0
        end = 1000
        middle = 500
        # creates the app instance
        app = pexpect.spawnu('python3 {}'.format(file), timeout=5) 
        print('Test run number {}\nGuess a number between 1 and 1000: 500'.format(i + 1))
        while True:
            app.sendline(str(middle))
            # check the correctness of submission
            # print(start, end, middle)
            index = app.expect_exact(['too low, try again; guess-->', 'too high, try again; guess-->',
                                    'You guessed it, the secret number was {}'.format(middle), pexpect.EOF, pexpect.TIMEOUT])
            # too low
            if index == 0:
                start = middle + 1
                # factored form, orginal -->int((end - start) / 2) + start
                middle = int(end / 2 + .5 * start) 
                print('too low, try again; guess-->{}'.format(middle))
            # too high
            elif index == 1:
                end = middle - 1
                middle = int(end / 2 + .5 * start) 
                print('too high, try again; guess-->{}'.format(middle))
            # number has been guessed                
            elif index == 2:
                ok += 1
                print('{}{}{}\n'.format(G, app.match, X))
                break 
            # exception raised
            elif index == 3 or 4:
                print('{}errors in your code{}'.format(R, X))
                break
            else:
                print('{}error in code{}'.format(R, X))
                break
            
    if ok == checks:
        print('{}:) {} == passed{}'.format(BY, file, X))
    else:
        print('{}:( {} == failed{}'.format(BY, file, X))


def quad_form_test():
        
    def quad_form_unit_test():
        
        ok = True
        zero = ('no', 1, -3, 4, 0, [])
        one = ('one', -4, 12, -9, 1, [1.5])
        two = ('two', 2, -11, 5, 2, [5.0, 0.5])
        data = (zero, one , two)
        
        for i, each in enumerate(data):
            t = quad_form(data[i][1], data[i][2], data[i][3])
            print('{}Testing for {} real root/s{}'.format(BY, data[i][0], X))
            print('quad_form({}, {}, {}) returns {}'.format(data[i][1], data[i][2], data[i][3], t))
        
            if len(t) == data[i][4]:
                print('{}Correct number of return values{}'.format(G, X))
                if t == data[i][5] or data[i][5].reverse:
                    print('{}root/s are correct{}'.format(G, X))
                else:
                    print('{}root/s are wrong{}'.format(G, X))
                    ok == False
            else:
                print('{}Wrong number of return values{}'.format(R, X))
                ok == False
            if type(t) == list:
                print('{}data type correct{}'.format(G, X))
            else:
                print('{}data type wrong{}'.format(R, X))
                ok == False
        if ok:
            print('{}:) quad_form == passed!{}'.format(BY, X))
        else:
            print('{}:( quad_from == failed{}'.format(BY, X))
    
    p = Popen(['python3'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
    out = p.communicate(input=b'from quad_form import quad_form\nfrom helpers import quad_form_unit_test\nquad_form_unit_test()\n')[0]
    print(out.decode())





def main():
    # validate arguments
    if len(sys.argv) == 2:
        try:
            # find and store the file
            student_file = findInSubdirectory(sys.argv[1])
            # print(student_file)
            app_selector(sys.argv[1], student_file)
            '''
            with open(student_file) as file:
                pass
                # call grader routine
                app_selector(sys.argv[1], student_file)
                '''
            ''' original
            with open(sys.argv[1]) as file:
                pass
                # call grader routine
                app_selector(sys.argv[1])
            '''
        except IOError as e:
            print('{}ERROR\n{}{}{} doesn\'t exist or is incorrectly named'.format(BR, Y, sys.argv[1], X))
            
    else:
        print('{}ERROR\n{}Expected 2 arguments\n{}<terminal>{}$ python3 grader.py filename.py'.format(BR, X, BB, X))
        
if __name__ == "__main__":
    main()
