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
# EXTRA CREDIT
# For (n > 4), the solution = ("(n*n)-1") I assume, rows moving right in ascending order, but where should the space be? Indication is not given. I will assume BOTTOM RIGHT.
# implementation of unsolvability is last if time. It is not necessary.
#
################################
size = 0
initial = 0
goal = 0
searchmethod = "empty"
depth = 0
numCreated = 0
numExpanded = 0
maxFringe = 0

# Print input request to console
file = open('Readme.txt', 'a')
print()
print("Type 'q' to exit and print to Readme.txt file.\nEnter Input of the form: [size] " + '"[initial state]" ' + "[search method]")
print()
prompt_input = input("Input: ")
while prompt_input != 'q':
    print()
    # Print output to console
    print("The output for now is the input so, : " + prompt_input)
    print("size: " + str(size))
    print("initial: " + '"' + str(initial) + '"')
    print("goal: " + '"' + str(goal) + '"')
    print("searchmethod: " + str(searchmethod))
    print(str(depth) + ", " + str(numCreated) + ", " + str(numExpanded) + ", " + str(maxFringe))
    print("----------------")
    print()

    # Print to a Readme.txt
    file.write("size: " + str(size))
    file.write("\ninitial: " + '"' + str(initial) + '"')
    file.write("\ngoal: " + '"' + str(goal) + '"')
    file.write("\nsearchmethod: " + str(searchmethod))
    file.write("\n" + str(depth) + ", " + str(numCreated) + ", " + str(numExpanded) + ", " + str(maxFringe))
    file.write("\n----------------\n")

    prompt_input = input("Input: ")

