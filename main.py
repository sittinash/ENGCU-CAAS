import time

import config.param as Param
import model as Model
from entities import *
from vector_and_matrix import *

##########################################################################

def _buildPools():

	print "######## BUILDING ENTITIY POOLS ########"

	print "  " + time.asctime( time.localtime(time.time()) ) + " >>>> BUILDING PERIOD POOL"
	periodPool = PeriodPool()

	print "  " + time.asctime( time.localtime(time.time()) ) + " >>>> BUILDING COURSE POOL"
	coursePool = CoursePool(periodPool)

	print "  " + time.asctime( time.localtime(time.time()) ) + " >>>> BUILDING CLASSROOM POOL"
	classroomPool = ClassroomPool()

	print "  " + time.asctime( time.localtime(time.time()) ) + " >>>> RETURNING POOLS"
	return (periodPool, coursePool, classroomPool)	


##########################################################################

def main():

	periodP, courseP, croomP = _buildPools()

	print "######## FINDING SOLUTION ########"
	solutionMat = Model.findSolution(periodP, courseP, croomP)

	print "######## EXPORTING SOLUTION ########"
	print "  " + time.asctime( time.localtime(time.time()) ) + " >>>> EXPORTING MATRIX"
	solutionMat.exportSolutionDotTxt(1)
	print "  " + time.asctime( time.localtime(time.time()) ) + " >>>> EXPORTING TABLE"
	solutionMat.exportSolutionDotCSV(courseP, croomP)
	

##########################################################################

if __name__ == "__main__":
	main()

##########################################################################
