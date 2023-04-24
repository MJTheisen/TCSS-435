import Board
import Solver 

#####################################
#                                   #
#         Michael Theisen           #
#           TCSS 435 AI             #
#           04/23/2023              #
#                                   #
#####################################

# "A tester file that connects your Board and Solver code."
#
# REQUIRED
# for (n = 2), the solution = ("213 ") ALWAYS. Rows move to the left in ascending order, but space is always BOTTOM RIGHT.
# for (n = 3), the solution = (" 12345678") ALWAYS. Rows move to the right in ascending order, but space is always TOP LEFT.
# for (n = 4), the solution = ("123456789ABCDEF ") ALWAYS. Rows move to the right in ascending order, but space is always BOTTOM RIGHT.
# 
# EXTRA CREDIT
# For (n > 4), the solution = ("(n*n)-1") I assume, rows moving right in ascending order, but where should the space be? Indication is not given. I will assume BOTTOM RIGHT.
# implementation of unsolvability is last if time. It is not necessary.

def printState(size, initial, goal, searchmethod, depth):
    initialStr = "".join(str(i) for row in initial for i in row)
    goalStr = "".join(str(i) for row in goal for i in row)

    # Print output to console
    print(f'{"size:"} {size}')
    print(f'{"initial:"} "{initialStr}"')
    print(f'{"goal:"} "{goalStr}"')  
    print(f'{"searchmethod:"} {searchmethod}')
    print(f'{depth}, {numCreated}, {numExpanded}, {maxFringe}')

    # Print output to Readme.txt
    file = open('Readme.txt', 'a')
    file.write("size: " + str(size))
    file.write("\ninitial: " + '"' + str(initialStr) + '"')
    file.write("\ngoal: " + '"' + str(goalStr) + '"')
    file.write("\nsearchmethod: " + str(searchmethod))
    file.write("\n" + str(depth) + ", " + str(numCreated) + ", " + str(numExpanded) + ", " + str(maxFringe))
    file.write("\n----------------\n")

promptInput=0

while promptInput != 'q':
    print()
    print("Enter q to quit.")
    print("Enter Input of the form: [size] " + '"[initial state]" ' + "[search method]")
    print()
    promptInput = input("Input: ")
    size, newInitial1, newInitial2, searchmethod = promptInput.split()
    quotesInitial = newInitial1 + ' ' + newInitial2 
    newInitial = quotesInitial[1:-1]

    # Convert the input string to a list of characters
    n = int(size)
    charList = list(newInitial)

    # Define an empty list to hold the n-length lists
    initial = []

    # Loop through the characters and group them into n-lists of n
    for i in range(0, len(charList), n):
        charInitial = charList[i:i+n]
        initial.append(charInitial)

    # Checking constant goal state for n = 2 per required Goal State on specification.
    if n == 2:
        # initial = [
        #     ['3', '2'],
        #     [' ', '1'],
        # ]
        goal = [
            ['2', '1'],
            ['3', ' '],
        ]

    # Checking constant goal state for n = 3 per required Goal State on specification.
    if n == 3:
        # initial = [
        #     ['4', '7', '3'],
        #     ['1', '5', '8'],
        #     ['6', '2', ' ']
        # ]
        goal = [
            [' ', '1', '2'],
            ['3', '4', '5'],
            ['6', '7', '8']
        ]

    # Checking constant goal state for n = 4 per required Goal State on specification.
    if n == 4:
        # initial = [
        #     ['1', '2', '3', '4'],
        #     ['5', '6', '7', '8'],
        #     ['9', 'A', 'B', ' '],
        #     ['D', 'E', 'F', 'C']
        # ]
        goal = [
            ['1', '2', '3', '4'],
            ['5', '6', '7', '8'],
            ['9', 'A', 'B', 'C'],
            ['D', 'E', 'F', ' ']
        ]

    if n == 5:
        goal = [
            ['1', '2', '3', '4', '5'],
            ['6', '7', '8', '9', 'A'],
            ['B', 'C', 'D', 'E', 'F'],
            ['G', 'H', 'I', 'J', 'K'],
            ['L', 'M', 'N', 'O', ' ']
        ]
    # Since no specification for goal state above 4 was given, I will simply just 
    # adopt "Row Order, Space in Bottom Right" similar to that of n = 4 for all puzzles
    # of size n > 4.
    # if n > 4:
    if searchmethod == 'BFS':
        depth = Solver.BFS(initial, goal)[0]
        numCreated = Solver.BFS(initial, goal)[1]
        numExpanded = Solver.BFS(initial, goal)[2]
        maxFringe = Solver.BFS(initial, goal)[3]
        solution = Solver.BFS(initial, goal)
    if searchmethod == 'DFS':
        depth = Solver.DFS(initial, goal)[0]
        numCreated = Solver.DFS(initial, goal)[1]
        numExpanded = Solver.DFS(initial, goal)[2]
        maxFringe = Solver.DFS(initial, goal)[3]
        solution = Solver.DFS(initial, goal)



        
    print() 
    if solution:
        printState(size, initial, goal, searchmethod, depth)
        print()    
    else:
        print("No solution found") 
    if promptInput == 'q':
        break
    promptInput   

