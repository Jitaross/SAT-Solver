"""
This module contains the functions that will be used to solve the SAT problem.
It will use 2 rules : the unit clause rule and the pure literal rule.
It is a recursive version of the solver (DPLL).
"""


def remove_clauses(literal, clauses):
    """
    This function will eliminate the clauses that contain the literal and the negation of the literal in other clauses.
    Then it will return the new clauses list.
    :param literal: The literal that will be used to eliminate the clauses.
    :param clauses: The list of the clauses.
    :return: The list of clauses updated after the elimination of the clauses.
    """
    return [[lit for lit in clause if lit != -literal] for clause in clauses if literal not in clause]


def find_unit_clause(clauses):
    """
    This function will find one unit clause in the clauses.
    :param clauses: The list of the clauses.
    :return: The first unit clause found, or None if there is no unit clause.
    """
    for clause in clauses:
        if len(clause) == 1:
            return clause[0]
    return None


def find_pure_literals(literals, clauses):
    """
    This function will find the pure literal in the clauses.
    :param literals: The list of literals in the clauses.
    :param clauses: The list of the clauses.
    :return: the first pure literal found, or None if there isn't.
    """
    for literal in literals:
        if -literal not in literals:
            return literal
    return None


def dpll(clauses, instance=None):
    """
    This function will solve the SAT problem using the DPLL algorithm.
    :param clauses: List of clauses.
    :param instance: The current instance of the solution.
    :return: The final instance of the solution, or None if there is no solution.
    """
    if instance is None:
        instance = []
    if not clauses:
        return instance
    if [] in clauses:
        return False

    # Find a unit clause
    unit = find_unit_clause(clauses)
    if unit:
        return dpll(remove_clauses(unit, clauses), instance + [unit])
    # Find a pure literal
    literals = {lit for clause in clauses for lit in clause}
    pure = find_pure_literals(literals, clauses)
    if pure:
        return dpll(remove_clauses(pure, clauses), instance + [pure])

    # Choose a literal
    literal = min(clauses, key=len)[0]

    # Try with the literal
    res = dpll(remove_clauses(literal, clauses), instance + [literal])
    if res is not False:
        return res

    return dpll(remove_clauses(-literal, clauses), instance + [-literal])


if __name__ == "__main__":
    # Test the function
    formula_test = [[1, 2, -3], [-1], [-2], [3]]
    print(dpll(formula_test))
