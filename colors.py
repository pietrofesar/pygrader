"""
This script demonstrates the possible text color combinations you can use in Python
"""

# http://ascii-table.com/ansi-escape-sequences.php
# http://kishorelive.com/2011/12/05/printing-colors-in-the-terminal/
# Esc[attribute;foreColor;aftColorm

# you can set constants
G = '\033[1;32m' # bold green
Y = '\033[1;33m' # bold yellow
R = '\033[31m' # red
X = '\033[0m' # reset


# base color options
for each in range(30, 47):
    print('\033[{}mTest number is {}'.format(each, each))
print(X)

# bold added to base colors
for each in range(30, 47):
    print('\033[1;{}mTest number is {}'.format(each, each))
print(X)

print('{}This is an example.{}'.format(G, X))

print('\033[33mThis is an example\033[0m')
