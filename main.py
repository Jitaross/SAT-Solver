import solveur as sol

# Read the input file and store the data in a list
data = []
with open("input.txt", "r") as file:
    for line in file:
        temp = [int(n) for n in line.split()]
        data.append(temp)

# Call the solver function from the solveur.py file
solved = sol.solver(data)
print(f"Solution found: {solved}")
