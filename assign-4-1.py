from pulp import *


def solve_lp(ver, w_edge, src, tgt):

    # Variables
    my_lp = LpProblem("My LP Problem", LpMaximize)
    variables = []
    for index, vertices in enumerate(ver):
        variables.append(LpVariable("ver{0}".format(index+1), None, None, cat='Continuous', e=None))
    print(variables)

    # Objective function
    print(sum(x for x in variables))
    my_lp += sum(x for x in variables)

    # Create constraints

    my_lp += variables[ver.index(src)] == 0
    for elem in w_edge:
        i = ver.index(elem[1])
        j = ver.index(elem[0])
        my_lp += variables[i] <= variables[j] + w_edge[elem]
        print(variables[i] <= variables[j] + w_edge[elem])
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
    vertex = [6, 7, 8, 9]
    weighted_edge = {(6, 7): 3, (6, 8): 4, (7, 8): -1, (7, 9): 4, (8, 7): 1, (8, 9): 3}
    source = 1
    target = 2
    solve_lp(vertex, weighted_edge, 6, 7)

