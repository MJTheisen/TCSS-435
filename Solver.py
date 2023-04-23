import Board
#import Tester
# " Source code that implements BFS, DFS, GBFS, AStar to solve n-by-n sliding puzzle."

# Under the assumption that we do not have to worry about checking if the puzzle is 
# solvable or not, we will not code a function to pre-check inversions and solvability.
# We will save that for later, after ensuring proper documentation.

# Breadth First Search based on textbook page 82.


def BFS(initial, goal):
    visited = set([tuple(map(tuple, initial))])
    queue = [(initial, 0)]
    while queue:
        state, depth = queue.pop(0)
        if Board.getStateString(state) == Board.getStateString(goal):
            return depth
        for neighbor in Board.getNeighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                visited.add(tuple(map(tuple, neighbor)))
                queue.append((neighbor, depth+1))
    return -1


#def BFS(problem):


    # node = node with state = problem.InitialState, PathCost = 0
    # if #problem.GoaTest(node.State)
    #     return Solution(node)
    # fringe = fifo queue with node as the only element
    # explored = empty set
    #     return solution.
    # loop do 
    #     if empty? ()frontier then 
    #         return failure
    #     node = poprontier
    #     add node.state to explored  
    #     for each action in problem.Actions(node.state) do 
    #         child=childnode(problem,node,action)
    #         if childe.state is not in explorer or frontier then
    #             if problem.goaltest(child.state) then
    #                 return solution
    #return #solution

# Depth First Search based on textbook page 88.
def DFS():
    return

# Greedy Best First Search based on textbook page 100.
def GBFS():
    return

# A* Search based on textbook page 100.
def AStar():
    return
