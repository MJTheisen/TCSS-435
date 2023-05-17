import random
import math
#import Solver

class GameBoard:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = [[' ' for _ in range(columns)] for _ in range(rows)]

    def display(self):
        print('-' * (self.columns*4 + 1))
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')
            print('-' * (self.columns * 4 + 1))

    def isEmpty(self, row, column):
        return self.board[row][column] == ' '

    def placeSymbol(self, row, column, symbol):
        self.board[row][column] = symbol
        for r in range(max(0, row - 1), min(self.rows, row + 2)):
            for c in range(max(0, column - 1), min(self.columns, column + 2)):
                if self.isEmpty(r, c):
                    self.board[r][c] = '/'

    def getSuccessorStates(self, symbol):
        successorStates = []
        for row in range(self.rows):
            for column in range(self.columns):
                if self.isEmpty(row, column):
                    successor = GameBoard(self.rows, self.columns)
                    successor.board = [r[:] for r in self.board]
                    successor.placeSymbol(row, column, symbol)
                    successorStates.append(successor)
        return successorStates

    # def isWin(self, symbol):
    #     for row in range(self.rows):
    #         for column in range(self.columns):
    #             if self.isEmpty(row, column):
    #                 return False
    #     return True

    # def isGameOver(self):
    #     # check if the board is full
    #     if self.isBoardFull():
    #         return True

    #     # check for winning configurations 
    #     if self.countWinningConfigurations('O') > 0 or self.countWinningConfigurations('X') > 0:
    #         return True

    #     return False
    
    # def isBoardFull(self):
    #     for row in self.board:
    #         for cell in row:
    #             if cell == ' ':
    #                 return False
    #     return True

def getPlayerMove(board, symbol):
    while True:
        try:
            move = input("Input GAMEMOVE ""r/c"" : ")
            row, column = map(int, move.split('/'))
            row -= 1
            column -= 1
            if (
                0 <= row < board.rows
                and 0 <= column < board.columns
                and board.isEmpty(row, column)
            ):
                return row, column
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

def getPlayerSymbol(playerNumber):
    if playerNumber == 1:
        return 'O'
    elif playerNumber == 2:
        return 'X'
    else:
        raise ValueError("Invalid player number.")

def getBoardSize():
    while True:
        try:
            inputStr = input("Input ""[player] [searchmethod] [size]"": ")
            playerNumber, size = inputStr.split()
            playerNumber = int(playerNumber)
            rows, columns = map(int, size.split('*'))
            return playerNumber, rows, columns
        except ValueError:
            print("Invalid input. Try again.")



playerNumber, boardRows, boardColumns = getBoardSize()
playerSymbol = getPlayerSymbol(playerNumber)

print(f"Player 1: {'Human' if playerNumber == 1 else 'AI'}")
print(f"Player 2: {'Human' if playerNumber == 2 else 'AI'}")
print()
print()