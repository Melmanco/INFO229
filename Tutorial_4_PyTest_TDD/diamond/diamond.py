import sys

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def distance(x,y):
    out = LETTERS.index(y) - LETTERS.index(x)
    if out < 0:
        out *= -1
    return out

def main(argv):
    last_letter = argv[0].upper()
    diamond_string = LETTERS[1:LETTERS.index(last_letter)]

    # Print first Letter
    for i in range(distance('A',last_letter)):
        print(' ', end='')
    print('A')

    # Print letters between first and last letters
    for letter in diamond_string:
        
        for i in range(distance(letter,last_letter)):
            print(' ', end='')
        print(letter, end='')

        for i in range(distance('A', letter)*2-1):
            print(' ', end='')
        print(letter)

    # Print last letter

    print(last_letter, end='')

    for i in range(distance('A', last_letter)*2-1):
        print(' ', end='')
    print(last_letter)

    # Print letters between first and last letters backwards
    for letter in diamond_string[::-1]:
        
        for i in range(distance(letter,last_letter)):
            print(' ', end='')
        print(letter, end='')

        for i in range(distance('A', letter)*2-1):
            print(' ', end='')
        print(letter)
    
    # Print first letter
    for i in range(distance('A',last_letter)):
        print(' ', end='')
    print('A')

if __name__ == '__main__':
    main(sys.argv[1:])