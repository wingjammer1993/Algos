from pulp import *


def solve_lp(ver, w_edge, src, tgt):

    # Variables
    my_lp = LpProblem("My LP Problem", LpMaximize)
    variables = {}
    objective = []
    for elems in w_edge:
        u = elems[0]
        v = elems[1]
        variables[u, v] = LpVariable("x{}{}".format(u, v), None, None, cat='Continuous', e=None)
        if src == u:
            objective.append(variables[u, v])
    print(variables)
    print(objective)

    # Objective function
    print(sum(x for x in objective))
    my_lp += sum(x for x in objective)

    # Create constraints
    for elem in w_edge:
        i = ver.index(elem[1])
        j = ver.index(elem[0])
        my_lp += variables[elem] <= w_edge[elem]
        my_lp += variables[elem] >= 0

    for elem in ver:
        if elem != src and elem != tgt:
            n = sum([variables[x, y] for x, y in variables if y == elem])
            m = sum([variables[x, y] for x, y in variables if x == elem])
            my_lp += n == m
        if elem == src:
            n = sum([variables[x, y] for x, y in variables if y == tgt])
            m = sum([variables[x, y] for x, y in variables if x == elem])
            my_lp += n == m
        if elem == tgt:
            n = sum([variables[x, y] for x, y in variables if y == elem])
            m = sum([variables[x, y] for x, y in variables if x == src])
            my_lp += n == m
    print(my_lp)

    my_lp.solve()

    if my_lp.status == LpStatusInfeasible:
        print("Constraints are infeasible!")

    if my_lp.status == LpStatusUnbounded:
        print("Solution is unbounded!")

    if my_lp.status == LpStatusOptimal:
        print("Optimal solution exists and is equal to: {} and the optimal point is:".format(value(my_lp.objective)))
        for variable in my_lp.variables():
            print("{} = {}".format(variable.name, variable.varValue))


if __name__ == "__main__":
    vertex = [0, 1, 2, 3, 4, 5, 6, 7]
    weighted_edge = {(0, 1): 3, (0, 2): 2, (0, 3): 2, (1, 4): 5, (1, 5): 1, (2, 4): 1,
                     (2, 5): 3, (2, 6): 1, (3, 5): 1, (4, 7): 4, (5, 7): 2, (6, 7): 4}
    solve_lp(vertex, weighted_edge, 0, 7)

