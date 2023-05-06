import random
from time import sleep

def create_board(b):
   print(' | |')
   print(''+b[7]+'|'+b[8]+'|'+b[9])
   print(' | |')
   print('-----------')
   print(''+b[4]+'|'+b[5]+'|'+b[6])
   print(' | |')
   print('-----------')
   print(''+b[1]+'|'+b[2]+'|'+b[3])
   print(' | |')
def inputPlayerLetter():
   letter=''
   while not (letter=='X' or letter=='O'):
        print('do you want to be X or O?')
        letter =input().upper()

if letter=='X':
    return['X','O']
else:
    return['O','X']

def whoGoesFirst():
    if random.randint(0,1)==o:
         return 'computer'
    esle:
         return 'player'

def playAgain():
    print('don you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(b,letter,move):
    b[move]=letter

