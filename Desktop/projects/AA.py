import random

def drawBoard(b):
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
    letter=' '
    while not (letter=='X' or letter=='O'):
        print('do you want to be X or O?')
        letter =input().upper()
    if letter=='X' :
        return['X','O']
    else:
        return['O','X']

def whoGoesFirst():
    if random.randint(0,1)==0:
         return 'computer'
    else:
         return 'player'

def playAgain():
    print('do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(b,letter,move):
    b[move]=letter

def isWinner(bo,le):
   return ((bo[7]==le and bo[8]==le and bo[9]==le) or
   (bo[4]==le and bo[5]==le and bo[6]==le) or
   (bo[1]==le and bo[2]==le and bo[3]==le) or
   (bo[7]==le and bo[4]==le and bo[1]==le) or
   (bo[8]==le and bo[5]==le and bo[2]==le) or
   (bo[9]==le and bo[6]==le and bo[3]==le) or
   (bo[7]==le and bo[5]==le and bo[3]==le) or
   (bo[9]==le and bo[5]==le and bo[1]==le))

def getBoardCopy(b):
   dupeBoard = []
   for i in b:
      dupeBoard.append(i)
   return dupeBoard

def isSpaceFree(b,move):
   return b[move] ==' '

def getPlayerMove(b):
   move=' '
   while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(b, int(move)):
      print('What is your next move?(1-9)')
      move=input()
   return int(move)

def chooseRandomMoveFromList(b,movesList):
   possibleMoves=[]
   for i in movesList:
      if isSpaceFree(b,i):
         possibleMoves.append(i)
         
      if len(possibleMoves)!=0:
         return random.choice(possibleMoves)
      else:
         return None

def getComputerMove(b,computerLetter):
   if computerLetter=='X':
      playerLetter='O'
   else:
      playerLetter='X'
   for i in range(1,10):
      copy=getBoardCopy(b)
      if isSpaceFree(copy,i):
         makeMove(copy,computerLetter,i)
         if isWinner(copy,computerLetter):
            return i
   for i in range(1,10):
      copy=getBoardCopy(b)
      if isSpaceFree(copy,i):
         makeMove(copy,playerLetter,i)
         if isWinner(copy,computerLetter):
            return i
   for i in range(1,10):
      copy=getBoardCopy(b)
      if isSpaceFree(copy,i):
         makeMove(copy,playerLetter,i)
         if isWinner(copy,playerLetter):
            return i
   move=chooseRandomMoveFromList(b, [1,3,7,9])
   if move!=None:
      return move
   if isSpaceFree(b,5):
      return 5
   return chooseRandomMoveFromList(b,[2,4,6,8])

def isBoardFull(b):
   for i in range(1,10):
      if isSpaceFree(b,i):
         return False
   return True
print('Welcome to Tic Tac Toe!')

while True:
   theBoard=[' ']*10
   playerLetter, computerLetter=inputPlayerLetter()
   turn=whoGoesFirst()
   print('the'+turn+' will go first.')
   gameIsPlaying = True

   while gameIsPlaying:
      if turn =='player':
         drawBoard(theBoard)
         move=getPlayerMove(theBoard)
         makeMove(theBoard,playerLetter,move)

         if isWinner(theBoard,playerLetter):
            drawBoard(theBoard)
            print('Hooray! You have Won the game!')
            gameIsPlaying=False
         else:
            if isBoardFull(theBoard):
               drawBoard(theBoard)
               print('The game is a tie!')
               break
            else:
               turn='computer'
      else:
         move=getComputerMove(theBoard,computerLetter)
         makeMove(theBoard,computerLetter,move)

         if isWinner(theBoard,computerLetter):
            drawBoard(theBoard)
            print('The computer has beaten you! you lose.')
            gameIsPlaying=False
         else:
            if isBoardFull(theBoard):
               drawBoard(theBoard)
               print('the game is a tie!')
               break
            else:
               turn='player'
   if not playAgain():
      break






























































         







         






         
