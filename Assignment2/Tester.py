import Board
#import Solver

board = Board.GameBoard(Board.boardRows, Board.boardColumns)
while True:
    if Board.playerNumber == 1:
        print("Player 1 Move:")
        row, col = Board.getPlayerMove(board, Board.playerSymbol)
        board.placeSymbol(row, col, Board.playerSymbol)
    else:
        print("Player 2 Move:")
        row, col = Board.aiMakeMove(board, Board.playerSymbol)
        board.placeSymbol(row, col, Board.playerSymbol)
    
    print(f"Game Move: {row+1}/{col+1}")
    board.display()
    
    # check game state 
    if board.isGameOver():
        break
    
    # switch player
    playerNumber = 3 - playerNumber  


# board = GameBoard(6, 6)
# display the initial board
# board.display()

while not board.isWin('O'):
    # getting the player move
    row, column = Board.getPlayerPove(board, 'O')
    board.placeSymbol(row, column, 'O')

    # display the updated board
    board.display()

    if board.isWin('O'):
        print("Player 1 wins!")
        break

    # getting AIs move
    emptyCells = [
        (r, c)
        for r in range(board.rows)
        for c in range(board.columns)
        if board.isEmpty(r, c)
    ]
    aiRow, aiColumn = Board.random.choice(emptyCells)
    board.placeSymbol(aiRow, aiColumn, 'X')
    print()  

    # updated board
    board.display()

    if board.isWin('X'):
        print("Player 2 wins!")
        break

print("The game is now over...")
