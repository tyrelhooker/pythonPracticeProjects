# Creates a tic-tac toe board from list of values
horizontalIndicators = ['L', 'M', 'R']
verticalIndicators = ['top', 'mid', 'low']

theBoard = {}

def buildSlots():
    boardSlots = []
    for vert in verticalIndicators:
        for horiz in horizontalIndicators:
            boardSlots.append(f'{vert}-{horiz}')

    return boardSlots

def buildBoard():
    boardSlots = buildSlots()
    for slot in boardSlots:
        theBoard.setdefault(slot, ' ')
    print(theBoard)

def printBoard(board):
    buildBoard()
    # boardSlots = buildSlots()
    # for slot in range(int(boardSlots[0]), int(boardSlots[3])):
    #     print(f'{board[]}')
    # theBoard['low-R'] = 'X'
    print(f"{board['top-L']}|{board['top-M']}|{board['top-R']}")
    print('-+-+-')
    print(f"{board['mid-L']}|{board['mid-M']}|{board['mid-R']}")
    print('-+-+-')
    print(f"{board['low-L']}|{board['low-M']}|{board['low-R']}")
# print(boardSlots)
# buildBoard()

def guessX():
    location = input('Enter a location to place an X: ')
    theBoard[location] = 'X'

def guessY():
    location = input('Enter a location to place an O: ')
    theBoard[location] = 'O'

def playGame():
    guessX()
    printBoard(theBoard)
    guessY()
    printBoard(theBoard)

playGame()