""" checkpython.py docstring

    This program will autocheck student programs made for the python_padawan curriculum
    The problem sets are defined in the curriculum docs and the routines are matched to each problem set
    http://pexpect.sourceforge.net/pexpect.html - only works in Linux environment
    
    :param app_name: the python file passed as a command line argument 
    :return None: each routine has a side effect, it prints the output and wether or not they were successful 

Todo:
    * implement the color variables and remove the colorama dependence
    * implement the Exception thrown by try-except so that user can see it better
    * code review and streamline earlier functions
    * modulize grader into pset graders
    
Author: Rocco Pietofesa
Date: 3/9/17

Please credit author for any use/modification of this base program
Please send donation to pietrofesar@gmail.com via PayPal if you find this useful

"""
from colorama import Fore, Style
import pexpect
import sys


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


def app_selector(option):
    """ input is name of program to grade, output is call to relevant autograde function """
    if option == 'slices.py':
        return slices(sys.argv[1])
    if option == 'madlib.py':
        return madlib(sys.argv[1])
    if option == 'hypotenuse.py': 
        return hypotenuse(sys.argv[1])
    if option == 'average.py': 
        return average(sys.argv[1])
    if option == 'polygon.py': 
        return polygon(sys.argv[1])
    if option == 'fahrenheit.py': 
        return fahrenheit(sys.argv[1])
    if option == 'report_card.py': 
        return report_card(sys.argv[1])
    if option == 'even_odd.py': 
        return even_odd(sys.argv[1])  
    if option == 'birth_month.py': 
        return birth_month(sys.argv[1]) 
    if option == 'grade_book.py': 
        return grade_book(sys.argv[1]) 
    if option == 'temperature.py': 
        return temperature(sys.argv[1]) 
    if option == 'initials.py':
        return initials(sys.argv[1])
    if option == 'left_stack.py': 
        return left_stack(sys.argv[1])
    if option == 'left_stacks.py': 
        return left_stacks(sys.argv[1])
    if option == 'right_stack.py': 
        return right_stack(sys.argv[1])
    if option == 'right_stacks.py': 
        return right_stacks(sys.argv[1])
    if option == 'pyramid.py': 
        return pyramid(sys.argv[1])
    if option == 'pyramid_hacker.py': 
        return pyramid_hacker(sys.argv[1])
    if option == 'binary_search.py': 
        return binary_search(sys.argv[1])
    if option == 'validate.py':
        return validate(sys.argv[1])
    if option == 'validate_functions.py':
        return validate_functions(sys.argv[1])


def slices(app_name):
    """
    :param app_name: the python file passed as a command line argument 
    :return None: 
        test suite for slices.py
    """
    # creates the app instance
    app = pexpect.spawnu('python3 {}'.format(app_name))
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
     
     
def madlib(app_name):
        """
        :param app_name: the python file passed as a command line argument 
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
        app = pexpect.spawnu('python3 {}'.format(app_name))
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
            
           
def hypotenuse(app_name):
    """
    :param app_name: the python file passed as a command line argument 
    :return None: 
    test suite for hypotenuse.py
    """
    phrase = ['Enter the side length:', 'The hypotenuse is ']
    data = ['3.1', '4.1', '5.14']
    # creates the app instance
    app = pexpect.spawnu('python3 {}'.format(app_name))
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


def average(app_name):
    """
    :param app_name: the python file passed as a command line argument 
    :return None: 
    test suite for hypotenuse.py
    """
    grade = ['first', 'second', 'third', 'fourth']
    nums = ['78', '97', '86', '88', '87']
    # creates the app instance
    app = pexpect.spawnu('python3 {}'.format(app_name))
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


def polygon(app_name):
    """
    :param app_name: the python file passed as a command line argument 
    :return None: 
    test suite for average.py
    """
    # creates the app instance
    app = pexpect.spawnu('python3 {}'.format(app_name))
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
            

def fahrenheit(app_name):
    """
    :param app_name: the python file passed as a command line argument 
    :return None: 
    test suite for fahrenheit.py
    """
    data = [['0', '0.0'], ['100', '100.0'], ['32', '32.0'], ['212', '212.0']]
    phrase = ['Hai! Enter the temperature in degrees Fahrenheit: ', '{} degrees Fahrenheit is approximately {} degrees Celsius.']
    
    # creates the app instance
    app = pexpect.spawnu('python3 {}'.format(app_name))
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
            

def report_card(app_name):
        """
        :param app_name: the python file passed as a command line argument 
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
        app = pexpect.spawnu('python3 {}'.format(app_name))
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
            

def even_odd(app_name):
    """
    :param app_name: the python file passed as a command line argument 
    :return None: 
    test suite for even_odd.py
    """
    ok = 0
    test_data = [['2', 'even'], ['3', 'odd'], ['-1', 'odd'], ['-2', 'even']]
    for i in range(4):
        # creates the app instance
        app = pexpect.spawnu('python3 {}'.format(app_name))
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


def birth_month(app_name):
    """ birth_month.py autograder """
    ok = 0
    checks = 12
    data = [['1', 'January'], ['2', 'February'], ['3', 'March'], ['4', 'April'], ['5', 'May'], ['6', 'June'], ['7', 'July'],
            ['8', 'August'], ['9', 'September'], ['10', 'October'], ['11', 'November'], ['12', 'December']]
    for i in range(checks):
        # creates the app instance
        app = pexpect.spawnu('python3 {}'.format(app_name))     
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
        print('{}\n:) {} == passed{}'.format(BY, app_name, X))
    else:
        print('{}\n:( {} == failed{}'.format(BY, app_name, X))


def grade_book(app_name):
    """ grade_book.py autograder """
    ok = 0
    checks = 5
    data = [['92', 'A'], ['84', 'B'], ['76', 'C'], ['65', 'D'], ['64', 'F']]
    for i in range(checks):
        # creates the app instance
        app = pexpect.spawnu('python3 {}'.format(app_name))     
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
        print('\n{}:) {} == passed{}'.format(BY, app_name, X))
    else:
        print('\n{}:( {} == failed{}'.format(BY, app_name, X))

  # -----------------------------------------------  
def temperature(app_name):
    """ temperature.py autograder """
    ok = 0
    checks = 4
    data = [['C', '212', '100.0'], ['C', '32', '0.0'], ['F', '100', '212.0'], ['F', '0', '32.0']]
    for i in range(checks):
        # creates the app instance
        app = pexpect.spawn('python3 {}'.format(app_name))     
        app.sendline('{}'.format(data[i][0]))
        app.sendline('{}'.format(data[i][1]))
        # check the correctness of submission
        try:
            app.expect_exact('{}'.format(data[i][2]))
            # pass
            print(Fore.GREEN, '{}:) {}'.format(app.before.decode("utf-8"), app.match.decode("utf-8")))
            ok += 1
        # fail
        except:
            print(Fore.YELLOW + ':( Expected: {}'.format(data[i][2]))
            print(Fore.RED + 'not {}'.format(app.before.decode("utf-8")))
    if ok == checks:
        print(Fore.GREEN + ':){} passed'.format(app_name))
    else:
        print(Fore.RED + ':({} failed'.format(app_name))


def initials(app_name):
    """initials.py autograder """
    ok = 0
    checks = 3
    data = [['albert percival wulfric brian dumbledore', 'APWBD'], ['ben franklin', 'BF'], ['broomhilda von shaft', 'BVS']]
    for i in range(checks):
        # creates the app instance
        app = pexpect.spawn('python3 {}'.format(app_name))     
        app.sendline('{}'.format(data[i][0]))
        # check the correctness of submission
        try:
            app.expect_exact('{}'.format(data[i][1]))
            # pass
            print(Fore.GREEN, '{}:) {}'.format(app.before.decode("utf-8"), app.match.decode("utf-8")))
            ok += 1
        # fail
        except:
            print(Fore.YELLOW + ':( Expected: {}'.format(data[i][1]))
            print(Fore.RED + 'not {}'.format(app.before.decode("utf-8")))
    if ok == checks:
        print(Fore.GREEN + ':){} passed'.format(app_name))
    else:
        print(Fore.RED + ':({} failed'.format(app_name))


def left_stack(app_name):
    """left_stack.py autograder """
    ok = 0
    checks = 2
    data = [[3, '#\r\n##\r\n###\r\n'], [6, '#\r\n##\r\n###\r\n####\r\n#####\r\n######\r\n']]
    for i in range(checks):
        # creates the app instance
        app = pexpect.spawn('python3 {}'.format(app_name))     
        app.sendline('{}'.format(data[i][0]))
        # check the correctness of submission
        try:
            app.expect_exact('{}'.format(data[i][1]))
            # pass
            print(Fore.GREEN, '{}{}'.format(app.before.decode("utf-8"), app.match.decode("utf-8")))
            ok += 1
        # fail
        except:
            print(Fore.YELLOW + ':( Expected: \n{}'.format(data[i][1]))
            print(Fore.RED + 'not: {}'.format(app.before.decode("utf-8")))
    if ok == checks:
        print(Fore.GREEN + ':) {} passed'.format(app_name))
    else:
        print(Fore.RED + ':({} failed'.format(app_name))
  
   
def left_stacks(app_name):
    """left_stacks.py autograder """
    ok = 0
    checks = 2
    data = [[3, '##\r\n###\r\n####\r\n'], [6, '##\r\n###\r\n####\r\n#####\r\n######\r\n#######\r\n']]
    for i in range(checks):
        # creates the app instance
        app = pexpect.spawn('python3 {}'.format(app_name))     
        app.sendline('{}'.format(data[i][0]))
        # check the correctness of submission
        try:
            app.expect_exact('{}'.format(data[i][1]))
            # pass
            print(Fore.GREEN, '{}{}'.format(app.before.decode("utf-8"), app.match.decode("utf-8")))
            ok += 1
        # fail
        except:
            print(Fore.YELLOW + ':( Expected: \n{}'.format(data[i][1]))
            print(Fore.RED + 'not: {}'.format(app.before.decode("utf-8")))
    if ok == checks:
        print(Fore.GREEN + ':) {} passed'.format(app_name))
    else:
        print(Fore.RED + ':({} failed'.format(app_name))
    

def right_stack(app_name):
    """right_stack.py autograder """
    ok = 0
    checks = 2
    data = [[3, '  #\r\n ##\r\n###\r\n'], [6, '     #\r\n    ##\r\n   ###\r\n  ####\r\n #####\r\n######\r\n']]
    for i in range(checks):
        # creates the app instance
        app = pexpect.spawn('python3 {}'.format(app_name))     
        app.sendline('{}'.format(data[i][0]))
        # check the correctness of submission
        try:
            app.expect_exact('{}'.format(data[i][1]))
            # pass
            print(Fore.GREEN, '{}{}'.format(app.before.decode("utf-8"), app.match.decode("utf-8")))
            ok += 1
        # fail
        except:
            print(Fore.YELLOW + ':( Expected: \n{}'.format(data[i][1]))
            print(Fore.RED + 'not: {}'.format(app.before.decode("utf-8")))
            print(app.before)
    if ok == checks:
        print(Fore.GREEN + ':) {} passed'.format(app_name))
    else:
        print(Fore.RED + ':({} failed'.format(app_name))


def right_stacks(app_name):
    """right_stacks.py autograder """
    ok = 0
    checks = 2
    data = [[3, '  ##\r\n ###\r\n####\r\n'], [6, '     ##\r\n    ###\r\n   ####\r\n  #####\r\n ######\r\n#######\r\n']]
    for i in range(checks):
        # creates the app instance
        app = pexpect.spawn('python3 {}'.format(app_name))     
        app.sendline('{}'.format(data[i][0]))
        # check the correctness of submission
        try:
            app.expect_exact('{}'.format(data[i][1]))
            # pass
            print(Fore.GREEN, '{}{}'.format(app.before.decode("utf-8"), app.match.decode("utf-8")))
            ok += 1
        # fail
        except:
            print(Fore.YELLOW + ':( Expected: \n{}'.format(data[i][1]))
            print(Fore.RED + 'not: {}'.format(app.before.decode("utf-8")))
            print(app.before)
    if ok == checks:
        print(Fore.GREEN + ':) {} passed'.format(app_name))
    else:
        print(Fore.RED + ':({} failed'.format(app_name))


def pyramid(app_name):
    """pyramid.py autograder """
    ok = 0
    checks = 2
    data = [[3, '  ##\r\n ####\r\n######\r\n'], [6, '     ##\r\n    ####\r\n   ######\r\n  ########\r\n ##########\r\n############\r\n']]
    for i in range(checks):
        # creates the app instance
        app = pexpect.spawn('python3 {}'.format(app_name))     
        app.sendline('{}'.format(data[i][0]))
        # check the correctness of submission
        try:
            app.expect_exact('{}'.format(data[i][1]))
            # pass
            print(Fore.GREEN, '{}{}'.format(app.before.decode("utf-8"), app.match.decode("utf-8")))
            ok += 1
        # fail
        except:
            print(Fore.YELLOW + ':( Expected: \n{}'.format(data[i][1]))
            print(Fore.RED + 'not: {}'.format(app.before.decode("utf-8")))
            print(app.before)
    if ok == checks:
        print(Fore.GREEN + ':) {} passed'.format(app_name))
    else:
        print(Fore.RED + ':({} failed'.format(app_name))


def pyramid_hacker(app_name):
    """pyramid_hacker.py autograder """
    ok = 0
    checks = 2
    data = [[3, '  /\\\r\n /  \\\r\n/____\\\r\n'], [6, '     /\\\r\n    /  \\\r\n   /    \\\r\n  /      \\\r\n /        \\\r\n/__________\\\r\n']]
    for i in range(checks):
        # creates the app instance
        app = pexpect.spawn('python3 {}'.format(app_name))     
        app.sendline('{}'.format(data[i][0]))
        # check the correctness of submission
        try:
            app.expect_exact('{}'.format(data[i][1]))
            # pass
            print(Fore.GREEN, '{}{}'.format(app.before.decode("utf-8"), app.match.decode("utf-8")))
            ok += 1
        # fail
        except:
            print(Fore.YELLOW + ':( Expected: \n{}'.format(data[i][1]))
            print(Fore.RED + 'not: {}'.format(app.before.decode("utf-8")))
        if app.isalive:
            app.kill(2)
    if ok == checks:
        print(Fore.GREEN + ':) {} passed'.format(app_name))
    else:
        print(Fore.RED + ':({} failed'.format(app_name))
    
        
        
def validate(app_name):
    """validate.py autograder """
    # creates the app instance
    app = pexpect.spawn('python3 {}'.format(app_name))  
    ok = 0
    data = [3, -6, - 8.9, '$', '\r', 'pickles', 'C']
    for i, each in enumerate(data):
        app.sendline('{}'.format(data[i]))
        # check the correctness of submission
        if each == 'C':
            print(Fore.GREEN + '{}{}'.format(app.match.decode("utf-8"), each))
            print(Fore.YELLOW + 'Alpha validation passed!\n')
            app.before = ''.encode("utf-8")
            data.reverse()
            for i, each in enumerate(data):
                app.sendline(str(data[i]))
                if type(each) != str and 0 < each < 10:
                    print(Fore.GREEN + '{}{}'.format(app.match.decode("utf-8"), each))
                    print(Fore.YELLOW + 'Numeric validation passed!\n')
                    print(Fore.GREEN + ': ) {} == passed!'.format(app_name))
                    
                else:
                    try:
                        app.expect_exact('Enter a positive number: ', timeout=1.5)
                        # pass
                        print(Fore.GREEN + '{}{}'.format(app.match.decode("utf-8"), data[i]))
                    except Exception as e:
                        print(Fore.RED + 'Numeric Validation Error\n\n {}'.format(e))
                        break    
        else:
            try:
                app.expect_exact('Enter a letter: ', timeout=1.5)
                # pass
                print(Fore.GREEN + '{}{}'.format(app.match.decode("utf-8"), data[i]))
            # fail
            except:
                print(Fore.RED + 'Alpha Validation Error\n\n {}'.format(app.before.decode("utf-8")))
                break

def validate_functions(app_name):
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
    

def binary_search(app_name):
    """ binary_search.py autograder """
    ok = 0
    checks = 4
    for i in range(checks):
        start = 0
        end = 1000
        middle = 500
        # creates the app instance
        app = pexpect.spawn('python3 {}'.format(app_name), timeout=5) 
        print(Fore.WHITE, end='')
        print('Test run number {}'.format(i + 1))
        print(Fore.GREEN, end='')
        print('Guess a number between 1 and 1000: 500')
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
                print(':) {}\n'.format(app.match.decode("utf-8")))
                break 
            # exception raised
            elif index == 3:
                print(Fore.RED, end='')
                print('errors in your code')
                break
            # exception raised
            elif index ==4:
                print(Fore.RED, end='')
                print('errors in your code')
                break
            else:
                print('error in code')
                break
            
    if ok == checks:
        print(Fore.GREEN, end='')
        print(':) {} passed'.format(app_name))
    else:
        print(Fore.RED, end='')
        print(':( {} failed'.format(app_name))


def main():
    # validate arguments
    if len(sys.argv) == 2:
        try:
            with open(sys.argv[1]) as file:
                pass
                # call grader routine
                app_selector(sys.argv[1])
        except IOError as e:
            print('{}ERROR\n{}{}{} doesn\'t exist or is incorrectly named'.format(BR, Y, sys.argv[1], X))
    else:
        print('{}ERROR\n{}Expected 2 arguments\n{}<terminal>{}$ python3 grader.py filename.py'.format(BR, X, BB, X))
        
if __name__ == "__main__":
    main()