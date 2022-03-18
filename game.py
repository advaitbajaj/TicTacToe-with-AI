def printBoard(board):
    print(board[1]+ '|'+ board[2]+ '|'+ board[3])
    print("-+-+-")
    print(board[4]+ '|'+ board[5]+ '|'+ board[6])
    print("-+-+-")
    print(board[7]+ '|'+ board[8]+ '|'+ board[9])
    print("\n")

def spaceIsFree(position):
    if (board[position] == ' '):
        return True
    return False

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def checkForWin():
    # check rows
    if (
        (board[1] == board[2] == board[3] and board[1] != ' ') or
        (board[4] == board[5] == board[6] and board[4] != ' ') or
        (board[7] == board[8] == board[9] and board[7] != ' ')
    ):
        return True
    

    # check columns
    if (
        (board[1] == board[4] == board[7] and board[1] != ' ') or
        (board[2] == board[5] == board[8] and board[2] != ' ') or
        (board[3] == board[6] == board[9] and board[3] != ' ')
    ):
        return True

    # check diagonals
    if (
        (board[1] == board[5] == board[9] and board[1] != ' ') or
        (board[3] == board[5] == board[7] and board[3] != ' ')
    ):
        return True
    return False

def checkWhoWon(symbol):
    # check rows
    if (
        (board[1] == board[2] == board[3] and board[1] == symbol) or
        (board[4] == board[5] == board[6] and board[4] == symbol) or
        (board[7] == board[8] == board[9] and board[7] == symbol)
    ):
        return True
    

    # check columns
    if (
        (board[1] == board[4] == board[7] and board[1] == symbol) or
        (board[2] == board[5] == board[8] and board[2] == symbol) or
        (board[3] == board[6] == board[9] and board[3] == symbol)
    ):
        return True

    # check diagonals
    if (
        (board[1] == board[5] == board[9] and board[1] == symbol) or
        (board[3] == board[5] == board[7] and board[3] == symbol)
    ):
        return True
    return False


def insertLetter(letter, position):
    if (spaceIsFree(position)):
        board[position] = letter
        printBoard(board)

        if (checkForWin()):
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
               
        if (checkDraw()):
            print("Draw!")
            exit()
    else:
        print("Position is occupied! Enter new position: ")
        position = int(input())
        insertLetter(letter, position)

def playerMove():
    position = int(input("Enter position for O: "))
    insertLetter(player, position)
    return

def botMove():
    bestScore = -1000
    bestMove = 0

    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return

def minimax(board, depth, isMaximizing):
    # Termination conditions
    if (checkWhoWon(bot)):
        return 1
    
    elif (checkWhoWon(player)):
        return -1

    elif (checkDraw()):
        return 0
    
    if (isMaximizing):
        bestScore = -1000
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, 0, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore          
    else:
        bestScore = 1000
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore

board = {
    1: 'X', 2: ' ', 3: 'O',
    4: 'O', 5: 'O', 6: ' ',
    7: 'X', 8: ' ', 9: 'X'
}
player = 'O'
bot = 'X'

while not checkForWin():
    botMove()
    playerMove()