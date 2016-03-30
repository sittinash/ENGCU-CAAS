from pulp import *

import config.param as Param
from entities import *
from vector_and_matrix import *

##########################################################################

def findSolution(periodPool, coursePool, classroomPool):

	# INSTANTIATE VECTORS AND MATRICES
	capacityVec = CapacityVector(classroomPool)
	periodCountVec = PeriodCountVector(coursePool)
	schedulingMat = SchedulingMatrix(coursePool)
	aaMat = AssignmentAvailabilityMatrix(coursePool, classroomPool)

	# SET UP t, m, n
	t = schedulingMat.n
	m = periodCountVec.size
	n = capacityVec.size

	print "(t, m, n) = " + str((t, m, n))
	print "############################################"
	
	# INSTANTIATE DECISION VARIABLES
	x = LpVariable.dicts("assignment.variables", (range(t), range(m), range(n)), 0, 1, LpInteger)
	k = LpVariable.dicts("dummy.variables", (range(m), range(n)), 0, 1, LpInteger)

	# INSTANTIATE A PROBLEM
	prob = LpProblem("eng.cu.classroom.assignment.problem", LpMinimize)

	# DEFINE OBJECTIVE FUNCTION
	prob += lpSum([capacityVec.getCapacityByClassroomIndex(i)*x[p][i][j] for p in range(t) for i in range(m) for j in range(n)])

	# DEFINE CONSTRAINTS
	for p in range(t):
		for i in range(m):
			prob += lpSum([x[p][i][j] for j in range(n)]) == schedulingMat.getValueByIndexes(i, p)#, "scheduling.constraint." + str(p) + "." + str(j)

	for p in range(t):
		for j in range(n):
			prob += lpSum([x[p][i][j] for i in range(m)]) <= 1#, "one.to.one.constraint." + str(p) + "." + str(j)

	for i in range(m):
		for j in range(n):
			prob += lpSum([x[p][i][j] for p in range(t)]) == k[i][j]*periodCountVec.getPeriodCountByCourseIndex(i) + (1-k[i][j])*0#, "periods.count.constraint." + str(i) + "." + str(j)

	for p in range(t):
		for i in range(m):
			for j in range(n):
				prob += x[p][i][j] <= aaMat.getValueByIndexes(i, j)#, "assignment.avail.constraint." + str(p) + "." + str(i) + "." + str(j)

	# SOLVE PROBLEM USING GLPK SOLVER
	GLPK().solve(prob)

	# PRINT OUTPUTS
	solutionMat = SolutionMatrix(t, m, n) 

	for v in prob.variables():

		tempList = v.name.split('_')

		if tempList[0] == "assignment.variables":

			p = int(tempList[1])
			i = int(tempList[2])
			j = int(tempList[3])
			val = v.varValue
			solutionMat.setValueAtIndexes(p, i, j, val)

			if val > 0:
				print "[" + str(capacityVec.getCapacityByClassroomIndex(i)) + "] " + str(p) + ", " + str(i) + ", " + str(j) + " = " + str(val)

	print "Objective value: " + str(value(prob.objective))
	print "Solution status: " + LpStatus[prob.status]

	return solutionMat


##########################################################################
