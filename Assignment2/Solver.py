# import Board 
# import Tester

# def aiMakeMove(board, symbol):
#     depth = 3  # depth for "several-move-look-ahead
#     bestScore, bestMove = minimax(board, depth, float('-inf'), float('inf'), True, symbol)
#     return bestMove

# def minimax(board, depth, alpha, beta, maximizingPlayer, symbol):
#     if depth == 0 or board.isGameOver():
#         return evaluate(board, symbol), None

#     if maximizingPlayer:
#         maxScore = float('-inf')
#         bestMove = None

#         for move in board.getEmptyCells():
#             row, col = move
#             board.placeSymbol(row, col, symbol)
#             score, _ = minimax(board, depth - 1, alpha, beta, False, symbol)
#             board.removeSymbol(row, col)

#             if score > maxScore:
#                 maxScore = score
#                 bestMove = move

#             alpha = max(alpha, maxScore)
#             if alpha >= beta:
#                 break

#         return maxScore, bestMove
#     else:
#         minScore = float('inf')
#         bestMove = None

#         for move in board.getEmptyCells():
#             row, col = move
#             board.placeSymbol(row, col, symbol)
#             score, _ = minimax(board, depth - 1, alpha, beta, True, symbol)
#             board.removeSymbol(row, col)

#             if score < minScore:
#                 minScore = score
#                 bestMove = move

#             beta = min(beta, minScore)
#             if beta <= alpha:
#                 break

#         return minScore, bestMove
    
# def countWinningConfigurations(board, symbol):
#     count = 0
    
#     # check rows
#     for row in board:
#         if symbol in row and '/' not in row:
#             count += 1
    
#     # check columns 
#     numRows = len(board)
#     numCols = len(board[0])
#     for col in range(numCols):
#         column = [board[row][col] for row in range(numRows)]
#         if symbol in column and '/' not in column:
#             count += 1
    
#     # check diagonals 
#     if numRows == numCols:  # square board only. fix later.
#         diagonal1 = [board[i][i] for i in range(numRows)]
#         diagonal2 = [board[i][numCols - 1 - i] for i in range(numRows)]
#         if symbol in diagonal1 and '/' not in diagonal1:
#             count += 1
#         if symbol in diagonal2 and '/' not in diagonal2:
#             count += 1
    
#     return count


# def evaluate(board, symbol):
#     # set to 10 for now
#     winningConfigWeight = 10
#     numWinningConfigurations = countWinningConfigurations(board, symbol)
#     utilityValue = numWinningConfigurations * winningConfigWeight
    
#     return utilityValue