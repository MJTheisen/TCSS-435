import Board
from queue import PriorityQueue

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

# it works garunteed accurate for a 2X2, but I don't have anything bigger to compare it 
# to because I think some of the sample answers are inaccurate on Sample_Readme.txt

# Breadth First Search based on textbook page 82.
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

# Depth First Search based on textbook page 88. We will use a stack, LIFO, instead of a queue,
# but honestly, its almost the same os the BFS above. If time permits, I will try to work in some
# polymorphism elements.

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

# Greedy Best First Search based on textbook page 100. Its still kind of like BFS, but I'm
# going to use a PriorityQueue and pass in a heuristic argument.

def GBFS(initial, goal, heuristic):
    visited = set([tuple(map(tuple, initial))])
    # Adding a queue like BFs, but PriorityQueue now.
    queue = PriorityQueue()
    # I want to add the heuristic on page 104 using Manhattan Distance
    queue.put((heuristic(initial, goal), (initial, 0)))
    numCreated = 0
    numExpanded = 0
    maxFringe = 1
    while not queue.empty():
        # Increment max Fringe if Fringe gets bigger than previous Fringe
        if queue.qsize() > maxFringe:
            maxFringe = queue.qsize()
        state, depth = queue.get()[1]
        # Increment based on dequeues
        numExpanded += 1
        if Board.getStateString(state) == Board.getStateString(goal):
            return depth, numCreated, numExpanded, maxFringe
        for neighbor in Board.getNeighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                visited.add(tuple(map(tuple, neighbor)))
                queue.put((heuristic(neighbor, goal), (neighbor, depth + 1)))
                # Increment node counter
                numCreated += 1          
    return -1, numCreated, numExpanded, maxFringe

# A* Search based on textbook page 100.
def AStar():




    return
