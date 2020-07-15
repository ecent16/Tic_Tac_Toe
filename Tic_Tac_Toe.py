# Tic - Tac - Toe Midterm Project
# Ervin Centeno
# October 17, 2018

import random

board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',  # Dictionary for game board.
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printedBoard(b):    # Prints game board.
    print(b['top-L'] + '|' + b['top-M'] + '|' + b['top-R'])
    print('-+-+-')
    print(b['mid-L'] + '|' + b['mid-M'] + '|' + b['mid-R'])
    print('-+-+-')
    print(b['low-L'] + '|' + b['low-M'] + '|' + b['low-R'])


def winnerCheck_x(b):
    if ((b['top-L'] == 'x' and b['top-M'] == 'x' and b['top-R'] == 'x') or
        (b['mid-L'] == 'x' and b['mid-M'] == 'x' and b['mid-R'] == 'x') or
        (b['low-L'] == 'x' and b['low-M'] == 'x' and b['low-R'] == 'x') or
        (b['top-L'] == 'x' and b['mid-M'] == 'x' and b['low-R'] == 'x') or
        (b['top-R'] == 'x' and b['mid-M'] == 'x' and b['low-L'] == 'x') or
        (b['top-L'] == 'x' and b['mid-L'] == 'x' and b['low-L'] == 'x') or
        (b['top-M'] == 'x' and b['mid-M'] == 'x' and b['low-M'] == 'x') or
        (b['top-R'] == 'x' and b['mid-R'] == 'x' and b['low-R'] == 'x')):
            return True

def winnerCheck_o(b):
    if ((b['top-L'] == 'o' and b['top-M'] == 'o' and b['top-R'] == 'o') or
        (b['mid-L'] == 'o' and b['mid-M'] == 'o' and b['mid-R'] == 'o') or
        (b['low-L'] == 'o' and b['low-M'] == 'o' and b['low-R'] == 'o') or
        (b['top-L'] == 'o' and b['mid-M'] == 'o' and b['low-R'] == 'o') or
        (b['top-R'] == 'o' and b['mid-M'] == 'o' and b['low-L'] == 'o') or
        (b['top-L'] == 'o' and b['mid-L'] == 'o' and b['low-L'] == 'o') or
        (b['top-M'] == 'o' and b['mid-M'] == 'o' and b['low-M'] == 'o') or
        (b['top-R'] == 'o' and b['mid-R'] == 'o' and b['low-R'] == 'o')):
            return True

def freeSpace(b, move): # Checks for available spaces in board.
    return b[move] == ' '


def makeMove(board, letter, move):
    board[move] = letter


def randomMoves(board, movesList):  # Function used to decide what moves to take for AI.
    possibleMoves = [' ']
    for i in movesList:
        if freeSpace(board, i):
            possibleMoves. append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def boardCopy(board):
    copyB = []

    for i in board:
        copyB.append(i)
    return copyB


def aiMove(board, aiTurn):

    for i in range(9):
        copy = boardCopy(board)

        if freeSpace(copy, i):
            makeMove(copy, aiTurn, i)
            if winnerCheck_x(copy):
                return i

    move = randomMoves(board, ['top-L', 'top-M', 'top-R', 'low-L', 'low-R', 'low-M', 'mid-L', 'mid-M', 'mid-R'])
    if move is not None:
        return move

    return randomMoves(board, ['top-L', 'top-M', 'top-R', 'low-L', 'low-R', 'low-M', 'mid-L', 'mid-M', 'mid-R'])


def soloPlay():

    turn = 'x'
    aiLetter = 'o'

    for i in range(9):
        printedBoard(board)
        print('Player x move on which space?')

        move = input()

        if move not in board or not freeSpace(board, move):
            while True:
                print('Invalid move try again. ')
                break

        else:
            if turn == 'x':

                board[move] = turn

                if winnerCheck_x(board) is True:
                        printedBoard(board)
                        print('Player x wins.')
                        return
                elif (winnerCheck_x(board) is False or winnerCheck_o(board) is False) and freeSpace(board, move) is False:
                        printedBoard(board)
                        print('It is a tie.')
                        return
                else:
                    turn = aiLetter

            if turn == aiLetter:
                print('Beep boop- its my turn 0_0')
                move = aiMove(board, aiLetter)

                board[move] = turn

                if winnerCheck_o(board) is True:
                    printedBoard(board)
                    print('Player o wins.')
                    return
                elif (winnerCheck_o(board) is False or winnerCheck_o(board) is False) and freeSpace(board, move) is False:
                    printedBoard(board)
                    print('It is a tie.')
                    return
                else:
                    turn = 'x'

    printedBoard(board)

def twoPlayer():    # Two player function start.

    turn = 'x'

    for i in range(9):
        printedBoard(board)
        print('Turn for ' + turn + '. Move on which space?')

        move = input()

        if move not in board or not freeSpace(board, move):
            while True:
                print('Invalid move try again. ')
                break

        else:
            board[move] = turn

            if turn == 'x':
                turn = 'o'
            else:
                turn = 'x'

        if winnerCheck_x(board) is True:
            printedBoard(board)
            print('Player x wins.')
            return
        elif winnerCheck_o(board) is True:
            printedBoard(board)
            print('Player o wins.')
            return
        elif (winnerCheck_x(board) is False or winnerCheck_o(board) is False) and freeSpace(board, move) is False:
            printedBoard(board)
            print('It is a tie.')
            return
    printedBoard(board)


# Start of Tic-Tac-Toe
print('Welcome to Tic-Tac-Toe')
replay = 'yes'
while replay == 'yes':
    board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',  # Dictionary for game board.
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

    print('Would you like to play with a friend or solo?(1 for solo, 2 for two player)')
    game = input()

    while game != '1' or game != '2':   # Select game.
        if game == '1':
            soloPlay()
            break
        if game == '2':
            twoPlayer()
            break
        if game != '1' or game != '2':
            game = input('Please select game mode!')    # Loops until player enters 1 or 2.

    replay = input('Would you like to play again. ')
    if replay != 'yes':
        print('Thanks for playing!')
        break

