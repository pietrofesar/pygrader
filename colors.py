# text color

# http://ascii-table.com/ansi-escape-sequences.php
# http://kishorelive.com/2011/12/05/printing-colors-in-the-terminal/
# Esc[attribute;foreColor;aftColorm

# you can set constants
G = '\033[38;5;70m' # green
Y = '\033[38;5;11m' # yellow
R = '\033[38;5;09m' # red
RST = '\033[0m' # reset


# base color options
for each in range(30, 47):
    print('\033[{}mTest number is {}'.format(each, each))
print(RST)

# bold added to base colors
for each in range(30, 47):
    print('\033[1;{}mTest number is {}'.format(each, each))
print(RST)

