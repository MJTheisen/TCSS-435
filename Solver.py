import Board
import heapq

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

# Duplication of BFS for now.
def GBFS(initial, goal):
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

# def GBFS(initial, goal):
#     pq = [(Board.heuristic(initial, goal), initial, 0)]
#     visited = set([tuple(map(tuple, initial))])
#     numCreated = 0
#     numExpanded = 0
#     maxFringe = 0
#     while pq:
#         if len(pq) > maxFringe:
#             maxFringe = len(pq)
#         state = heapq.heappop(pq)[1]
#         numExpanded += 1
#         if state == goal:
#             return Board.heuristic(state, goal), numCreated, numExpanded, maxFringe
#         for neighbor in Board.getNeighbors(state):
#             if tuple(map(tuple, neighbor)) not in visited:
#                 visited.add(tuple(map(tuple, neighbor)))
#                 numCreated += 1
#                 heapq.heappush(pq, (Board.heuristic(neighbor, goal), neighbor, 0))
#     return -1, numCreated, numExpanded, maxFringe

# Duplicate of BFS for now. so that it stops crashing.
def AStar(initial, goal):
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

    
# def AStar(initial, goal):
#     pq = [(0 + heuristic(initial, goal), initial, 0, [])]
#     visited = set() 
#     while pq:
#         # Sort queue so that lowest cost states are expanded first
#         pq.sort() 
#         # Get state with lowest cost from queue
#         state = pq.pop(0) 
#         current, depth, path = state[1], state[2], state[3] # unpack state values
#         visited.add(tuple(current)) # mark current state as visited
#         if current == goal:
#             return (depth, path + [current]) # goal state found, return depth and path to it
#         for neighbor in Board.neighbors(current):
#             if tuple(neighbor) not in visited:
#                 pq.append((depth + 1 + Board.heuristic(neighbor, goal), neighbor, depth + 1, path + [current])) # add neighbor to queue
#     return None # goal state not found, return None
