import numpy as np
import matplotlib.pyplot as plt
from pulp import *

my_lp = LpProblem("My LP Problem", LpMaximize)
x1 = LpVariable('x1', None, None, cat='Continuous', e=None)
x2 = LpVariable('x2', None, None, cat='Continuous', e=None)
x3 = LpVariable('x3', None, None, cat='Continuous', e=None)
x4 = LpVariable('x4', None, None, cat='Continuous', e=None)
x5 = LpVariable('x5', None, None, cat='Continuous', e=None)
x6 = LpVariable('x6', None, None, cat='Continuous', e=None)
# Objective function
my_lp += 2*x1 + 7*x2 + x3, "Optimization Function"

# Constraints
my_lp += x1 >= x4 - x5, "constraint 0 "
my_lp += x2 >= 0, "constraint 1 "
my_lp += x3 >= 0, "constraint 2 "
my_lp += x1 == 7 - x3, "constraint 3"
my_lp += x2 == 24 - 3*x1 + x6, "constraint 4"
my_lp += x4 >= 0, "constraint 5 "
my_lp += x5 >= 0, "constraint 6 "
my_lp += x6 >= 0, "constraint 7 "

my_lp.solve()

if my_lp.status == LpStatusInfeasible:
        print("Constraints are infeasible!")

if my_lp.status == LpStatusUnbounded:
        print("Solution is unbounded!")

if my_lp.status == LpStatusOptimal:
        print("Optimal solution exists and is equal to: {} and the optimal point is:".format(value(my_lp.objective)))
        for variable in my_lp.variables():
                print("{} = {}".format(variable.name, variable.varValue))


