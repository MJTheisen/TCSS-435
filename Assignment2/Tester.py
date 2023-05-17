import Board
import random

def getBoardSize():
    while True:
        try:
            inputStr = input("\nInput ""[player] [searchmethod] [size]"": ")
            playerNumber, size = inputStr.split()
            playerNumber = int(playerNumber)
            rows, columns = map(int, size.split('*'))
            return playerNumber, rows, columns
        except ValueError:
            print("Invalid input. Try again.\n")

def getPlayerMove(board, symbol):
    while True:
        try:
            move = input("\nInput GAMEMOVE ""r/c"" : ")
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
        raise ValueError("Invalid player number.\n")

playerNumber, boardRows, boardColumns = getBoardSize()
playerSymbol = getPlayerSymbol(playerNumber)

print(f"\nPlayer 1: {'Human' if playerNumber == 1 else 'AI'}")
print(f"Player 2: {'Human' if playerNumber == 2 else 'AI'}")

board = Board.GameBoard(boardRows, boardColumns)

# Display the initial board
print()
print("\nHere is what the board looks like")
board.display()

while not board.isWin('O'):
    # player move
    row, column = getPlayerMove(board, 'O')
    board.placeSymbol(row, column, 'O')

    # updated board
    print()
    print("Your move:")
    board.display()

    if board.isWin('O'):
        print(f"\nPlayer {playerNumber} wins!")
        break

    # AI move
    emptyCells = [
        (r, c)
        for r in range(board.rows)
        for c in range(board.columns)
        if board.isEmpty(r, c)
    ]
    aiRow, aiColumn = random.choice(emptyCells)
    board.placeSymbol(aiRow, aiColumn, 'X')
    
    # updated board
    print()
    print("AI's move:") 
    board.display()

    if board.isWin('X'):
        print(f"\nPlayer {playerNumber} wins!")
        break

print("\nThe game is now over for now...\n")
