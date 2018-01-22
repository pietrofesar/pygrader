"""
this script computes the damage done between two opposing cards using the Iorveth duel mechanic within the Witcher Card Game
"""

b = int(input('Enter the greater power: '))
a = int(input('Enter the lower power: '))
c = 0
d = 0

def iorveth(a, b):
    global c
    global d
    if a <= 0:
        return a
    else:
        print('{} minus {}'.format(b, a))
        if a < b:
            c += a
        else:
            c += b
        b -= a
        d = a
        if b <= 0:
            b = 0
        return iorveth(b, a)
    

print(iorveth(a, b))
print('total damage of {}, remaining unit is {} power'.format(c, d))
