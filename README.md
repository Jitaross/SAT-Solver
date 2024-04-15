# SAT-Solver
## Description

This is a SAT solver implemented in Python. It uses 2 rules to solve a SAT problem : Unit Clauses and Pure Literals.

_*Unit Clauses*_: A unit clause is a clause with only one literal. If a clause has only one literal, then that literal must be true for the clause to be satisfied. Therefore, we can assign that literal to be true and remove all clauses containing that literal.

_*Pure Literals*_: A pure literal is a literal that appears with only one polarity in the formula. If a literal appears only as positive or negative in the formula, then we can assign that literal to be true and remove all clauses containing that literal.

## How to run the program

The program can be run using the following command:
- `python3 main.py ../resources/input.txt` if you are in the sources directory.
- `python3 ./sources/main.py ./resources/input.txt` if you are in the root directory.

Where _input.txt is the name of the input file containing the SAT problem.

## Input Format

To solve your SAT problem, you need to provide the input in the following format:
- A clause is a list of literals separated by a space.
- A literal is a number or its negative.
- The clauses are separated by a newline.
- The input file should not contain any empty lines.
- No comments allowed in the input file.

You can find an example of the input file in the `/resources/input.txt` file.
For your SAT problem, you can just replace the clauses in the `/resources/input.txt` file with your clauses, or you replace in the command line argument the name of the input file.

## Output Format

The solution will be printed both in the console and in the output.txt file.
- If the SAT problem is satisfiable, the solution will be a list of literals that satisfy the formula.
- If the SAT problem is unsatisfiable, the solution will be "No solution found".