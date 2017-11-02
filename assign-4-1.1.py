import numpy as np
import matplotlib.pyplot as plt
from pulp import *

# Construct lines
# x >= 0
# x <= 5
x = np.linspace(0, 5, endpoint=True)
# y >= 0
y1 = (x*0)
# y <=  5x/2
y2 = 5 * x / float(2)
# y <=  7 - x
y3 = 7 - x


plt.plot(x, y1, label=r'$y\geq0$')
plt.plot(x, y2, label=r'$2y\leq5x$')
plt.plot(x, y3, label=r'$y\leq7-x$')

plt.xlim((0, 5))
plt.ylim((0, 10))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

# Fill feasible region
y5 = np.minimum(y1, y3)
y6 = np.maximum(y1, y3)
plt.fill_between(x, y5, y6, where=y5 > y6, color='grey', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

my_lp = LpProblem("My LP Problem", LpMaximize)
x1 = LpVariable('x1', None, None, cat='Continuous', e=None)
x2 = LpVariable('x2', None, None, cat='Continuous', e=None)


# Objective function
my_lp += 5*x1 - 3*x2, "Optimization Function"

# Constraints
my_lp += x1 >= 0, "constraint 1 "
my_lp += x1 <= 5, "constraint 2 "
my_lp += x2 <= 7 - x1, "constraint 3"
my_lp += 2*x2 <= 5*x1, "constraint 4"
my_lp += x2 >= 0, "constraint 5 "

my_lp.solve()

if my_lp.status == LpStatusInfeasible:
        print("Constraints are infeasible!")

if my_lp.status == LpStatusUnbounded:
        print("Solution is unbounded!")

if my_lp.status == LpStatusOptimal:
        print("Optimal solution exists and is equal to: {} and the optimal point is:".format(value(my_lp.objective)))
        for variable in my_lp.variables():
                print("{} = {}".format(variable.name, variable.varValue))



