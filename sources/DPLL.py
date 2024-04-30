"""
Dans ce script, nous avons implanté l'algorithme DPLL pour résoudre le problème SAT.
Dans un premier temps, le solveur va chercher des clauses unitaires et des littéraux purs afin de retirer les clauses
facilement solvables du problème. Une fois aucun littéral pur ou clause unitaire trouvé, il va choisir le premier
littéral de la première clause pour continuer la résolution. Si le problème n'a pas de solution, le solveur revient en
arrière (grâce à un historique de l'état du problème) et essaye avec le littéral opposé. Si aucune des 2 solutions
n'amène une solvabilité au problème alors le solveur indique que le problème initial n'est pas satisfiable. Sinon, il
retourne une instance du problème le satisfaisant.

Toutes les fonctions sont commentées en anglais par habitude, mais cette introduction est en français pour plus de
facilité de compréhension.
"""


def remove_clauses(literal, clauses):
    """
    This function will eliminate the clauses that contain the literal and the negation of the literal in other clauses.
    :param literal: The literal that will be used to eliminate the clauses.
    :param clauses: The list of the clauses.
    :return: The list of clauses updated after the elimination of the clauses.
    """
    return [[lit for lit in clause if lit != -literal] for clause in clauses if literal not in clause]


def find_unit_clause(clauses):
    """
    This function will find one unit clause in clauses.
    :param clauses: The list of the clauses.
    :return: The first unit clause found, or None if there is no unit clause.
    """
    for clause in clauses:
        if len(clause) == 1:
            return clause[0]
    return None


def find_pure_literals(literals):
    """
    This function will find one pure literal found in literals.
    :param literals: The list of literals in the clauses.
    :return: the first pure literal found, or None if there isn't.
    """
    for literal in literals:
        if -literal not in literals:
            return literal
    return None


def dpll(clauses, instance=None, history=None):
    """
    This function will solve the SAT problem using the DPLL algorithm.
    :param history: The history of clauses before modifications
    :param clauses: List of clauses.
    :param instance: The current instance of the solution.
    :return: The final instance of the solution, or None if there is no solution.
    """
    # Initialize the instance and the history for the first call
    if instance is None:
        instance = []
    if history is None:
        history = [(clauses[:], instance[:])]
    # If all the clauses are satisfied
    if not clauses:
        return instance
    # If there is an empty clause (i.e., a clause that is always false)
    if [] in clauses:
        return False

    # Find a unit clause
    unit = find_unit_clause(clauses)
    if unit:
        history.append((clauses[:], instance[:]))
        return dpll(remove_clauses(unit, clauses), instance + [unit], history)
    # Find a pure literal
    literals = {lit for clause in clauses for lit in clause}
    pure = find_pure_literals(literals)
    if pure:
        history.append((clauses[:], instance[:]))
        return dpll(remove_clauses(pure, clauses), instance + [pure], history)

    # Choose a literal
    literal = min(clauses, key=len)[0]

    # Save the current state of the problem to backtrack if needed
    count = len(history)
    # Try with the literal chosen
    res = dpll(remove_clauses(literal, clauses), instance + [literal], history)
    if res is not False:
        return res

    # Return to the previous state of the problem to try with the opposite literal
    while len(history) > count:
        history.pop()
    clauses, instance = history[-1][0], history[-1][1]

    return dpll(remove_clauses(-literal, clauses), instance + [-literal], history)


