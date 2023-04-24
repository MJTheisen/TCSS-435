import Board

#####################################
#                                   #
#         Michael Theisen           #
#           TCSS 435 AI             #
#           04/23/2023              #
#                                   #
#####################################


# " Source code that implements BFS, DFS, GBFS, AStar to solve n-by-n sliding puzzle."

# Under the assumption that we do not have to worry about checking if the puzzle is 
# solvable or not, we will not code a function to pre-check inversions and solvability.
# We will save that for later, after ensuring proper documentation.

# Breadth First Search based on textbook page 82.
# it works garunteed accurate for a 2X2, but I don't have anything bigger to compare it 
# to because I think some of the sample answers are inaccurate on Sample_Readme.txt
# The focus here was using a queue FIFO instead of a stack.
def BFS(initial, goal):
    visited = set([tuple(map(tuple, initial))])
    queue = [(initial, 0)]
    # Added node counter. 
    numCreated = 0
    # Added expansion counter that failed.
    numExpanded = 0
    # Added maximum Fringe size counter.
    maxFringe = 0
    while queue:
        # Increment max Fringe if Fringe gets bigger than previous Fringe
        if len(queue) > maxFringe:
            maxFringe = len(queue)
        # Added depth
        state, depth = queue.pop(0)
        # Increment based on dequeues
        numExpanded += 1
        if Board.getStateString(state) == Board.getStateString(goal):
            return depth, numCreated, numExpanded, maxFringe
        for neighbor in Board.getNeighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                visited.add(tuple(map(tuple, neighbor)))
                # Increment depth
                queue.append((neighbor, depth + 1))
                # Increment node counter
                numCreated += 1          
    return -1, numCreated, numExpanded, maxFringe

# Depth First Search based on textbook page 88. We will use a stack, LIFO, instead of a queue
def DFS(initial, goal):
    visited = set([tuple(map(tuple, initial))])
    stack = [(initial, 0)]
    # Added node counter. 
    numCreated = 0
    # Added expansion counter that failed.
    numExpanded = 0
    # Added maximum Fringe size counter.
    maxFringe = 0
    while stack:
        # Increment max Fringe if Fringe gets bigger than previous Fringe
        if len(stack) > maxFringe:
            maxFringe = len(stack)
        # Added depth
        state, depth = stack.pop()
        # Increment based on dequeues
        numExpanded += 1
        if Board.getStateString(state) == Board.getStateString(goal):
            return depth, numCreated, numExpanded, maxFringe
        for neighbor in Board.getNeighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                visited.add(tuple(map(tuple, neighbor)))
                # Increment depth
                stack.append((neighbor, depth + 1))
                # Increment node counter
                numCreated += 1
            # To remove the likelihood of cycles, we skip visited nodes and just continue on.    
            else:
                break          
    return -1, numCreated, numExpanded, maxFringe

# Greedy Best First Search based on textbook page 100.
def GBFS():
    return

# A* Search based on textbook page 100.
def AStar():
    return
