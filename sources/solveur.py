"""
This module contains the functions that will be used to solve the SAT problem.
It will use 2 rules : the unit clause rule and the pure literal rule.
"""


def unit_clauses(literal, clauses):
    """
    This function will eliminate the clauses that contain the literal and the negation of the literal in other clauses.
    Then it will return the new clauses list.
    :param literal: The literal that will be used to eliminate the clauses.
    :param clauses: The list of the clauses.
    :return: The list of clauses updated after the elimination of the clauses.
    """
    new_clauses = []
    for clause in clauses:
        if literal not in clause:
            # Keep the clause if the literal is not in it, and if the clause is not empty
            new_clause = [x for x in clause if x != -literal]
            if new_clause:
                new_clauses.append(new_clause)
    return new_clauses


def pure_literals(literal, clauses):
    """
    This function will eliminate the clauses that contain the pure literal.
    Then it will return the new clauses list.
    :param literal: The list of literals that will be used to eliminate the clauses.
    :param clauses: The list of the clauses.
    :return: The list of clauses updated after the elimination of the clauses.
    """
    new_clauses = []
    for clause in clauses:
        # Keep the clause if the literal is not in it
        if literal not in clause:
            new_clauses.append(clause)
    return new_clauses


def find_pure_literals(clauses):
    """
    This function will find the pure literals in the clauses.
    :param clauses: The list of the clauses.
    :return: The list of the pure literals.
    """
    literals = []
    literals_temp = []
    for clause in clauses:
        for literal in clause:
            if literal not in literals_temp:
                literals_temp.append(literal)
    for literal in literals_temp:
        if -literal not in literals_temp:
            literals.append(literal)
    return literals


def find_unit_clauses(clauses):
    """
    This function will find the unit clauses in the clauses.
    :param clauses: The list of the clauses.
    :return: The list of the unit clauses.
    """
    literals = []
    for clause in clauses:
        if len(clause) == 1:
            literals.append(clause[0])
    return literals


def solver(clauses):
    """
    This function will solve the SAT problem using the unit clause rule and the pure literal rule.
    :param clauses: The list of the clauses.
    :return: The list of the clauses updated after the elimination of the clauses.
    """
    # The list of the literals that will be used to eliminate the clauses
    literals_res = []
    while len(clauses) > 0:
        # Find the unit clauses
        literals_unit = find_unit_clauses(clauses)
        # Find the pure literals
        literals_pure = find_pure_literals(clauses)
        if literals_unit:
            for literal in literals_unit:
                clauses = unit_clauses(literal, clauses)
                literals_res.append(literal)
                print(f"Unit clause found: {literal}\nClauses left: {clauses}\n")
        elif literals_pure:
            for literal in literals_pure:
                if len(clauses) != 0:
                    clauses = pure_literals(literal, clauses)
                    literals_res.append(literal)
                    print(f"Pure literal found: {literal}\nClauses left: {clauses}\n")
        else:
            # If there are no unit clauses and no pure literals, then the problem is unsatisfiable
            return None

    return literals_res


if __name__ == '__main__':
    l_test = [[1, 2, 3], [1, 2, -3], [1, -2, 3], [1, -2, -3], [-2, 3, -4]]
    print(unit_clauses(2, l_test))
    print(pure_literals(1, l_test))
