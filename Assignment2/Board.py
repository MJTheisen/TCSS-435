import random

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

    def isWin(self, symbol):
        for row in range(self.rows):
            for column in range(self.columns):
                if self.isEmpty(row, column):
                    return False
        return True
