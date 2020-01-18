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

# def guessX(location):
#     theBoard[location] = 'X'
#     # printBoard(theBoard)
#     xTurn = theBoard[location]
#     printBoard(theBoard)
#     return xTurn
#
# def guessO(location):
#     theBoard[location] = 'O'
#     # printBoard(theBoard)
#     oTurn = theBoard[location]
#     printBoard(theBoard)
#     return oTurn

def guesses(turn, location):
    theBoard[location] = turn
    # printBoard(theBoard)
    oTurn = theBoard[location]
    printBoard(theBoard)
    return oTurn

def playGame():
    # printBoard(theBoard)
    turn = 'X'
    guess = ''
    # print(turn == guessX())
    for i in range(9):
        print(i)
        if turn == 'X':
            turn = 'O'
            guess = input(f'Enter a location to place an {turn}: ')
            guesses(turn, guess)
            # print(f'If turn2: {turn}')
        else:
            turn = 'X'
            guess = input(f'Enter a location to place an {turn}: ')
            guesses(turn, guess)
            # print(f'Else turn: {turn}')
    # for i in range(9):
    #     printBoard(theBoard)
    #     if turn == guessX():
    #         printBoard(theBoard)
    #         turn = guessO()
    #     else:
    #         printBoard(theBoard)
    #         turn = guessX()
    # printBoard(theBoard)

playGame()