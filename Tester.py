import Board
import Solver 
# "A tester file that connects your Board and Solver code."
#
#
#
#
################################
#
# REQUIRED
# for (n = 2), the solution = ("213 ") ALWAYS. Rows move to the left in ascending order, but space is always BOTTOM RIGHT.
# for (n = 3), the solution = (" 12345678") ALWAYS. Rows move to the right in ascending order, but space is always TOP LEFT.
# for (n = 4), the solution = ("123456789ABCDEF ") ALWAYS. Rows move to the right in ascending order, but space is always BOTTOM RIGHT.
# 
# EXTRA CREDIT
# For (n > 4), the solution = ("(n*n)-1") I assume, rows moving right in ascending order, but where should the space be? Indication is not given. I will assume BOTTOM RIGHT.
# implementation of unsolvability is last if time. It is not necessary.
#
################################
#size = 0
#initial = 0
#goal = 0
#searchmethod = "empty"
#depth = 0
numCreated = 0
numExpanded = 0
maxFringe = 0



def printState(size, initial, goal, searchmethod, depth):
    initialStr = "".join(str(i) for row in initial for i in row)
    goalStr = "".join(str(i) for row in goal for i in row)

    print(f'{"size:"}  {size}')
    print(f'{"initial"}  {initialStr}"')
    print(f'{"goal: "}  "{goalStr}"')  
    print(f'{"searchmethod: "} {searchmethod}')
    print(f'{depth} ", " {numCreated} ", " {numExpanded} ", " {maxFringe}')



# Print input request to console
file = open('Readme.txt', 'a')
print()
print("Type 'q' to exit and print to Readme.txt file.\nEnter Input of the form: [size] " + '"[initial state]" ' + "[search method]")
print()
promptInput = input("Input: ")
size, newInitial1, newInitial2, searchmethod = promptInput.split()
quotesInitial = newInitial1 + ' ' + newInitial2 
newInitial = quotesInitial[1:-1]

# Convert the input string to a list of characters
n = int(size)
charList = list(newInitial)

# Define an empty list to hold the sublists
initial = []

# Loop through the characters and group them into sublists of four
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
# Since no specification for goal state above 4 was given, I will simply just 
# adopt "Row Order, Space in Bottom Right" similar to that of n = 4 for all puzzles
# of size n > 4.
# if n > 4:


depth = Solver.BFS(initial, goal)

solution = Solver.BFS(initial, goal)


    
while promptInput != 'q':
    print()
    # Print output to console
    # print("size: " + str(size))
    # print("initial: " + '"' + str(initial) + '"')
    # print("goal: " + '"' + str(goal) + '"')
    # print("searchmethod: " + str(searchmethod))
    # print(str(depth) + ", " + str(numCreated) + ", " + str(numExpanded) + ", " + str(maxFringe))
    # print("----------------")
    # print()


        
    if solution:
        printState(size, initial, goal, searchmethod, depth)
        print()
        # Print output to console
        # print("size: " + str(size))
        # print("initial: " + '"' + str(initial) + '"')
        # print("goal: " + '"' + str(goal) + '"')
        # print("searchmethod: " + str(searchmethod))
        # print(str(depth) + ", " + str(numCreated) + ", " + str(numExpanded) + ", " + str(maxFringe))
        # print("----------------")
        # print()
        # Print to a Readme.txt
        file.write("size: " + str(size))
        file.write("\ninitial: " + '"' + str(initial) + '"')
        file.write("\ngoal: " + '"' + str(goal) + '"')
        file.write("\nsearchmethod: " + str(searchmethod))
        file.write("\n" + str(depth) + ", " + str(numCreated) + ", " + str(numExpanded) + ", " + str(maxFringe))
        file.write("\n----------------\n")
    else:
        print("No solution found")

    # promptInput = input("Input: ")
    # size, newInitial, searchmethod = promptInput.split()   

