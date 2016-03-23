from pulp import *

#pulp.pulpTestAll()

model = LpProblem("test", LpMinimize)

x = LpVariable("x", 0, 4)
y = LpVariable("y", -1, 1)
z = LpVariable("z", 0)

model += x + 4*y + 9*z

model += x + y <= 5
model += x + z >= 10
model += -y + z == 7

GLPK().solve(model)

for v in model.variables():
	print v.name + " = " + str(v.varValue)

print "Objective value: " + str(value(model.objective))