import config.param as Param
import model as Model
from entities import *
from vector_and_matrix import *

##########################################################################

def _buildPools():

	periodPool = PeriodPool()
	coursePool = CoursePool(periodPool)
	classroomPool = ClassroomPool()

	return (periodPool, coursePool, classroomPool)


##########################################################################

def testPeriod():

	with open(Param.periodFile) as fh:
		reader = csv.reader(fh)
		listTable = list(reader)

	testPeriod1 = Period(listTable[1])
	testPeriod2 = Period(listTable[67])
	testPeriod3 = Period(listTable[100])
	testPeriod4 = Period(listTable[157])

	testPeriod1.printPeriod()
	testPeriod2.printPeriod()
	testPeriod3.printPeriod()
	testPeriod4.printPeriod()


def testPeriodPool():

	# TEST CONSTRUCTOR AND printPool()
	periodP = PeriodPool()
	periodP.printPool()
	print "  >>>> Count => " + str(periodP.count)
	print ""

	# TEST toTimetable(~)
	day = "TU"
	startTime = "12:30"
	endTime = "13:00"

	timetable = periodP.toTimetable(day, startTime, endTime)

	if timetable == -1:
		print "!!! ERROR !!!"
		print ""

	for i in range(len(timetable)):
		print str(i) + " -> " + str(timetable[i])
	print ""

	# TEST GETTERS
	periodP.getPeriodByIndex(156).printPeriod()


##########################################################################

def testCourse():
	
	with open(Param.courseFile) as fh:
		reader = csv.reader(fh)
		listTable = list(reader)

	testCourse1 = Course(listTable[1])
	testCourse2 = Course(listTable[67])
	testCourse3 = Course(listTable[100])
	testCourse4 = Course(listTable[684])

	testCourse1.printCourse()
	testCourse2.printCourse()
	testCourse3.printCourse()
	testCourse4.printCourse()


def testCoursePool():

	# TEST CONSTRUCTOR AND printPool()
	courseP = CoursePool()
	courseP.printPool()
	print "  >>>> Count => " + str(courseP.count)
	print ""

	# TEST GETTERS
	courseP.getCourseByIndex(683).printCourse()


##########################################################################

def testClassroom():

	with open(Param.classroomFile) as fh:
		reader = csv.reader(fh)
		listTable = list(reader)

	testRoom1 = Classroom(listTable[1])
	testRoom2 = Classroom(listTable[67])
	testRoom3 = Classroom(listTable[100])
	testRoom4 = Classroom(listTable[104])

	testRoom1.printClassroom()
	testRoom2.printClassroom()
	testRoom3.printClassroom()
	testRoom4.printClassroom()
	

def testClassroomPool():

	# TEST CONSTRUCTOR AND printPool()
	roomP = ClassroomPool()
	roomP.printPool()
	print "  >>>> Count => " + str(roomP.count)
	print ""

	# TEST GETTERS
	roomP.getClassroomByIndex(103).printClassroom()


##########################################################################

def testCapacityVector(): # OBSOLETE

	croomP = ClassroomPool()
	capacityVec = CapacityVector(croomP)

	capacityVec.printVector() 
	print capacityVec.getCapacityByClassroomIndex(8) #40


def testPeriodCountVector(): # OBSOLETE

	courseP = CoursePool(PeriodPool())
	periodCountVec = PeriodCountVector(courseP)

	periodCountVec.printVector()
	print periodCountVec.getPeriodCountByCourseIndex(4) #3


def testSchedulingMatrix(): # OBSOLETE

	courseP = CoursePool(PeriodPool())
	schedulingMat = SchedulingMatrix(courseP)

	schedulingMat.printMatrix()
	print str(schedulingMat.m) + " x " + str(schedulingMat.n) 
	print schedulingMat.getValueByIndexes(5, 4) #1
	print schedulingMat.getValueByIndexes(2, 5) #0


def testAssignmentAvailabilityMatrix(): # OBSOLETE

	courseP = CoursePool(PeriodPool())
	croomP = ClassroomPool()
	aaMat = AssignmentAvailabilityMatrix(courseP, croomP)

	aaMat.printMatrix()
	print str(aaMat.m) + " x " + str(aaMat.n) 
	print aaMat.getValueByIndexes(5, 4) #1
	print aaMat.getValueByIndexes(2, 5) #0


##########################################################################

def testFindSolution():

	Model.findSolution()


##########################################################################

def main():

	#testPeriod()
	#testPeriodPool()

	#testCourse()
	#testCoursePool()

	#testClassroom()
	#testClassroomPool()

	#testCapacityVector()
	#testPeriodCountVector()
	#testSchedulingMatrix()
	#testAssignmentAvailabilityMatrix()

	testFindSolution()
	

##########################################################################

if __name__ == "__main__":
	main()

##########################################################################
