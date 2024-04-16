import sys
import solver_dpll as sol_dpll

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

# Call the solver function from the solver_it.py file
solved_dpll = sol_dpll.dpll(data)
print(f"Solution found: {solved_dpll if solved_dpll else 'No solution found'}")

with open("output.txt", "w") as file:
    file.write(f"{solved_dpll if solved_dpll else 'No solution found'}\n")
