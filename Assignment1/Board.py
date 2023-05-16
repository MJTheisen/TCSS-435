
#####################################
#                                   #
#         Michael Theisen           #
#           TCSS 435 AI             #
#           04/23/2023              #
#                                   #
#####################################


# Source code that models an n-by-n board with sliding tiles. 
# Your heuristic function resides in this file.  

# Get the location of the black square
def getBlankPosition(state):
    for i, row in enumerate(state):
        if ' ' in row:
            return i, row.index(' ')

#Get the location of the neightbors.
def getNeighbors(state):
    neighbors = []
    row, col = getBlankPosition(state)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for move in moves:
        newRow = row + move[0]
        newCol = col + move[1]
        if 0 <= newRow < len(state) and 0 <= newCol < len(state):
            neighbor = [row[:] for row in state]
            neighbor[row][col], neighbor[newRow][newCol] = neighbor[newRow][newCol], neighbor[row][col]
            neighbors.append(neighbor)
    return neighbors

# Get a string from the tuples for output rquirement purposes.
# (coding it as a map tuples was easier to understand and debug.)
def getStateString(state):
    return ''.join(str(num) for row in state for num in row)


# The heuristic is as follows:
# Manhattan Distance

def heuristic(state, goal):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == 0:
                continue
            val = state[i][j]
            xGoal, yGoal = divmod(goal.index(val), len(goal))
            distance += abs(i - xGoal) + abs(j - yGoal)
    return distance