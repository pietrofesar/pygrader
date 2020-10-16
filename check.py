#!/usr/bin/env python3.6
""" check.py docstring
    check.py version 2.0
    This program will autocheck student problem sets for the python curriculum I've designed
    The problem sets are taken from numerous coureses and texts, I don't claim they are original.
    http://pexpect.sourceforge.net/pexpect.html - only works in Linux environment
    
    ****notes
        * spawn instead of spawnu shows unformatted strings for debugging
    
    :param file: the python file passed as a command line argument 
    :return None: each routine has a side effect, it prints the output and wether or not they were successful 
Todo:
    * implement the Exception thrown by try-except so that user can see it better
    * string slicing relies on hypothetical child.before strings; look for bugs while piloting grader, could produce exceptions
    * binary_search.py(beta status)
    * validate_functions.py(alpha status)
    * validate.py(beta status)
    * troubleshoot line 60
    
    
Author: Rocco Pietofesa
Date: 1/14/20
Please credit author for any use/modification of this base program
Please send donation to pietrofesar@gmail.com via PayPal if you find this useful
"""
import pexpect
import sys
import os
import random
import math
import time

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


library = ['hello', 'apparatus', 'consequence', 'missippi', 'alagash', 'illustrate', 'erradicate', 'impecible', 'american-indian', 'distillery', 'distinguished']

# searches for a file in the tree
def findInSubdirectory(filename, subdirectory=''):
    if subdirectory:
        path = subdirectory
    else:
        path = os.getcwd()
    for root, dirs, names in os.walk(path):
        if filename in names:
            return os.path.join(root, filename)
    #raise 'File not found'
    
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
    :param before:  child.before->string type
    :return parts:  a list of the lines or an empty list if error occured
    """
    parts = []
    try:
        parts = str(before).strip("b'").split('\r\n')
    except:
        pass
    return parts

def assess(child, pset, answerKey, read=""):
    """
    assesses the output of the calling function for correctness, reports the output
    """
    # check the correctness of the submission
    try:
        child.expect_exact(answerKey)
        # pass
        print(f'{BY}Output is correct!')
        print(f'\n{G}{read}{child.before}')
        print(f'{answerKey}')
        print(f'\n{BY}:) {pset} == passed!{X}')
        child.terminate
    # fail
    except:
        print(f'{BY}Expected output of:\n\n{R}{answerKey}')
        print(f'\n{BY}Actual output was:\n\n{R}{read}{child.before}')
        print(f'{BY}:( {pset} == failed{X}')
        child.terminate


def getOperands(theString):   
    while len(theString) != 0 and not theString[0].isdigit():
        theString = theString[1:]
    while len(theString) != 0 and not theString[-1].isdigit():
        theString = theString[:-1]
        print()
    operands = [int(i) for i in theString.split() if i.isdigit()]
    return operands

    
def child_selector(option, file):
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
    if option == 'ch1_6.py':
        return ch1_6(file)
        
    if option == 'ch2_1.py':
        return ch2_1(file)
    if option == 'ch2_2.py':
        return ch2_2(file)
    if option == 'ch2_3.py':
        return ch2_3(file)
    if option == 'ch2_4.py':
        return ch2_4(file)
    if option == 'ch2_5.py':
        return ch2_5(file)
    if option == 'ch2_6.py':
        return ch2_6(file)
    if option == 'ch2_7.py':
        return ch2_7(file)
    if option == 'ch2_8.py':
        return ch2_8(file)
    if option == 'ch2_9.py':
        return ch2_9(file)
    if option == 'ch2_10.py':
        return ch2_10(file)
    if option == 'ch2_13.py':
        return ch2_13(file)
    if option == 'ch2_14.py':
        return ch2_14(file)
    if option == 'ch2_15.py':
        return ch2_15(file)
    if option == 'ch2_18.py':
        return ch2_18(file)
    if option == 'ch2_19.py':
        return ch2_19(file)
    if option == 'ch2_20.py':
        return ch2_20(file)
    if option == 'ch2_21.py':
        return ch2_21(file)
        
    if option == 'ch3_1.py':
        return ch3_1(file)
    if option == 'ch3_2.py':
        return ch3_2(file)
    if option == 'ch3_4.py':
        return ch3_4(file)
    if option == 'ch3_5.py':
        return ch3_5(file)
    if option == 'ch3_6.py':
        return ch3_6(file)
    if option == 'ch3_7.py':
        return ch3_7(file)
    if option == 'ch3_11.py':
        return ch3_11(file)
    
    if option == 'ch4_1.py':
        return ch4_1(file)
    if option == 'ch4_2.py':
        return ch4_2(file)
    if option == 'ch4_3.py':
        return ch4_3(file)
    if option == 'ch4_4.py':
        return ch4_4(file)
    if option == 'ch4_5.py':
        return ch4_5(file)
    if option == 'ch4_6.py':
        return ch4_6(file)
    if option == 'ch4_7.py':
        return ch4_7(file)
    if option == 'ch4_8.py':
        return ch4_8(file)
    if option == 'ch4_9.py':
        return ch4_9(file)  
    if option == 'ch4_10.py':
        return ch4_10(file)
    if option == 'ch4_11.py':
        return ch4_11(file)
    if option == 'ch4_12.py':
        return ch4_12(file)
    if option == 'ch4_16.py':
        return ch4_16(file)
    if option == 'ch4_17.py':
        return ch4_17(file)
    if option == 'ch4_24.py':
        return ch4_24(file)
    
    if option == 'ch5_1.py':
        return ch5_1(file)
    if option == 'ch5_2.py':
        return ch5_2(file)
    if option == 'ch5_3.py':
        return ch5_3(file)
    if option == 'ch5_4.py':
        return ch5_4(file)
    if option == 'ch5_5.py':
        return ch5_5(file)
    if option == 'ch5_6.py':
        return ch5_6(file)
    if option == 'ch5_7.py':
        return ch5_7(file)
    if option == 'ch5_8.py':
        return ch5_8(file)
    if option == 'ch5_11.py':
        return ch5_11(file)
    if option == 'ch5_12.py':
        return ch5_12(file)
    if option == 'ch5_13.py':
        return ch5_13(file)
    if option == 'ch5_14.py':
        return ch5_14(file)
    if option == 'ch5_15.py':
        return ch5_15(file)
    if option == 'ch5_16.py':
        return ch5_16(file)
    if option == 'ch5_17.py':
        return ch5_17(file)
    if option == 'ch5_18.py':
        return ch5_18(file)
    if option == 'ch5_19.py':
        return ch5_19(file)
    if option == 'ch5_20A.py':
        return ch5_20A(file)
    if option == 'ch5_20B.py':
        return ch5_20B(file)
    if option == 'ch5_20C.py':
        return ch5_20C(file)
    if option == 'ch5_20D.py':
        return ch5_20D(file)
    if option == 'ch5_21.py':
        return ch5_21(file)
        
    if option == 'ch6_2.py':
        return ch6_2(file)
    if option == 'ch6_3.py':
        return ch6_3(file)
    if option == 'ch6_4.py':
        return ch6_4(file)
    if option == 'ch6_5.py':
        return ch6_5(file)
    if option == 'ch6_6.py':
        return ch6_6(file)
    if option == 'ch6_7.py':
        return ch6_7(file)
    if option == 'ch6_8.py':
        return ch6_8(file)
    if option == 'ch6_9.py':
        return ch6_9(file)
    if option == 'ch6_10.py':
        return ch6_10(file)
    if option == 'ch6_11.py':
        return ch6_11(file)
    if option == 'ch6_12.py':
        return ch6_12(file)
    if option == 'ch6_13.py':
        return ch6_13(file)
    
    if option == 'ch8_1.py':
        return ch8_1(file)
    if option == 'ch8_2.py':
        return ch8_2(file)
    if option == 'ch8_3.py':
        return ch8_3(file)
    if option == 'ch8_4.py':
        return ch8_4(file)
    if option == 'ch8_5.py':
        return ch8_5(file)
    if option == 'ch8_6.py':
        return ch8_6(file)
    if option == 'ch8_7.py':
        return ch8_7(file)
    if option == 'ch8_8.py':
        return ch8_8(file)
    if option == 'ch8_9.py':
        return ch8_9(file)
    if option == 'ch8_10.py':
        return ch8_10(file)
    if option == 'ch8_11.py':
        return ch8_11(file)
    if option == 'ch8_12.py':
        return ch8_12(file)
    if option == 'ch8_13.py':
        return ch8_13(file)
    
    if option == 'ch10_1.py':
        return ch10_1(file)
    if option == 'ch10_2.py':
        return ch10_2(file)
    if option == 'ch10_3.py':
        return ch10_3(file)
    if option == 'ch10_4.py':
        return ch10_4(file)
    if option == 'ch10_5.py':
        return ch10_5(file)
    if option == 'ch10_6.py':
        return ch10_6(file)
    if option == 'ch10_7.py':
        return ch10_7(file)
    if option == 'ch10_8.py':
        return ch10_8(file)
    if option == 'ch10_9.py':
        return ch10_9(file)
    if option == 'ch10_10.py':
        return ch10_10(file)
    
    # Sienna Green 2018 Problems
    if option == 'green1_18.py':
        return green1_18(file)
    if option == 'green2_18.py':
        return green2_18(file)
    if option == 'green3_18.py':
        return green3_18(file)
    if option == 'green4_18.py':
        return green4_18(file)
    if option == 'green5_18.py':
        return green5_18(file)
    if option == 'green6_18.py':
        return green6_18(file)
    if option == 'green7_18.py':
        return green7_18(file)
    
    # random
    if option == 'rock_paper_scissors.py':
        return rock_paper_scissors(file)
    
    
    # old stuff
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
    if option == 'leftStack.py':
        return leftStack(file)
    if option == 'rightStack.py':
        return rightStack(file)
    '''
    options = ('leftStack.py', 'rightStack.py', 'pyramid.py')
    if any(routine in option for routine in options):
        return pyramidStacks(file)
        '''
    if option == 'binary_search.py': 
        return binary_search(file)
    if option == 'validate.py':
        return validate(file)
    if option == 'validate_functions.py':
        return validate_functions(form)
    if option == 'lottery.py':
        return lottery(file)

#++++++++++++++++++++++++++++ chapter 1 ++++++++++++++++++++++++
def ch1_1(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = 'Welcome to Python\r\nWelcome to Computer Science\r\nProgramming is fun\r\n'
    # check the correctness of the submission
    assess(child, "ch1_1.py", key)
    

def ch1_2(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = 'FFFF  U    U  N    N\r\nF     U    U  NN   N\r\nFFFF  U    U  N N  N\r\nF     U    U  N  N N\r\nF      UUUU   N   NN\r\n'
    # check the correctness of the submission
    assess(child, "ch1_2.py", key)
    

def ch1_3(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = ' ---------\r\n|  O   O  |\r\n|    U    |\r\n|  \___/  |\r\n|         |\r\n ---------'
    # check the correctness of the submission
    assess(child, "ch1_3.py", key)


def ch1_4(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = '{0:7s}{1:7s}{2:s}\r\n'.format('a', 'a^2', 'a^3') + '{0:<7d}{1:<7d}{2:d}\r\n'.format(1, 1, 1) +\
                '{0:<7d}{1:<7d}{2:d}\r\n'.format(2, 4, 16) + '{0:<7d}{1:<7d}{2:d}\r\n'.format(3, 9, 27) + \
                '{0:<7d}{1:<7d}{2:d}\r\n'.format(4, 16, 64)
    # check the correctness of the submission
    assess(child, "ch1_4.py", key)
    
 
def ch1_5(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = str((9.5 *4.5-2.5*3)/(45.5-3.5))
    # check the correctness of the submission
    assess(child, "ch1_5.py", key)
    

def ch1_6(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = 'area is {0:.2f}\r\nperimeter is {1:.2f}\r\n'.format(4.5 * 7.9, (2 * 4.5 + 2 * 7.9))
    # check the correctness of the submission
    assess(child, "ch1_6.py", key)
    
#++++++++++++++++++++++ chapter 2 ++++++++++++++++++++++++++++++++++++++

def ch2_1(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = '24 Celsius is 75.2 Fahrenheit'
    child.sendline('24')
    # check the correctness of the submission
    assess(child, "ch2_1.py", key)
    

def ch2_2(file):
    child = pexpect.spawnu(f'python3 {file}')
    PI = 3.14159
    radius = round(random.uniform(8, 1), 1)
    length = round(random.uniform(15, 1), 1)
    child.sendline('{}, {}'.format(radius, length))
    key = 'The area is {}\r\nThe volume is {}'.format(PI * radius**2, PI * radius**2 * length)
    assess(child, "ch2_2.py", key)
    
 
def ch2_3(file):
    child = pexpect.spawnu(f'python3 {file}')
    feet = round(random.uniform(30, 1), 2)
    child.sendline(str(feet))
    key = '{} feet is {} meters'.format(feet, feet * .305)
    assess(child, "ch2_3.py", key)
    
            
def ch2_4(file):
    child = pexpect.spawnu(f'python3 {file}')
    pounds = round(random.uniform(200, 1), 2)
    child.sendline(str(pounds))
    key = '{} pounds is {} kilograms'.format(pounds, pounds * .454)
    assess(child, "ch2_4.py", key)


def ch2_5(file):
    child = pexpect.spawnu(f'python3 {file}')
    subtotal = round(random.uniform(80, 1), 2)
    rate = round(random.uniform(20, 10))
    child.sendline('{}, {}'.format(subtotal, rate))
    key = 'The gratuity is {0:.2f} and the total is {1:.2f}'.format(subtotal * (rate/100), subtotal * (1 + (rate/100)))
    assess(child, "ch2_5.py", key)
            
            
def ch2_6(file):
    child = pexpect.spawnu(f'python3 {file}')
    num = random.randint(0, 1000)
    child.sendline(str(num))
    key = 'The sum of the digits is {}'.format((num % 10) + ((num // 10) % 10) + ((num // 100) % 10))
    # check the correctness of the submission
    assess(child, "ch2_6.py", key)
            

def ch2_7(file):
    child = pexpect.spawnu(f'python3 {file}')
    minutes = random.randint(0, 1000000000)
    child.sendline(str(minutes))
    key = '{} minutes is approximately {} years and {} days'.format(minutes, minutes // 525600, (minutes % 525600) // 1440)
    assess(child, "ch2_7.py", key)


def ch2_8(file):
    child = pexpect.spawnu(f'python3 {file}')
    data = [round(random.uniform(100,20), 1), round(random.uniform(20,1), 1), round(random.uniform(20,1), 1)]
    for each in data:
        child.sendline(str(each))
    key = 'The energy needed is {:.1f}'.format(data[0] * (data[2] - data[1]) * 4184)
    assess(child, "ch2_8.py", key)
            
            
def ch2_9(file):
    child = pexpect.spawnu(f'python3 {file}')
    t = round(random.uniform(41, -58), 1)
    v = random.randint(2, 80)
    child.sendline(str(t))
    child.sendline(str(v))
    key = 'The wind chill index is {:.5f}'.format(35.74 + 0.621 * t - 35.75 * v**0.16 + 0.4275 * t * v**0.16)
    assess(child, "ch2_9.py", key)


def ch2_10(file):
    child = pexpect.spawnu(f'python3 {file}')
    v = round(random.uniform(210, 80), 1)
    a = round(random.uniform(10, 3), 1)
    child.sendline('{}, {}'.format(v, a))
    key = 'The minimum runway length for this airplane is {:.3f} meters'.format((v**2)/(2*a))
    assess(child, "ch2_10.py", key)
    

def ch2_13(file):
    child = pexpect.spawnu(f'python3 {file}')
    n = random.randint(1111, 9999)
    F = 1000
    child.sendline(str(n))
    data =[]
    data.append(n // 1000)
    n %= 1000
    data.append(n // 100)
    n %= 100
    data.append(n // 10)
    n%= 10
    data.append(n)
    key = '{}\r\n{}\r\n{}\r\n{}'.format(data[0], data[1], data[2], data[3])
    assess(child, "ch2_13.py", key)
    
    
def ch2_14(file):
    child = pexpect.spawnu(f'python3 {file}')
    data = []
    for each in range(6):
        data.append(round(random.uniform(10,-10), 1))
    child.sendline('{}, {}, {}, {}, {}, {}'.format(data[0], data[1], data[2], data[3], data[4], data[5]))
    key = '{}\r\n{}\r\n{}\r\n{}'.format(data[0], data[1], data[2], data[3])
    s1 = ((data[0] - data[2])**2 + (data[1] - data[3])**2)**.5
    s2 = ((data[2] - data[4])**2 + (data[3] - data[5])**2)**.5
    s3 = ((data[4] - data[0])**2 + (data[5] - data[1])**2)**.5
    s = (s1 + s2 + s3) / 2
    area = (s * (s - s1) * (s - s2) * (s - s3))**.5
    key = 'The area of the triangle is {:.1f}'.format(area)
    assess(child, "ch2_14.py", key)
            

def ch2_15(file):
    child = pexpect.spawnu(f'python3 {file}')
    s = round(random.uniform(15, 5), 1)
    child.sendline(str(s))
    key = 'The area of the hexagon is {0:.2f}'.format(((3*3**.5) / 2) * s**2)
    assess(child, "ch2_15.py", key)


def ch2_18(file):
    child = pexpect.spawnu(f'python3 {file}')
    offset = random.randint(-10, -3)
    child.sendline(str(offset))

    currentTime = time.time()# get current time
    # obtain the total seconds since midnight Jan 1, 1970 
    totalSeconds = int(currentTime)
    # get the current second
    currentSecond = totalSeconds % 60
    # get the total minutes
    totalMinutes = totalSeconds // 60
    # compute the current minute in the hour
    currentMinute = totalMinutes % 60
    # obtain the total hours
    totalHours = totalMinutes // 60
    # compute the current hour
    currentHour = totalHours % 24
   
    key = f"Current time is {currentHour + offset}:{currentMinute}:{currentSecond}"
    
    assess(child, 'ch2_18.py', key)


def ch2_19(file):
    investmentAmount = random.randint(1200, 50000)
    annualInterestRate = round(random.uniform(1, 7), 2)
    years = random.randint(1, 10)

    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(str(investmentAmount))
    child.sendline(str(annualInterestRate))
    child.sendline(str(years))

    annualInterestRate /= 100
    monthlyInterestRate = annualInterestRate / 12
    numberOfMonths = years * 12
    futureInvestmentAmount = investmentAmount * (1 + monthlyInterestRate) ** numberOfMonths
    key = f"Accumulated value is ${futureInvestmentAmount:.2f}"
    assess(child, 'ch2_19.py', key)


def ch2_20(file):
    balance = random.randint(1200, 50000)
    rate = round(random.uniform(1, 7), 2)
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(f"{balance}, {rate}")
    interest = balance * (rate / 1200)
    key = f"The interest is ${interest:.2f}"
    assess(child, 'ch2_20.py', key)


def ch2_21(file):
    
    principal = random.randint(100, 1000)
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(str(principal))
    m1 = principal * (1 + .00417)
    for i in range(5):
        m1 = (principal + m1) * (1 + .00417)
    key = f"After the sixth month, the account value is ${m1:.2f}"
    assess(child, 'ch2_21.py', key)
    

#++++++++++++++++++++++++ Chapter 3 ++++++++++++++++++++++++++++++++++++++++++++
    
def ch3_1(file):
    child = pexpect.spawnu(f'python3 {file}')
    s = round(random.uniform(15, 1), 1)
    child.sendline(str(s))
    side = 2 * s * math.sin((math.pi / 5))
    area = (3 * math.sqrt(3) / 2) * math.pow(side, 2)
    key = f"The area of the pentagon is {area:.2f}"
    assess(child, "ch3_1.py", key)
      

def ch3_2(file):
    child = pexpect.spawnu(f'python3 {file}')
    data = []
    for i in range(4):
        data.append(round(random.uniform(100, -100), 1))
   
    child.sendline(f"{data[0]}, {data[1]}")
    child.sendline(f"{data[2]}, {data[3]}")
    
    for i, each in enumerate(data):
        data[i] = math.radians(data[i])
  
    d = 6371.01 * math.acos(math.sin(data[0]) * math.sin(data[2]) + math.cos(data[0]) * math.cos(data[2]) * math.cos(data[1] - data[3]))

    key = f"The distance between two points is {d:.4f} km"
    assess(child, "ch3_2.py", key)
    
    
def ch3_4(file):
    child = pexpect.spawnu(f'python3 {file}')
    s = round(random.uniform(15, 1), 1)

    child.sendline(str(s))
    area = (5 * s**2) / (4 * math.tan((math.pi / 5)))

    key = f"The area of a pentagon is {area:.2f}"
    assess(child, "ch3_4.py", key)
    

def ch3_5(file):
    child = pexpect.spawnu(f'python3 {file}')
    n = round(random.uniform(15, 1), 1)
    s = round(random.uniform(15, 1), 1)

    child.sendline(str(n))
    child.sendline(str(s))

    area = (n * s**2) / (4 * math.tan((math.pi / n)))

    key = f"The area of a pentagon is {area:.2f}"
    assess(child, "ch3_5.py", key)


def ch3_6(file):
    child = pexpect.spawnu(f'python3 {file}')
    n = random.randint(0, 127)
    child.sendline(str(n))
    key = f"The character is {chr(n)}"
    assess(child, "ch3_6.py", key)
            
            
def ch3_7(file):
    child = pexpect.spawnu(f'python3 {file}')
    child.expect(pexpect.EOF)
    if child.before.strip() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        # pass
        print(f"{BY}Output is correct!\n\n{G}{child.before}\n{BY}:) ch3_7.py == passed!{X}")
    # fail
    else:
        print(f"{BY}Expected output of:\n\n{R}{'a capital letter'}\n{BY}Actual output was:\n\n{R}{child.before}\n{BY}:( ch3_7.py == failed{X}")
            

def ch3_11(file):
    child = pexpect.spawnu(f'python3 {file}')
    n = random.randint(0, 9999)
    child.sendline(str(n))
    thousands = n // 1000
    remainder = n % 1000
    hundreds = remainder // 100
    remainder = n % 100
    tens = remainder // 10
    ones = remainder % 10
    key = f"{n} reversed is {ones}{tens}{hundreds}{thousands}"
    assess(child, "ch3_11.py", key)
    
            
#++++++++++++++++++++++++++++++ Chapter 4 ++++++++++++++++++++++++++++++++++++++

def ch4_1(file):
    def genCoefficients():
        while True:
            a = random.randint(-5, 5)
            b = random.randint(-5, 5)
            c = random.randint(-5, 5)
            discriminant = b**2 - 4 * a * c
            if 2 * a == 0:
                continue
            else:
                return a, b, c, discriminant

    # test case 1: d < 0, no roots
    a, b, c, discriminant = genCoefficients()
    while discriminant >= 0:
        a, b, c, discriminant = genCoefficients()
    key = "The equation has no real roots"
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(f"{a}, {b}, {c}")
    assess(child, "ch4_1.py case 1", key)
    
    # test case 2: d == 0, one root
    while discriminant != 0:
        a, b, c, discriminant = genCoefficients()
    singleRoot = -b / (2 * a)
    key = f"The root is {singleRoot:.2f}"
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(f"{a}, {b}, {c}")
    assess(child, "ch4_1.py case 2", key)
     
    # test case 3: d > 0, two roots
    while discriminant <= 0:
        a, b, c, discriminant = genCoefficients()
    pRoot = (-b + math.pow(discriminant, .5)) / (2 * a)
    nRoot = (-b - math.pow(discriminant, .5)) / (2 * a)
    key = f"The roots are {pRoot:.2f} and {nRoot:.2f}"
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(f"{a}, {b}, {c}")
    assess(child, "ch4_1.py case 3", key)


def ch4_2(file):
    def computeSum(child):
        message = child.read_nonblocking(size=20, timeout=-1).strip()
        operands = []
        for i in message:
            if i.isdigit():
                operands.append(int(i))
        total = operands[0] + operands[1] + operands[2]
        child.sendline(str(total))
        return message, operands, total
        
    child = pexpect.spawnu(f'python3 {file}')
    message, operands, total = computeSum(child)
    key = f'{operands[0]} + {operands[1]} + {operands[2]} = {total} is True'
    assess(child, 'ch4_2.py: case 1', key, f'{message} ')
    
    child = pexpect.spawnu(f'python3 {file}')
    message, operands, total = computeSum(child)
    key = f'{operands[0]} + {operands[1]} + {operands[2]} = {total} is False'
    assess(child, 'ch4_2.py: case 2', key, f'{message} ')
    
    
def ch4_3(file):
    
    def genCoefficients():
        data = []
        for i in range(6):
            data.append(round(random.randint(-15, 15), 1))
        return data
    
    # case 1
    data = genCoefficients()
    while data[0] * data[3] - data[1] * data[2] == 0:
        data = genCoefficients()
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}")
    x = (data[4] * data[3] - data[1] * data[5]) / (data[0] * data[3] - data[1] * data[2])
    y = (data[0] * data[5] - data[4] * data[2]) / (data[0] * data[3] - data[1] * data[2])
    key = f"x is {x:.1f} and y is {y:.1f}"
    assess(child, "ch4_3.py: case 1", key)
    
    # case 2
    data = genCoefficients()
    while data[0] * data[3] - data[1] * data[2] != 0:
        data = genCoefficients()
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}")
    key = "The equation has no solution"
    assess(child, "ch4_3.py: case 2", key)
    

def ch4_4(file):
    child = pexpect.spawnu(f'python3 {file}')
    inputOutput = child.read_nonblocking(size=18, timeout=-1)
    operands = getOperands(inputOutput)
    child.sendline(str(sum(operands)))
    key = f'{operands[0]} + {operands[1]} + {operands[2]} = {sum(operands)} is True'
    assess(child, f'{file}: case 2', key, inputOutput)
    
    child = pexpect.spawnu(f'python3 {file}')
    inputOutput = child.read_nonblocking(size=18, timeout=-1).strip()
    operands = getOperands(inputOutput)
    total = sum(operands) + random.randint(-5, 5)
    child.sendline(str(total))
    key = f'{operands[0]} + {operands[1]} + {operands[2]} = {total} is False'
    assess(child, f'{file}: case 2', key, inputOutput)
    

def ch4_5(file):
    for i in range(3):
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        day = random.randint(0, 6)
        f = random.randint(2, 6)
        future = (day + f) % 7
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline(str(day))
        child.sendline(str(f))
        key = f'Today is {days[day]} and the future day is {days[future]}'
        assess(child, f'ch4_5.py try {i + 1}', key)
        

def ch4_6(file):
    weight = random.randint(150, 230)
    feet = random.randint(4, 6)
    inch = random.randint(0, 11)
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(str(weight))
    child.sendline(str(feet))
    child.sendline(str(inch))

    height = (feet * 12) + inch

    KILOGRAMS_PER_POUND = 0.45359237 # Constant
    METERS_PER_INCH = 0.0254 # Constant
    
    # Compute BMI
    weightInKilograms = weight * KILOGRAMS_PER_POUND
    heightInMeters = height * METERS_PER_INCH
    bmi = weightInKilograms / (heightInMeters * heightInMeters)
    
    # Display result
    s1 = f'BMI is {bmi:.2f}'
    if bmi < 18.5:
        s2 = 'Underweight'
    elif bmi < 25:
        s2 = 'Normal'
    elif bmi < 30:
        s2 = 'Overweight'
    else:
        s2 = 'Obese'
    key = f'{s1}\r\n{s2}'
    assess(child, f'ch4_6.py', key)
    

def ch4_7(file):

    def getMoney(amount):
        remainingAmount = int(amount * 100)
        oneDollars = remainingAmount // 100
        remainingAmount = remainingAmount % 100
        quarters = remainingAmount // 25
        remainingAmount = remainingAmount % 25
        dimes = remainingAmount // 10
        remainingAmount = remainingAmount % 10
        nickels = remainingAmount // 5
        pennies = remainingAmount % 5
        return [oneDollars, quarters, dimes, nickels, pennies]


    def getResult(amount, money):
        result = f'Your amount ${amount} consists of\r\n'
        if money[0] >= 1:
            if money[0] == 1:
                result += f'\t{money[0]} dollar\r\n'
            else:
                result += f'\t{money[0]} dollars\r\n'
        if money[1] >= 1:
            if money[1] == 1:
                result += f'\t{money[1]} quarter\r\n'
            else:
                result += f'\t{money[1]} quarters\r\n'
        if money[2] >= 1:
            if money[2] == 1:
                result += f'\t{money[2]} dime\r\n'
            else:
                result += f'\t{money[2]} dimes\r\n'
        if money[3] >= 1:
            if money[3] == 1:
                result += f'\t{money[3]} nickel\r\n'
            else:
                result += f'\t{money[3]} nickels\r\n'
        if money[4] >= 1:
            if money[4] == 1:
                result += f'\t{money[4]} penny\r\n'
            else:
                result += f'\t{money[4]} pennies\r\n'
        return result
        
    amount = [0.13, 1.41, 4.69]
    # amount = round(random.uniform(0, 6), 2)
    
    for i in range(3):
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline(str(amount[i]))
        money = getMoney(amount[i])
        key = getResult(amount[i], money)
        assess(child, f'ch4_7.py case {i + 2}', key)
        
    
def ch4_8(file):
    
    data = [[-8,-5,-2], [8,9,7], [15,13,14]]
    for i in range(3):
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline(f'{data[i][0]}, {data[i][1]}, {data[i][2]}')
        greatest = max(data[i])
        lowest = min(data[i])
        for j in range(3):
            if data[i][j] != greatest and data[i][j] != lowest:
                middle = data[i][j]
        key = f'max: {greatest} middle: {middle} min: {lowest}'
        assess(child, f'ch4_8.py case {i + 1}', key)


def ch4_9(file):
    
    def getData():
        weight1 = random.randint(25, 100)
        price1 = round(random.uniform(30, 10),2)
        weight2 = random.randint(25, 100)
        price2 = round(random.uniform(30, 10),2)
        return price1, weight1, price2, weight2
    
    # case 1 Package 1 has better price
    child = pexpect.spawnu(f'python3 {file}')
    while True:
        price1, weight1, price2, weight2 = getData()
        if price1 / weight1 < price2 / weight2:
            break
    child.sendline(f'{weight1}, {price1}')
    child.sendline(f'{weight2}, {price2}')
    key = f'Package 1: ${price1/weight1:.2f}\r\nPackage 2: ${price2/weight2:.2f}\r\nPackage 1 has the better price.\r\n'
    assess(child, f'{file} case 1', key)
    
    # case 2 Package  has better price       
    child = pexpect.spawnu(f'python3 {file}')
    while True:
        price1, weight1, price2, weight2 = getData()
        if price1 / weight1 > price2 / weight2:
            break
    child.sendline(f'{weight1}, {price1}')
    child.sendline(f'{weight2}, {price2}')
    key = f'Package 1: ${price1/weight1:.2f}\r\nPackage 2: ${price2/weight2:.2f}\r\nPackage 2 has the better price.\r\n'
    assess(child, f'{file} case 2', key)
    
    # case 3 packages are same price
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(f'{1}, {1}')
    child.sendline(f'{1}, {1}')
    key = f'Package 1: ${1:.2f}\r\nPackage 2: ${1:.2f}\r\nThey are the same price.\r\n'
    assess(child, f'{file} case 3', key)


def ch4_10(file):
    child = pexpect.spawnu(f'python3 {file}')
    inputOutput = child.read_nonblocking(size=10, timeout=-1)
    operands = getOperands(inputOutput)
    child.sendline(str(operands[0] * operands[1]))
    key = 'correct :)'
    assess(child, f'{file} case 1', key, inputOutput)
    
    child = pexpect.spawnu(f'python3 {file}')
    inputOutput = child.read_nonblocking(size=10, timeout=-1)
    operands = getOperands(inputOutput)
    total =  operands[0] * operands[1] + random.randint(1, 9)
    child.sendline(str(total))
    key = 'incorrect :('
    assess(child, f'{file} case 2', key, inputOutput)

    
def ch4_12(file):
    number = random.randint(-1000, 1000)
    child = pexpect.spawnu(f'python3 {file}')
    while not (number % 5 == 0 and number % 6 == 0):
        number = random.randint(-1000, 1000)
    child.sendline(str(number))
    key = f'{number} is divisible by 5 and 6'
    assess(child, 'ch4_12.py case 1', key)
        
    child = pexpect.spawnu(f'python3 {file}')
    while not(number % 5 == 0 and number % 6 != 0):
        number = random.randint(-1000, 1000)
    child.sendline(str(number))
    key = f'{number} is divisible by 5'
    assess(child, 'ch4_12.py case 2', key)
    
    child = pexpect.spawnu(f'python3 {file}') 
    while not(number % 5 != 0 and number % 6 == 0):
        number = random.randint(-1000, 1000)
    child.sendline(str(number))
    key = f'{number} is divisible by 6'
    assess(child, 'ch4_12.py case 3', key)
    
    child = pexpect.spawnu(f'python3 {file}') 
    while not(number % 5 != 0 and number % 6 != 0):
        number = random.randint(-1000, 1000)
    child.sendline(str(number))
    key = f'{number} is not divisible by 5 or 6'
    assess(child, 'ch4_12.py case 4', key)
    

def ch4_16(file):
    child = pexpect.spawnu(f'python3 {file}')
    inputOutput = child.read_nonblocking(size=1, timeout=-1).strip()
    if 65<= ord(inputOutput) <= 90:
        print(f'{G}:) ch4_16.py == passed!{X}')
    else:
        print(f'{R}:( ch4_16.py failed{X}')


def ch4_17(file):
   
    def testChild(player, file):
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline(str(player))
        child.expect('computer is .*', timeout=-1)
        output = (child.after).split('\r\n')
        # Extract computer value
        computer = getIntegersFromString(output[0])[0]
        # Extract user submitted output
        computerOutput = output[1]
        child.terminate
        return computer, computerOutput
    
    
    def checkGame(player, computer):
        if computer == player:
            return 'it\'s a tie'
        # player is rock
        elif player == 0:
            if computer == 2:
                return 'rock beats scissors - you win'
            else:
                return 'paper beats rock - you lose'
        # player is paper
        elif player == 1:
            if computer == 0:
                return 'paper beats rock - you win'
            else:
                return 'scissor beats paper - you lose'
        else:
            if player == 2:
                if computer == 1:
                    return 'scissors beat paper'
                else:
                    return 'rock beats scissors'
    
    
    def testKey(computerOutput, key, case):
        if computerOutput == key:
            print(f'{BY}Output is correct!')
            print(f'\n{G}{key}')
            print(f'\n{BY}:) ch4_17.py case {case} == passed!{X}')
        else:
            print(f'{BY}Expected output of:\n\n{R}{key}')
            print(f'\n{BY}Actual output was:\n\n{R}{computerOutput}')
            print(f'{BY}:( ch4_17.py test case {case} == failed{X}')
    case = 0
    for player in range(3):
        for computerValue in range(3):
            case += 1
            while True:
                computer, computerOutput = testChild(player, file)
                if computer == computerValue:
                    break
            key = checkGame(player, computer)
            testKey(computerOutput, key, case)
    

def ch4_24(file):
    def createDeck():
        """generates a deck of cards"""
        cards = []
        for number in range(2, 11):
            cards.extend([str(number) + suite for suite in ['\u2664', '\u2661', '\u2662', '\u2667']])
        for face in 'JQKA':
            cards.extend([face + suite for suite in  ['\u2664', '\u2661', '\u2662', '\u2667']])
        random.shuffle(cards)
        return cards
    
    cards = createDeck()
    child = pexpect.spawnu(f'python3 {file}')
    inputOutput = child.read_nonblocking(size=5, timeout=-1).strip()
    print(f'{Y}{inputOutput}{X}')
    if inputOutput in cards:
        print(f'{G}:) ch4_24.py == passed!{X}')
    else:
        print(f'{R}:( ch4_24.py failed{X}')
#+++++++++++++++++++++++++++++ Chapter 5 +++++++++++++++++++++++++++++++++++++++

def ch5_1(file):
    # generate integers for test case 1
    integers = []
    for i in range(random.randint(4, 11)):
        sign = random.randint(0, 1)
        if sign == 0:
            integers.append(random.randint(1, 20))
        else:
            integers.append(random.randint(-20, -1))
    integers.append(0)
    
    # summarize the data for case 1
    tally, positives, negatives, total = 0, 0, 0, 0
    for i in integers:
        if i != 0:
            tally += 1
            if i > 0:
                positives += 1
            else:
                negatives +=1
            total += i
    average = total / tally
    
    # generate the output for test case 1
    key = f'The number of positives is {positives}\r\n'
    key += f'The number of negatives is {negatives}\r\n'
    key += f'The total is {total}\r\n'
    key += f'The average is {average:.2f}\r\n'
    child = pexpect.spawnu(f'python3 {file}')
    # send the input
    for i in integers:
        child.sendline(str(i))
    # test the output
    assess(child, f'ch5_1.py Case 1', key)
    # test case 2
    child = pexpect.spawnu(f'python3 {file}')
    # send the input
    child.sendline(str(0))
    # correct output
    key = 'You didn\'t enter any number\r\n'
    # test the output
    assess(child, f'ch5_1.py Case 2', key)


def ch5_2(file):
    DELAY = .1
    CORRECT_LENGTH = 12
    WRONG_LENGTH = 26
    print(f'{BY}!!!+++Time may be off and cause a failure+++!!!{X}')
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    start = time.time()
    for i in range(10):
        # capture child out
        expression = child.read_nonblocking(size=18, timeout=-1).strip()
        # extract numbers from child out
        numbers = getNumbers(expression)
        # determines if the response is 1 or 2 characters
        if len(str(sum(numbers))) == 1:
            size = 1
        else:
            size = 2
        # prints the question
        print(f'{P}{expression} {B}{str(sum(numbers))}{X}')
        # sends the correct response
        child.sendline(str(sum(numbers)))
        # delays so that all text is present before flushing
        time.sleep(DELAY)
        # flushes the inbetween text
        child.read_nonblocking(size=CORRECT_LENGTH + size, timeout=-1)

    duration = time.time() - start -.1
    key = f'You got 10 out of 10 correct\r\nTest time is {duration:.1f} seconds'
    assess(child, f'ch5_2.py Case 1', key)
    child.terminate()
    
    print(f'{BY}!!!+++Time may be off and cause a failure+++!!!{X}')
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    start = time.time()
    for i in range(10):
        # capture child out
        expression = child.read_nonblocking(size=18, timeout=-1).strip()
        # extract numbers from child out
        numbers = getNumbers(expression)
        # determines if the response is 1 or 2 characters
        if len(str(sum(numbers))) == 1:
            size = 1
        else:
            size = 2
        print(f'{P}{expression} {B}{str(sum(numbers))}{X}')
        # sends the correct response
        child.sendline(str(sum(numbers) + 1))
        # delays so that all text is present before flushing
        time.sleep(DELAY)
        # flushes the inbetween text
        child.read_nonblocking(size=WRONG_LENGTH + size, timeout=-1)

    duration = time.time() - start
    key = f'You got 0 out of 10 correct\r\nTest time is {duration:.1f} seconds'
    assess(child, f'ch5_2.py Case 2', key)


def ch5_3(file):
    key = f'{"Kilograms":13}{"Pounds":>6}\r\n'
    kilograms = 1
    while kilograms <= 199:
        pounds = kilograms * 2.2
        key += f'{kilograms:<13}{pounds:>6.1f}\r\n'
        kilograms += 2
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    assess(child, f'ch5_3.py', key)
    
    
def ch5_4(file):
    key = f'{"Miles":7}Kilometers\r\n'
    miles = 1
    while miles <= 10:
        kilometers = miles * 1.609
        key += f'{miles:<7}{kilometers:.3f}\r\n'
        miles += 1
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    assess(child, f'ch5_4.py', key)


def ch5_5(file):
    key = f'{"Kilograms":<11}{"Pounds":<7}| {"Pounds":<7}{"Kilograms":<9}\r\n'
    kilograms1 = 1
    pounds2 = 20
    while kilograms1 <= 199:
        pounds1 = kilograms1 * 2.2 
        kilograms2 = pounds2 * .4536
        key += f'{kilograms1:<11}{pounds1:<7.1f}| {pounds2:<7}{kilograms2:<9.2f}\r\n'
        kilograms1 += 2
        pounds2 += 5
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    assess(child, f'ch5_5.py', key)


def ch5_6(file):
    key = f'{"Miles":<7}{"Kilometers":<11}| {"Kilometers":<11}{"Miles":<6}\r\n'
    miles1 = 1
    kilometers2 = 20
    while miles1 <= 10:
        kilometers1 = miles1 * 1.609 
        miles2 = kilometers2 * .621
        key += f'{miles1:<7}{kilometers1:<11.3f}| {kilometers2:<11}{miles2:<6.3f}\r\n'
        miles1 += 1
        kilometers2 += 5
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    assess(child, f'ch5_6.py', key)


def ch5_7(file):
    key = f'{"Degree":<8}{"Sin":<10}{"Cos":<6}\r\n'
    degree = 0
    while degree <= 360:
        sin = math.sin(math.radians(degree))
        cos = math.cos(math.radians(degree))
        key += f'{degree:<8}{sin:<10.4f}{cos:<6.4f}\r\n'
        degree += 10
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    assess(child, f'ch5_7.py', key)


def ch5_8(file):
    key = f'{"Number":<8}{"Square Root":<11}\r\n'
    number = 0
    while number <= 20:
        root = math.sqrt(number)
        key += f'{number:<8}{root:<11.4f}\r\n'
        number += 1
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    assess(child, f'ch5_8.py', key)


def ch5_11(file):
    
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    NUM_OF_STUDENTS = random.randint(2, 9)
    child.sendline(str(NUM_OF_STUDENTS))
    grades = []
    for i in range(NUM_OF_STUDENTS):
        temp = random.randint(50, 100)
        child.sendline(str(temp))
        grades.append(temp)
    highScore, runnerUp = 0, 0
    for i in grades:
        if i > highScore:
            runnerUp = highScore
            highScore = i
        else:
            if i > runnerUp:
                runnerUp = i
    key = f'High Score: {highScore} Second Highest Score: {runnerUp}'
    assess(child, f'ch5_11.py Case 1', key)
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline('0')
    key = '0 was entered for the number of students'
    assess(child, f'ch5_11.py Case 2', key)
    

def ch5_12(file):
    
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    key = ''
    i = 100
    while i <= 1000:
        count = 0
        line = ''
        while count < 10 and i <= 1000:
            if i % 5 == 0 and i % 6 == 0:
                line += str(i)
                count += 1
                if count != 10:
                    line += ' '
            i += 1
        key += f'{line}\r\n' 
    assess(child, f'ch5_12.py', key)
    
    
def ch5_13(file):
    
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    key = ''
    i = 100
    while i <= 200:
        count = 0
        key = ''
        line = ''
        while count < 10 and i <= 200:
            if i % 5 == 0 or i % 6 == 0 and not(i % 5 == 0 and i % 6 == 0):
                line += str(i)
                count += 1
                if count != 10:
                    line += ' '
            i += 1
        key += f'{line}\r\n' 
    assess(child, f'ch5_13.py', key)  
    
    
def ch5_14(file):
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    key = ''
    n = 0
    while n**2 < 12000:
        key += f'{n} is not the answer\r\n'
        n += 1
    key += f'{n} is the answer\r\n'
    assess(child, f'ch5_14.py', key)  
       

def ch5_15(file):
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    key = ''
    n = 1
    while n**3 < 12000:
        n += 1
    key += f'{n - 1}\r\n'
    assess(child, f'ch5_15.py', key)  


def ch5_17(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = ''
    for char in range(33, 127, 10):
        for each in range(10):
            key += f'{chr(char)} '
            char += 1
        key += '\r\n'
    assess(child, f'{file}', key)


def ch5_19(file):
    child = pexpect.spawnu(f'python3 {file}')
    height = random.randint(2, 9)
    child.sendline(str(height))
    spaces = height * 2 - 2
    key = ''
    for digit in range(1, height + 1):
        for space in range(spaces):
            key +=' '
        digitCopy = digit
        while digitCopy > 1:
            key += f'{digitCopy} '
            digitCopy -= 1
        while digitCopy <= digit:
            key += f'{digitCopy} '
            digitCopy += 1
        spaces -= 2
        key += '\r\n'
    assess(child, file, key)


def ch5_20A(file):
    child = pexpect.spawnu(f'python3 {file}')
    key = ''
    for row in range(1, 7):
        for digit in range(row):
           key += f'{digit + 1} '
        key += '\r\n'
    assess(child, file, key)
   

def ch5_20B(file):
    child = pexpect.spawnu(f'python3 {file}')
    height = 6
    key = ''
    for row in range(1, 7):
        for digit in range(1, height + 1):
            key += f'{digit} '
        height -= 1
        key += '\r\n'
    assess(child, file, key)   

#def ch5_20C(file):
#def ch5_20D(file):
def ch5_21(file):
    # generate python instance
    child = pexpect.spawnu(f'python3 {file}')
    key = ''
    LINES = 8
    spaces = LINES * 4 - 4
    # loops for the number of rows
    for i in range(1, LINES + 1):
        output = ''
        # creates the spaces part of the row
        for j in range(spaces):
            output += ' '
        
        # creates the left digits decreasing part of a row
        power = 0
        for j in range(i):
            output += f'{str(2 ** power):>4}'
            power += 1
            
        
        # creates the right digits increasing part of a row
        power = i - 2
        for j in range(i - 1):
            output += f'{str(2 ** power):>4}'
            power -= 1
        key += f'{output}\r\n'
        
        # update counters
        spaces -= 4
    assess(child, f'ch5_21.py', key)
    

#++++++++++++++++++++++++++Chapter 6++++++++++++++++++++++++++++++++++++++++++++

def ch6_2(file):
    child = pexpect.spawnu(f'python3 {file}')
    n = random.randint(0, 9999)
    
    child.sendline(str(n))
    total = n // 1000
    remainder = n % 1000
    total += remainder // 100
    remainder = n % 100
    total += remainder // 10
    total += remainder % 10
    
    key = f'The sum of the numbers is {total}'
    assess(child, "ch6_2.py", key)


def ch6_3(file):
    child = pexpect.spawnu(f'python3 {file}')
    n = random.randint(1111, 9999)
    
    child.sendline(str(n))
    thousands = n // 1000
    remainder = n % 1000
    hundreds = remainder // 100
    remainder = n % 100
    tens = remainder // 10
    ones = remainder % 10
    
    key = f'{n} reversed is {ones}{tens}{hundreds}{thousands}'
    assess(child, "ch6_3.py", key)


def ch6_4(file):
    # Test case 1 no palindrome
    child = pexpect.spawnu(f'python3 {file}')
    not_palindrome = str(random.randint(1, 4))
    not_palindrome += str(random.randint(0, 9))
    not_palindrome += str(random.randint(0, 9))
    not_palindrome += str(random.randint(5, 9))
    child.sendline(not_palindrome)
    key = f'No {not_palindrome} is not a palindrome'
    assess(child, 'ch6_4.py Case 1', key)
    
    # Test case 2 palindrome
    child = pexpect.spawnu(f'python3 {file}')
    outers = str(random.randint(1, 9))
    inners = str(random.randint(1, 9))
    palindrome = outers + inners * 2 + outers
    child.sendline(palindrome)
    key = f'Yes {palindrome} is a palindrome'
    assess(child, 'ch6_4.py Case 2', key)
    
        
def ch6_5(file):
    child = pexpect.spawnu(f'python3 {file}')
    numbers = [random.randint(50, 300), random.randint(-100, 30), random.randint(-200, 200)]
    child.sendline(f'{numbers[0]}, {numbers[1]}, {numbers[2]}')
    numbers.sort()
    key = f'The sorted numbers are {numbers[0]}, {numbers[1]}, {numbers[2]}'
    assess(child, 'ch6_5.py', key)
    

def ch6_6(file):
    child = pexpect.spawnu(f'python3 {file}')
    rows = random.randint(0, 9)
    child.sendline(str(rows))
    spaces = rows - 1
    key = ''
    for row in range(rows):
        for spaces in range(spaces):
            key += '  '
        digits = row + 1
        for nums in range(row + 1):
            key += f'{digits} '
            digits -= 1
        key += '\r\n'
    assess(child, 'ch6_6.py', key)
            

def ch6_7(file):
   
    def future_value(principle, annual_rate, years):
        # Computes the return on an investment
        annual_rate /= 100
        monthly_rate = annual_rate / 12
        months = years * 12
        future_amount = principle * (1 + monthly_rate) ** months
        return future_amount


    def create_table(principle, annual_rate, years):
        # Creates a printable table of the loan data
        table = f'{"Years":7}{"Future Value":12}\r\n'
        for year in range(1, years + 1):
            table += f'{year:<7}{future_value(principle, annual_rate, year):<12.2f}\r\n'
        return table
    
    
    child = pexpect.spawnu(f'python3 {file}')
    principle = random.randint(1000, 80000)
    rate = random.randint(3, 6)
    years = random.randint(4, 15)
    child.sendline(str(principle))
    child.sendline(str(rate))
    child.sendline(str(years))
    table = f'{create_table(principle, rate, years)}\r\n'
    
    assess(child, 'ch6_7.py', table)
    

def ch6_8(file):
    def celsius_to_fahreneit(celsius):
        # Converts from Celsius to Fahrenheit
        return (9 / 5) * celsius + 32

    def fahrenheit_to_celsius(fahrenheit):
        # Converts from Fahrenheit to Celsius
        return (5 / 9) * (fahrenheit - 32)
    
    child = pexpect.spawnu(f'python3 {file}')
    fahrenheit = 120.0
    table = ''
    table +=f'{"Celsius":<10}{"Fahrenheit":<12}|  {"Fahrenheit":<12}{"Celsius":<10}\r\n'
    for row in range(40, 30, -1):
        f_temp = celsius_to_fahreneit(float(row))
        c_temp = fahrenheit_to_celsius(fahrenheit)
        table += f'{float(row):<10.1f}{f_temp:<12.1f}|  {fahrenheit:<12.1f}{c_temp:<10.2f}\r\n'
        fahrenheit -= 10
    assess(child, 'ch6_8.py', table)
    
    
def ch6_9(file):
    def ft_to_m(foot):
        # Converts from feet to meters
        return 0.305 * foot


    def m_to_ft(meter):
        # Converts from meters to feet
        return meter / 0.305
        
    child = pexpect.spawnu(f'python3 {file}')
    meter = 20.0
    table = ''
    table += f'{"Feet":<10}{"Meters":<8}|  {"Meters":<10}{"Feet":<10}\r\n'
    for foot in range(1, 11):
        to_meter = ft_to_m(foot)
        to_foot = m_to_ft(meter)
        table += f'{float(foot):<10.1f}{to_meter:<8.3f}|  {meter:<10.1f}{to_foot:<10.3f}\r\n'
        meter += 6
    assess(child, 'ch6_9.py', table)


def ch6_12(file):
    
    def print_chars(ch1, ch2, number_per_line):
        start = ord(ch1)
        the_string = ''
        while start <= ord(ch2):
            for i in range(number_per_line):
                the_string += chr(start)
                start += 1
                if start > ord(ch2):
                    break
            the_string += '\r\r\n'
        return the_string
    
    ch1 = chr(random.randint(33, 80))
    ch2 = chr(random.randint(81, 133))
    number_per_line = random.randint(5, 15)
    the_string = print_chars(ch1, ch2, number_per_line)
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(ch1)
    child.sendline(ch2)
    child.sendline(str(number_per_line))
    assess(child, 'ch6_12.py', the_string)


def ch6_13(file):
   
    def sum_series(i):
        # Computes the sum of a series
        total = 0
        for j in range(1, i + 1):
            total += j / (j + 1)
        return total
    
    answer_key = ''
    answer_key += f'{"i":10}{"m(i)":10}\r\n'
    for i in range(1, 21):
        total = sum_series(i)
        answer_key += f'{i:<10}{total:<10.4f}\r\n'
    child = pexpect.spawnu(f'python3 {file}')
    assess(child, 'ch6_13.py', answer_key)

#++++++++++++++++++++++++Chapter 8++++++++++++++++++++++++++++++++++++++++++++++

def ch8_1(file):
    tests = [['123456789', 'Valid SSN'], ['1234567890111213', 'Invalid SSN'],
            ['123-45-6789', 'Valid SSN'], ['123p45p6789', 'Invalid SSN'],
            ['1234567ok', 'Invalid SSN']]
    for i in range(5):
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline(tests[i][0])
        assess(child, f'ch8_1.py case {i + 1}', tests[i][1])


def ch8_2(file):
    words = ['hot', 'cold', 'cat', 'mouse', 'pizza', 'wet']
    
    def sub_pass(words):
        key = random.randint(0, len(words) - 1)
        key = words[key]
        for i in range(len(words)):
            key += words[random.randint(0, len(words) - 1)]
        return words[key], key
    
    def sub_fail(words):
        key = random.randint(0, len(words) - 1)
        key = ''
        for i in range(len(words)):
            if i != key:
                key += words[i]
        return words[key], key
    
    key, key = sub_pass(words)
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(key)
    child.sendline(key)
    assess(child, "ch8_2.py Case 1", 'is a substring')
    
    key, key = sub_fail(words)
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(key)
    child.sendline(key)
    assess(child, "ch8_2.py Case 2", 'not a substring')
    
    
def ch8_3(file):
    
    def valid():
        password = ''
        digits = random.randint(2, 5)
        alpha = 9 - digits
        for digit in range(digits):
            password += str(random.randint(0,9))
        for char in range(alpha):
            password += chr(random.randint(97, 122))
        return password
        
    def dig_invalid():
        password = str(random.randint(0,9))
        for char in range(8):
            password += chr(random.randint(97, 122))
        return password
    
    def char_invalid():
        password = ''
        for char in range(9):
            password += chr(random.randint(33, 122))
        return password
    
    def len_invalid():
        password = ''
        digits = random.randint(2, 4)
        alpha = 7 - digits
        for digit in range(digits):
            password += str(random.randint(0,9))
        for char in range(alpha):
            password += chr(random.randint(65, 90))
        return password
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(valid())
    assess(child, "ch8_3.py Case 1", 'valid password')
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(dig_invalid())
    assess(child, "ch8_3.py Case 2", 'invalid password')
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(char_invalid())
    assess(child, "ch8_3.py Case 3", 'invalid password')
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(len_invalid())
    assess(child, "ch8_3.py Case 4", 'invalid password')
    

def ch8_4(file):
    words = [['apparatus', 'a', 3], ['missippi', 'i', 3],
            ['penelope', 'e', 3], ['sassafras', 's', 4]]
    child = pexpect.spawnu(f'python3 {file}')
    index = random.randint(0, 3)
    child.sendline(f'{words[index][0]}, {words[index][1]}')
    assess(child, "ch8_4.py", str(words[index][2]))
    

def ch8_5(file):
    print('Under Construction :(')
    
    
def ch8_6(file):
    def count_letters(s1):
        s2 = ''
        for each in s1:
            if each not in s2:
                s2 += each
        return len(s2)
    
    for i in range(4):
        child = pexpect.spawnu(f'python3 {file}')
        test = library[random.randint(0, len(library) - 1)]
        child.sendline(test)
        assess(child, f'ch8_6.py test{i + 1}', str(count_letters(test)))


def ch8_7(file):
    def get_number(letter):
        if letter in 'ABC':
            return 2
        elif letter in 'DEF':
            return 3
        elif letter in 'GHI':
            return 4
        elif letter in 'JKL':
            return 5
        elif letter in 'MNO':
            return 6
        elif letter in 'PQRS':
            return 7
        elif letter in 'TUV':
            return 8
        else:
            return 9
   
    for i in range(4):
        child = pexpect.spawnu(f'python3 {file}')
        test = chr(random.randint(65, 90))
        child.sendline(test)
        assess(child, f'ch8_7.py test{i + 1}', str(get_number(test)))
    
    
def ch8_8(file):
    print('Under Construction :(')
    

def ch8_9(file):
    print('Under Construction :(')
    
    
def ch8_10(file):
    print('Under Construciton :(')
    
    
def ch8_11(file):
    def reverse(s):
        s2 = ''
        i = len(s) - 1
        while i >= 0:
            s2 += s[i]
            i -= 1
        return s2
        
    for i in range(4):
        child = pexpect.spawnu(f'python3 {file}')
        test = library[random.randint(0, len(library) - 1)]
        child.sendline(test)
        assess(child, f'ch8_11.py test{i + 1}', str(reverse(test)))
        
    
def ch8_12(file):
    print('Under Construction :(')


def ch8_13(file):
    def prefix(s1, s2):
        i = 0
        shortest = min(len(s1), len(s2))
        while s1[i] == s2[i] and i < shortest:
            i += 1
        if s1[0] != s2[0]:
            return 'no matches'
        else:
            return s1[:i]
        
    
    for i in range(3):
        tests = ['disinfection', 'distance', 'diolate', 'dissatisfactory', 
                'dissimilarities', 'dissatisfactory', 'disable', 'disagree',
                'onynx', 'onion', 'onbaord', 'online']
        child = pexpect.spawnu(f'python3 {file}')
        test1 = tests[random.randint(0, len(tests) - 1)]
        while True: 
            test2 = tests[random.randint(0, len(tests) - 1)]
            if test1 != test2:
                break
       
        child.sendline(test1)
        child.sendline(test2)
        assess(child, f'ch8_13.py test{i + 1}', str(prefix(test1, test2)))
    

#+++++++++++++++++++++++++++++++Chapter 10++++++++++++++++++++++++++++++++++++++

def ch10_1(file):
    students = [random.randint(21, 97) for each in range(random.randint(4, 7))]
    
    best = max(students)
    
    answer_key = ''
    for i in range(len(students)):
        if students[i] >= best - 10:
            answer_key+= f'Student {i} score is {students[i]} and grade is A\r\n'
        elif students[i] >= best - 20:
            answer_key += f'Student {i} score is {students[i]} and grade is B\r\n'
        elif students[i] >= best - 30:
            answer_key += f'Student {i} score is {students[i]} and grade is C\r\n'
        elif students[i] >= best - 40:
            answer_key += f'Student {i} score is {students[i]} and grade is D\r\n'
        else:
            answer_key += f'Student {i} score is {students[i]} and grade is F\r\n'
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(' '.join(str(n) for n in students))
    assess(child, f'ch10_1.py', answer_key)


def ch10_2(file):
    integers = [random.randint(1, 99) for each in range(random.randint(4, 9))]
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(' '.join(str(n) for n in integers))
    integers.reverse()
    assess(child, f'ch10_2.py', str(integers))
    

def ch10_3(file):
    integers = [random.randint(1, 100) for each in range(random.randint(3, 6))]
    num = random.randint(1, 50)
    for each in range(random.randint(2, 4)):
        integers.append(num)
    num = random.randint(51, 100)
    for each in range(random.randint(2, 4)):
        integers.append(num)
    random.shuffle(integers)
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(' '.join(str(n) for n in integers))
    
    integers.sort()
    numbers = []
    counts = []
    answer_key = ''
    for i in range(len(integers)):
        if integers[i] not in numbers:
            numbers.append(integers[i])
            counts.append(integers.count(integers[i]))
    
    for i in range(len(counts)):
        if counts[i] > 1:
            answer_key += f'{numbers[i]} occurs {counts[i]} times\r\n'
        else:
            answer_key += f'{numbers[i]} occurs {counts[i]} time\r\n'
    
    assess(child, f'ch10_3.py', answer_key)
    
    
def ch10_4(file):
    
    def data_summary(scores):
        average = int(sum(scores) / len(scores))
        
        above_average = 0
        below_average = 0
        equal = 0
        
        for score in scores:
            if score > average:
                above_average += 1
            elif score < average:
                below_average += 1
            else:
                equal += 1
        
        answer_key = f'average is {average}\r\n'
        if above_average > 0:
            answer_key += f'{above_average} above average\r\n'
        if below_average > 0:
            answer_key += f'{below_average} below average\r\n'
        if equal > 0:
            answer_key += f'{equal} equal\r\n'
        return answer_key
    
    reg_scores = [random.randint(30, 100) for each in range(random.randint(6, 10))]
    child = pexpect.spawnu(f'python3 {file}')
    answer_key = data_summary(reg_scores)
    child.sendline(' '.join(str(n) for n in reg_scores))
    assess(child, f'ch10_4.py Test 1', answer_key)
    
    equal_scores = [random.randint(75, 78) for each in range(10)]
    child = pexpect.spawnu(f'python3 {file}')
    answer_key = data_summary(equal_scores)
    child.sendline(' '.join(str(n) for n in equal_scores))
    assess(child, f'ch10_4.py Test 2', answer_key)
    

def ch10_5(file):
    numbers = [random.randint(0, 9) for each in range(5)]
    n = random.randint(0, 9)
    for i in range(3):
        numbers.append(n)
    n = random.randint(0, 9)
    for i in range(2):
        numbers.append(n)
    random.shuffle(numbers)
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(' '.join(str(n) for n in numbers))
    numbers.sort()
    aggregator = []
    for each in numbers:
        if each not in aggregator:
            aggregator.append(each)
    answer_key = f'the distinct numbers are {" ".join(str(each ) for each in aggregator)}\r\n'
    assess(child, f'ch10_5.py', answer_key)


def ch10_6(file):
    print('under construction')


def ch10_7(file):
    print('under construction')


def ch10_8(file):
    print('under construction')


def ch10_9(file):
    print('under construction')


def ch10_10(file):
    print('under construction')


def ch10_11(file):
    print('under construction')


#++++++++++++++++++++++++++++SIENNA Green 2018++++++++++++++++++++++++++++++++++

def green1_18(file):
    def fourthsum(n):
        result = 0
        for i in range(1, n + 1):
            result += i**4
        return result
    
    child = pexpect.spawnu(f'python3 {file}')
    n = random.randint(0, 9)
    child.sendline(str(n))
    assess(child, 'g1_2018.py', str(fourthsum(n)))


def green2_18(file):
    def test(first_symbol, second_symbol):
        if first_symbol == 'Rock':
            if second_symbol == 'Scissors' or second_symbol == 'Lizard' or second_symbol == 'Zombie':
                return first_symbol
            elif first_symbol == second_symbol:
                return 'Tie'
            else:
                return second_symbol
        elif first_symbol == 'Paper':
            if second_symbol == 'Rock' or second_symbol == 'Spock' or second_symbol == 'LargeHadronCollider':
                return first_symbol
            elif first_symbol == second_symbol:
                return 'Tie'
            else:
                return second_symbol
        elif first_symbol == 'Scissors':
            if second_symbol == 'Paper' or second_symbol == 'Lizard' or second_symbol == 'Zombie':
                return first_symbol
            elif first_symbol == second_symbol:
                return 'Tie'
            else:
                return second_symbol
        elif first_symbol == 'Lizard':
            if second_symbol == 'Paper' or second_symbol == 'Spock' or second_symbol == 'LargeHadronCollider':
                 return first_symbol
            elif first_symbol == second_symbol:
                return 'Tie'
            else: 
                return second_symbol
        elif first_symbol == 'Spock':
            if second_symbol == 'Rock' or second_symbol == 'Scissors' or second_symbol == 'Collider':
                 return first_symbol
            elif first_symbol == second_symbol:
                return 'Tie'
            else: 
                return second_symbol
        elif first_symbol == 'Zombie':
            if second_symbol == 'Paper' or second_symbol == 'Lizard' or second_symbol == 'Spock':
                 return first_symbol
            elif first_symbol == second_symbol:
                return 'Tie'
            else: 
                return second_symbol
        else:
            if second_symbol == 'Rock' or second_symbol == 'Scissors' or second_symbol == 'Zombie':
                 return first_symbol
            elif first_symbol == second_symbol:
                return 'Tie'
            else: 
                return second_symbol  
    
    symbols = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock', 'Zombie', 'LargeHadronCollider']
    child = pexpect.spawnu(f'python3 {file}')
    first = symbols[random.randint(0, len(symbols) - 1)]
    while True:
        second = symbols[random.randint(0, len(symbols) - 1)]
        if first != second:
            break
    child.sendline(first)
    child.sendline(second)
    assess(child, 'g2_2018.py', test(first, second))

    
def green3_18(file):
    def get_time(current, alarm):
        if current < 720 and alarm < 720:
            if current > alarm:
                return 1440 - current + alarm
            else:
                return alarm - current
        elif current < 720 and alarm > 720:
            return alarm - current
        else:
            if alarm > current:
                return alarm - current
            else:
                return 1440 - current + alarm
        
    current_hour = random.randint(7, 23)
    current_minute = random.randint(10, 58)
    current_time = current_hour * 60 + current_minute
    alarm_hour = random.randint(7, 23)
    alarm_minute = random.randint(10, 58)
    alarm_time = alarm_hour * 60 + alarm_minute
    
    duration = get_time(current_time, alarm_time)
    hours = duration // 60
    minutes  = duration % 60
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(str(current_hour))
    child.sendline(str(current_minute))
    child.sendline(str(alarm_hour))
    child.sendline(str(alarm_minute))
    assess(child, 'g3_2018.py', f'{hours} {minutes}')
    
    
def green4_18(file):
    tests = ['mountains', 'altruism', 'alphanumeric', 'beautiful', 
            'parameterize', 'automobile' 'absurdism', 
            'underwear', 'organisms']
    word = tests[random.randint(0, len(tests) - 1)]
    ranges = [[0, 2], [3, 4], [5, 6], [7, 9]]
    indices = []
    n = random.randint(2, 4)
    for each in range(n):
        indices.append(random.randint(ranges[each][0], ranges[each][1]))
    
    answer_key = ''
    for i in range(len(word)):
        if i not in indices:
            answer_key += word[i]
    
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(word)
    child.sendline(str(n))
    for each in range(n):
        child.sendline(str(indices[each] + 1))
    assess(child, 'g4_2018.py', answer_key)
    

def green5_18(file):
    tests = [['Elvis', 'Lives!'], ['Astronomer', 'moon starers'],
            ['clothes pins', 'so let\'s pinch'], 
            ['Slot machines', 'Cash lost in \'em'],
            ['A registrant\'s friend', 'Transfinder is great!!!']]
    
    def sterilize(word):
        # removes any chars other than alpha
        word = word.strip()
        word = word.lower()
        sterilized = ''
        for each in word:
            if each.isalpha():
                sterilized += each
        return sterilized
    
    
    def uniqe_letters(sterilized):
        # collects a copy of each uniqe letter in sorted order
        letters = []
        for each in sterilized:
            if each not in letters:
                letters.append('each')
        letters.sort()
        return letters
        
    
    def compare_lists(list1, list2):
        if list1 == list2:
            return True
        else:
            return False
    
    for i in range(4):
        first = tests[i][0]
        second = tests[i][1]
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline(first)
        child.sendline(second)
        
        first = sterilize(first)
        first = uniqe_letters(first)
        
        second = sterilize(second)
        second = uniqe_letters(second)
    
        if compare_lists(first, second):
            answer_key = 'YES'
        else:
            answer_key = 'NO'
            
        assess(child, f'g5_2018.py Case{i + 1}', answer_key)
        

def green6_18(file):
    
    def primary(N):
        answer_key = ''
        for base in range(2, 11):
            max_exponent = find_exponent(N, base)
            converted = converted_base(N, base, max_exponent)
            if is_mono_digit(converted):
                answer_key += f'{N} Base {base}: {converted}\r\n'
        return answer_key
        
        
    def find_exponent(N, base):    
        # finds the greatest base quantity in the number N
        exponent = 0
        while N >= base**exponent:
            exponent += 1
        return exponent - 1
       
    
    def converted_base(N, base, exponent):
        # returns N in converted to a new base as a string
        number = ''
        while exponent >= 0:
            number += str(N // base**exponent) 
            N %= base**exponent
            exponent -= 1
        return number
        
    
    def is_mono_digit(number):
        for each in number:
            if each == number[0]:
                continue
            else:
                return False
        return True
    
    
    child = pexpect.spawnu(f'python3 {file}')
    while True:
        N = random.randint(4, 1000)
        answer_key = primary(N)
        if answer_key != '':
            break
    child.sendline(str(N))
    assess(child, f'green6_18.py', answer_key)
    
    
def green7_18(file):
    
    def get_sets(cards):
        sets = []
        if '1DSR' in cards and '1OSV' in cards and '1PSG' in cards:
            sets.append('1DSR 1OSV 1PSG')
        if '1DSR' in cards and '2DHV' in cards and '3DLG' in cards:
            sets.append('1DSR 2HDV 3DLG')
        if '1OHG' in cards and '2OLV' in cards and '3OSR' in cards:
            sets.append('1OHG 2OLV 3OSR')
        if '1PSR' in cards and '2DSR' in cards and '3OSR' in cards:
            sets.append('1PSR 2DSR 3OSR')
        if '2DSR' in cards and '2OLV' in cards and '2PHG' in cards:
            sets.append('2DSR 2OLV 2PHG')
        if '3DLG' in cards and '3OSR' in cards and '3PHV' in cards:
            sets.append('3DLG 3OSR 3PHV')
        sets.sort()
        return sets
        
    def generate_test_cards():
        while True:
            num_of_cards = random.randint(3, 12)
            list_of_cards = ['1DSR', '3OSR', '2PHG', '3PHV', '1PSR', '2DHV', 
                            '3DLG', '1PSG', '2DSR', '1OSV', '1OHG', '2OLV']
            test_cards = []
            for n in range(num_of_cards):
                while True:
                    i = random.randint(0, len(list_of_cards) - 1)
                    if list_of_cards[i] not in  test_cards:
                        test_cards.append(list_of_cards[i])
                        break
            if len(get_sets(test_cards)) != 0:
                break
        return num_of_cards, test_cards   
        
    n, test_cards = generate_test_cards()
    sets = get_sets(test_cards)
    answer_key = ''
    for each in sets:
        answer_key += f'{each}\r\n'
       
        
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(str(n))
    for each in test_cards:
        child.sendline(each)
    assess(child, f'green7_18.py', answer_key)
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def rock_paper_scissors(file):
    def test(first, second):
        combined = first + second
        if 'PAPER' in combined and 'ROCK' in combined:
            return 'PAPER WINS'
        elif 'SCISSORS' in combined and 'PAPER' in combined:
            return 'SCISSORS WINS'
        elif 'ROCK' in combined and 'SCISSORS' in combined:
            return 'ROCK WINS'
        else:
            return "TIE"
        
        
    tests = ['ROCK', 'PAPER', 'SCISSORS']
    for i in range(3):
        child = pexpect.spawnu(f'python3 {file}')
        first = tests[i % 3]
        second =  tests[(i + 1) % 3]
        child.sendline(first)
        child.sendline(second)  
        answer_key = test(first, second)
        
        assess(child, f'rock_paper_scissors.py Case{i + 1}', answer_key)
        
            

def slices(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
        test suite for slices.py
    """
    # creates the child instance
    child = pexpect.spawnu(f'python3 {file}')
    key = 'Be\r\nyourself\r\neveryone\r\nelse\r\nis\r\nalready\r\ntaken\r\n'
    # check the correctness of the submission
    assess(child, "slices.py", key)
    if child.isalive:
            child.kill(2)
     

def madlib(file):
        """
        :param file: the python file passed as a command line argument 
        :return None: 
        test suite for madlib.py
        """
        # words to enter
        words = ['<to>', '<adj>', '<verb1>', '<body_part>', '<num>', '<noun>', '<adverb>', '<verb2>', '<verb3>',
                '<pronouns>', '<author>']
        key = 'Dear <to>,\r\nYou are extremely <adj> and I <verb1> you.\r\n' \
                 'I want to kiss your <body_part> <num> times.\r\n' \
                 'You make my <noun> burn with desire.\r\n' \
                 'When I first saw you, I <adverb> <verb2> at you and fell in love.\r\n' \
                 'Will you <verb3> out with me?\r\n' \
                 'Don\'t let your parents discourage you, <pronouns> are just jealous.\r\n' \
                 'Yours forever, <author> :)\r\n'
        # creates the child instance
        child = pexpect.spawnu(f'python3 {file}')
        # enters the words
        for each in words:
            child.sendline(each)
        assess(child, "madlib.py", key)
        if child.isalive:
            child.kill(2)


def greedy(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for greedy.py
    """
    # creates the child instance
    data_in = [3.84,  1.10, .30, .04]
    data_out = ['15 quarters, 0 dimes, 1 nickels, 4 pennies', '4 quarters, 1 dimes, 0 nickels, 0 pennies', '1 quarters, 0 dimes, 1 nickels, 0 pennies', '0 quarters, 0 dimes, 0 nickels, 4 pennies']
    
    for i, each in enumerate(data_in):
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline(str(each))
        assess(child, "greedy.py", key)
        if child.isalive:
                child.kill(2) 

           
def hypotenuse(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for hypotenuse.py
    """
    key = ['Enter the side length:', 'The hypotenuse is ']
    data = ['3.1', '4.1', '5.14']
    # creates the child instance
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(data[0])
    child.sendline(data[1])
    # check the correctness of submission
    try:
        child.expect_exact(key[1] + data[2])
        # pass
        print('{}Output is correct!\n\n{}{}{}\n\n{}:) hypotenuse.py == passed{}'
        .format(BY, G, child.before, child.match, BY, X))
    # fail
    except:
        print('{}Expected output of:\n\n{}{}{}\n{}{}\n{}{}\n\n{}Actual output was:\n\n{}{}\n{}:( slices.py == failed{}'
        .format(BY, R, key[0], data[0], key[0], data[1], key[1], data[2], BY, R, child.before, BY, X))
    if child.isalive:
            child.kill(2)


def average(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for hypotenuse.py
    """
    grade = ['first', 'second', 'third', 'fourth']
    nums = ['78', '97', '86', '88', '87']
    # creates the child instance
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(nums[0])
    child.sendline(nums[1])
    child.sendline(nums[2])
    child.sendline(nums[3])
    # check the correctness of submission
    try:
        child.expect_exact('The average is 87')
        # pass
        print('{}Output is correct!\n\n{}{}{}\n\n{}:) average.py == passed{}'
        .format(BY, G, child.before, child.match, BY, X))
    # fail
    except:
        print('{}Expected output of:{}\n'.format(BY, R))
        for i, each in enumerate(grade):
            print('Enter the {} grade: {}'.format(grade[i], nums[i]))
        print('The average is 87')
        print('\n{}Actual output was:\n\n{}{}\n{}:( average.py == failed{}'.format(BY, R, child.before, BY, X))
    if child.isalive:
            child.kill(2)


def polygon(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for average.py
    """
    # creates the child instance
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline('6')
    # check the correctness of submission
    try:
        child.expect_exact('The interior angles are 120.0 degrees.')
        # pass
        print('{}Output is correct!\n\n{}{}{}\n\n{}:) polygon.py == passed{}'
        .format(BY, G, child.before, child.match, BY, X))
    # fail
    except:
        print('{}Expected output of:\n\n{}Enter the number of sides: 6\nThe interior angles are 120.0 degrees.\n'.format(BY, R))
        print('{}Actual output was:\n\n{}{}\n{}:( polygon.py == failed{}'.format(BY, R, child.before, BY, X))
    if child.isalive:
            child.kill(2)
            

def fahrenheit(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for fahrenheit.py
    """
    data = [['0', '0.0'], ['100', '100.0'], ['32', '32.0'], ['212', '212.0']]
    key = ['Hai! Enter the temperature in degrees Fahrenheit: ', '{} degrees Fahrenheit is childroximately {} degrees Celsius.']
    
    # creates the child instance
    child = pexpect.spawnu(f'python3 {file}')
    child.sendline(data[3][0])
    # check the correctness of submission
    try:
        child.expect_exact(key[1].format(data[3][1], data[1][1]))
        # pass
        print('{}Output is correct!\n\n{}{}{}\n\n{}:) fahrenheit.py == passed{}'
        .format(BY, G, child.before, child.match, BY, X))
    # fail
    except:
        print('{}Expected output of:\n\n{}{}{}\n{}\n{}\nActual output was:\n\n{}{}{}\n:( fahrenheit.py == failed{}'
        .format(BY, R, key[0], data[3][0], key[1].format(data[3][1], data[1][1]), BY, R, child.before, BY, X))
    if child.isalive:
            child.kill(2)
            

def report_card(file):
        """
        :param file: the python file passed as a command line argument 
        :return None: 
        test suite for fahrenheit.py
        """
        # words to enter
        data = ['Einstein', '99.8', '98.7', '95.3', '81.4', '75.0', '68.5']

        key = 'This is {}\'s report card.\r\n\r\n' \
         '6 sorted grades: [{}, {}, {}, {}, {}, {}]\r\n\r\n' \
         '{}\'s highest grade is {}.\r\n\r\n' \
         'The low grade of {} is being dropped.\r\n\r\n' \
         'Now {}\'s grades are [{}, {}, {}, {}, {}].\r\n\r\n' \
         '{}\'s average is now 90.0.\r\n\r\n'.format(data[0], data[6], data[5], data[4], data[3], data[2], data[1],
                                                     data[0], data[1], data[6], data[0], data[5],
                                                     data[4], data[3], data[2], data[1], data[0])
        # creates the child instance
        child = pexpect.spawnu(f'python3 {file}')
        # enters the words
        for each in data:
            child.sendline(each)
        # check the correctness of submission
        try:
            child.expect_exact(key)
            # pass
            print('\n{}Output is correct!\n{}{}\n{}{}:) report_card.py == passed\n{}'
            .format(BY, G, child.before, child.match, BY, X))
        # fail
        except:
            print(child.before)
            print('\n{}Expected output of:\n{}{}\n{}Actual output was:\n{}{}{}:( report_card.py == failed{}'
            .format(BY, R, key, BY, R, child.before[225:], BY, X))
        if child.isalive:
            child.kill(2)
            

def even_odd(file):
    """
    :param file: the python file passed as a command line argument 
    :return None: 
    test suite for even_odd.py
    """
    ok = 0
    test_data = [['2', 'even'], ['3', 'odd'], ['-1', 'odd'], ['-2', 'even']]
    for i in range(4):
        # creates the child instance
        child = pexpect.spawnu(f'python3 {file}')
        child.sendline('{}'.format(test_data[i][0]))
        # check the correctness of submission
        try:
            child.expect_exact('{} is an {} number.'.format(test_data[i][0], test_data[i][1]))
            # pass
            print('{}{}'.format(G, child.match))
            ok += 1
        # fail
        except:
            print('\n{}Expected output of:\n{}{} is an {} number.\n{}Actual output was:\n{}{}{}'
            .format(BY, R, test_data[i][0], test_data[i][1], BY, R, child.before[19:], X))
        if child.isalive:
            child.kill(2)
    if ok == 4:
        print('{}:) even_odd.py == passed{}'.format(BY, X))
    else:
        print('{} even_odd.py == failed{}'.format(BY, X))


def birth_month(file):
    """ birth_month.py autograder """
    samples = random.randint(2, 6)
    birthMonths = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    
    for sample in range(samples):
        child = pexpect.spawnu(f'python3 {file}')   
        birthMonth = random.choice(list(birthMonths))
        child.sendline(str(birthMonth))
        
        key = f'You were born in {birthMonths[birthMonth]}'
        assess(child, f'{file} case {sample + 1}', key)
        

def grade_book(file):
    """ grade_book.py autograder """
    ok = 0
    checks = 5
    data = [['92', 'A'], ['84', 'B'], ['76', 'C'], ['65', 'D'], ['64', 'F']]
    for i in range(checks):
        # creates the child instance
        child = pexpect.spawnu(f'python3 {file}')     
        child.sendline('{}'.format(data[i][0]))
        # check the correctness of submission
        try:
            child.expect_exact('{} is your letter grade.'.format(data[i][1]))
            # pass
            print('{}{}{}{}'.format(child.before, G, child.match, X))
            ok += 1
        # fail
        except:
            print(child.before[:27])
            print('{}Expected output of:\n{}{} is your letter grade.{}'.format(BY, R, data[i][1], X))
            print('{}Actual output was:\n{}{}{}'.format(BY, R, child.before[29:len(child.before)-2], X))
        if child.isalive:
            child.kill(2)
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
        # creates the child instance
        child = pexpect.spawnu(f'python3 {file}')     
        child.sendline('{}'.format(data[i][0]))
        child.sendline('{}'.format(data[i][1]))
        # check the correctness of submission
        try:
            child.expect_exact('{}'.format(data[i][2]))
            # pass
            print('{}{}{}{}'.format(child.before, G, child.match, X))
            ok += 1
        # fail
        except:
            before = b_sanitize(child.before)
            print('{}\n{}'.format(before[0], before[1]))
            print('{}Expected output of:\n{}{}'.format(BY, R, data[i][2]))
            print('{}Actual output was:\n{}{}{}'.format(BY, R, before[2], X))
        if child.isalive:
            child.kill(2)
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
        # creates the child instance
        child = pexpect.spawnu(f'python3 {file}')     
        child.sendline('{}'.format(data[i][0]))
        # check the correctness of submission
        try:
            child.expect_exact('{}'.format(data[i][1]))
            # pass
            print('{}{}{}{}'.format(child.before, G, child.match, X))
            ok += 1
        # fail
        except:
            index = str(child.before.encode('utf-8')).index(chr(92)) # finds first \r in child.before for slice
            print('{}'.format(child.before[:index-1]))
            print('{}Expected output of:\n{}{}{}'.format(BY, R, data[i][1], X))
            print('{}Actual output was:\n{}{}{}'.format(BY, R, child.before[index:len(child.before)-2], X))
        if child.isalive:
            child.kill(2)
    if ok == checks:
        print('{}:) {} == passed{}'.format(BY, file, X))
    else:
        print('{}:( {} == failed{}'.format(BY, file, X))


def leftStack(file):
    height = random.randint(3, 8)
    key = ''
    for row in range(1, height + 1):
        key += row * '#' + '\r\n'
    child = pexpect.spawnu(f'python3 {file}')     
    child.sendline(str(height))
    assess(child, f'{file}', key)
    

def rightStack(file):
    height = random.randint(3, 8)
    spaces = height - 1
    key = ''
    for row in range(1, height + 1):
        for space in range(spaces):
            key += ' '
        spaces -= 1    
        key += row * '#' + '\r\n'
    child = pexpect.spawnu(f'python3 {file}')     
    child.sendline(str(height))
    assess(child, f'{file}', key)
    
def pyramidStacks(file):
    """pyramidStacks.py autograder """
    ok = 0
    checks = 2
    
    if file == 'leftStack.py':
        def getKey(height):
            key = ''
            for row in range(1, height + 1):
                key += row * '#' + '\r\n'
            return key
        height = random.randint(3, 10)
        child = pexpect.spawnu(f'python3 {file}')     
        child.sendline(str(height))
        key = getKey(height)
        assess(child, f'{file}', key)
    '''
    if file == 'leftStack.py':
        data = [[3, '#\r\n##\r\n###\r\n'], [6, '#\r\n##\r\n###\r\n####\r\n#####\r\n######\r\n']]
    if file == 'leftStacks.py': 
        data = [[3, '##\r\n###\r\n####\r\n'], [6, '##\r\n###\r\n####\r\n#####\r\n######\r\n#######\r\n']]
    if file == 'rightStack.py':
        data = [[3, '  #\r\n ##\r\n###\r\n'], [6, '     #\r\n    ##\r\n   ###\r\n  ####\r\n #####\r\n######\r\n']]
    if file == 'rightStacks.py':
        data = [[3, '  ##\r\n ###\r\n####\r\n'], [6, '     ##\r\n    ###\r\n   ####\r\n  #####\r\n ######\r\n#######\r\n']]
    if file == 'pyramid.py':
        data = [[3, '  ##\r\n ####\r\n######\r\n'], [6, '     ##\r\n    ####\r\n   ######\r\n  ########\r\n ##########\r\n############\r\n']]
    if file == 'pyramidHacker.py':
        data = [[3, '  /\\\r\n /  \\\r\n/____\\\r\n'], [6, '     /\\\r\n    /  \\\r\n   /    \\\r\n  /      \\\r\n /        \\\r\n/__________\\\r\n']]
    
    for i in range(checks):
        # creates the child instance
        child = pexpect.spawnu(f'python3 {file}')     
        child.sendline('{}'.format(data[i][0]))
        # check the correctness of submission
        try:
            child.expect_exact('{}'.format(data[i][1]))
            # pass
            print('{}{}{}{}'.format(child.before, G, child.match, X))
            ok += 1
        # fail
        except:
            print(child.before[:find_nth(child.before, '\r\n', 0)])
            print('{}Expected output of:\n{}{}{}'.format(BY, R, data[i][1], X))
            print('{}Acutal output was:\n{}{}{}'.format(BY, R, '\n'.join(b_sanitize(child.before)[1:]), X))
        if child.isalive:
            child.kill(2)
    if ok == checks:
        print('{}:) {} == passed{}'.format(BY, file, X))
    else:
        print('{}:( {} == failed{}'.format(BY, file, X))
    '''
    
def validate(file):
    """validate.py autograder 
    this needs to be gone over with test cases, still in beta
    """
    # creates the child instance
    child = pexpect.spawnu(f'python3 {file}')  
    ok = 0
    data = [3, -6, - 8.9, '$', '\r', 'pickles', 'C']
    for i, each in enumerate(data):
        child.sendline(str(data[i]))
        # checking alpha validation
        if each == 'C':
            # alpha passed
            print('{}{}{}{}'.format(child.match, BG, each, X))
            print('{}Alpha validation passed!\n{}'.format(G, X))
            data.reverse()
            # checking for numeric validation
            for i, each in enumerate(data):
                child.sendline(str(data[i]))
                if type(each) != str and 0 < each < 10:
                    #numeric passed
                    print('{}{}{}{}'.format(child.match, BG, each, X))
                    print('{}Numeric validation passed!\n{}'.format(G, X))
                    print('{}:) {} == passed!{}'.format(BY, file, X))
                # cycle numeric data test   
                else:
                    try:
                        child.expect_exact('Enter a positive number: ', timeout=1.5)
                        # pass
                        print('{}{}'.format(child.match, data[i]))
                    #fail
                    except Exception as e:
                        print('{}Numeric Validation Error\n\n{}{}{}'.format(BR, R, e, X))
                        print('{}:( {} == failed!{}'.format(BY, file, X))
                        break    
        # cycle alpha data test
        else:
            try:
                child.expect_exact('Enter a letter: ', timeout=1.5)
                # pass
                print('{}{}'.format(child.match, data[i]))
            # fail
            except:
                print('{}Alpha Validation Error\n\n{}{}{}'.format(BR, R, child.before, X))
                print('{}:( {} == failed!{}'.format(BY, file, X))
                break
    if child.isalive:
            child.kill(2)
            
            
def validate_functions(file):
    """validate_functions.py autograder """
    # creates the child instance
    child = pexpect.spawn('python3')
    child.sendline('from validate_functions import *')
    child.sendline('temp = test()')
    child.sendline('print(temp)')
    try:
        child.expect('test printed')
        print('yes the test has passed')
    except Exception as e:
        print(e)
    # print(child.before.decode("utf-8")) 
    print(child.after.decode("utf-8"))           
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
        # creates the child instance
        child = pexpect.spawnu('python3 {}'.format(file), timeout=5) 
        print('Test run number {}\nGuess a number between 1 and 1000: 500'.format(i + 1))
        while True:
            child.sendline(str(middle))
            # check the correctness of submission
            # print(start, end, middle)
            index = child.expect_exact(['too low, try again; guess-->', 'too high, try again; guess-->',
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
                print('{}{}{}\n'.format(G, child.match, X))
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


def lottery(file):

    def createTest(file):
        child = pexpect.spawnu(f'python3 {file}')
        secret = int(child.read_nonblocking(size=2, timeout=-1).strip())
        secret1 = secret // 10 # isolate first digit
        secret2 = secret % 10 # isolate second digit
        return [child, secret, secret1, secret2]
    
    
    def case1(data):
        data[0].sendline(str(data[1]))
        key = 'You won $10000'
        print(f'Secret is {data[1]}')
        assess(data[0], "lottery.py Case 1", key)
    
            
    def case2(data):
        data[0].sendline(f'{data[3]}{data[2]}')
        key = 'You won $3000'
        print(f'Secret is {data[1]}')
        assess(data[0], "lottery.py Case 2", key)
    
    
    def case3(data):
        while True:
            noMatch = random.randint(1,9)
            if noMatch != data[2] and noMatch != data[3]:
                break
            else:
                continue
        data[0].sendline(f'{data[3]}{noMatch}')
        key = 'You won $1000'
        print(f'Secret is {data[1]}')
        assess(data[0], "lottery.py Case 3", key)
    
    
    def case4(data):
        while True:
            noMatch = random.randint(1,9)
            if noMatch != data[2] and noMatch != data[3]:
                break
            else:
                continue
        data[0].sendline(f'{noMatch}{noMatch}')
        key = 'You won $0'
        print(f'Secret is {data[1]}')
        assess(data[0], "lottery.py Case 4", key)

    
    case1(createTest(file))
    case2(createTest(file))
    case3(createTest(file))
    case4(createTest(file))


def main():
    # validate arguments
    if len(sys.argv) == 2:
        try:
            # find and store the file
            student_file = findInSubdirectory(sys.argv[1])
            child_selector(sys.argv[1], student_file)
            
        except IOError as e:
            print(f'{BR}ERROR\n{Y}{sys.argv[1]}{X} doesn\'t exist or is incorrectly named')
            
    else:
        print(f'{BR}ERROR\n{X}Expected 1 argument\n{BB}<terminal>{X}$ testMe filename.py')
        
if __name__ == "__main__":
    main()
