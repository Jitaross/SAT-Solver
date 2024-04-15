import sys
import solveur as sol

# Check if a filename was provided
if len(sys.argv) != 2:
    print("Usage: python3 main.py <filename>")
    sys.exit(1)

# Read the input file and store the data in a list
data = []
with open(sys.argv[1], "r") as file:
    for line in file:
        temp = [int(n) for n in line.split()]
        data.append(temp)

# Call the solver function from the solveur.py file
solved = sol.solver(data)
print(f"Solution found: {solved if solved else 'No solution found'}")

with open("output.txt", "w") as file:
    file.write("Solution found: ")
    if solved:
        file.write(" ".join(str(literal) for literal in solved))
    else:
        file.write("No solution found")
