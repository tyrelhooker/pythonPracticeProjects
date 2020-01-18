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

# print(boardSlots)
buildBoard()
#