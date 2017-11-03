import numpy as np
import matplotlib.pyplot as plt
from pulp import *

my_lp = LpProblem("My LP Problem", LpMaximize)
x1 = LpVariable('x1', None, None, cat='Continuous', e=None)
x2 = LpVariable('x2', None, None, cat='Continuous', e=None)
x3 = LpVariable('x3', None, None, cat='Continuous', e=None)

# Objective function
my_lp += 1000*x1 + 1200*x2 + 12000*x3, "Optimization Function"

# Constraints
my_lp += x1 <= 40, "constraint 1 "
my_lp += x2 <= 30, "constraint 2 "
my_lp += x3 <= 20, "constraint 3 "
my_lp += x1 + x2 + x3 <= 60, "constraint 4 "
my_lp += 2*x1 + x2 + x3 <= 100, "constraint 5 "
my_lp += x1 >= 0, "constraint 6 "
my_lp += x2 >= 0, "constraint 7 "
my_lp += x3 >= 0, "constraint 8 "


my_lp.solve()

if my_lp.status == LpStatusInfeasible:
        print("Constraints are infeasible!")

if my_lp.status == LpStatusUnbounded:
        print("Solution is unbounded!")

if my_lp.status == LpStatusOptimal:
        print("Optimal solution exists and is equal to: {} and the optimal point is:".format(value(my_lp.objective)))
        for variable in my_lp.variables():
                print("{} = {}".format(variable.name, variable.varValue))


