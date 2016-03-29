import config.param as Param
import model_solution as Soln
from entities import *
from vector_and_matrix import *

##########################################################################

def testCourse(): # OBSOLETE
	
	testListCourse = ['6', '2110116', 'TEST COURSE 06', 'MO', '9:30', '11:00', 'LECTURE', '120']
	testColList =['COURSE_NO', 'COURSE_CODE', 'COURSE_NAME', 'DAY', 'START_TIME', 'END_TIME', 'TYPE', 'ENROLL']

	room = Course(testListCourse, testColList)
	room.printCourse()


def testClassroom(): # OBSOLETE

	testListClassroom = ['12', 'ENG3', '412', '60', 'lecture', 'x', 'E990']
	testConlumnList = ['CLASSROOM_NO', 'BUILDING', 'CLASSROOM_CODE', 'CAPACITY', 'TYPE', 'ATTR1', 'ATTR2']

	room = Classroom(testListClassroom, testConlumnList)
	room.printClassroom()


##########################################################################

def _buildPools():

	periodPool = PeriodPool()
	coursePool = CoursePool(periodPool)
	classroomPool = ClassroomPool()

	return (periodPool, coursePool, classroomPool)


def testPeriodPool():

	# TEST CONSTRUCTOR AND printPool()
	periodP = PeriodPool()
	periodP.printPool()
	print "Count => " + str(periodP.count)

	# TEST toTimetable(~)
	day = "MO"
	startTime = "9:00"
	endTime = "12:00"

	timetable = periodP.toTimetable(day, startTime, endTime)

	if timetable == -1:
		print "!!! ERROR !!!"

	for i in range(len(timetable)):
		print str(i) + " -> " + str(timetable[i])

	# TEST GETTERS
	periodP.getPeriodByIndex(1).printPeriod()


def testCoursePool():

	# TEST CONSTRUCTOR AND printPool()
	periodP = PeriodPool()
	courseP = CoursePool(periodP)
	courseP.printPool()
	print "Count => " + str(courseP.count)

	# TEST GETTERS
	courseP.getCourseByIndex(4).printCourse()


def testClassroomPool():

	# TEST CONSTRUCTOR AND printPool()
	croomP = ClassroomPool()
	croomP.printPool()
	print "Count => " + str(croomP.count)

	# TEST GETTERS
	croomP.getClassroomByIndex(17).printClassroom()


##########################################################################

def testCapacityVector():

	croomP = ClassroomPool()
	capacityVec = CapacityVector(croomP)

	capacityVec.printVector() 
	print capacityVec.getCapacityByClassroomIndex(8) #40


def testPeriodCountVector():

	courseP = CoursePool(PeriodPool())
	periodCountVec = PeriodCountVector(courseP)

	periodCountVec.printVector()
	print periodCountVec.getPeriodCountByCourseIndex(4) #3


def testSchedulingMatrix():

	courseP = CoursePool(PeriodPool())
	schedulingMat = SchedulingMatrix(courseP)

	schedulingMat.printMatrix()
	print str(schedulingMat.m) + " x " + str(schedulingMat.n) 
	print schedulingMat.getValueByIndexes(5, 4) #1
	print schedulingMat.getValueByIndexes(2, 5) #0


def testAssignmentAvailabilityMatrix():

	courseP = CoursePool(PeriodPool())
	croomP = ClassroomPool()
	aaMat = AssignmentAvailabilityMatrix(courseP, croomP)

	aaMat.printMatrix()
	print str(aaMat.m) + " x " + str(aaMat.n) 
	print aaMat.getValueByIndexes(5, 4) #1
	print aaMat.getValueByIndexes(2, 5) #0


##########################################################################

def testModelSolution():

	periodP, courseP, croomP = _buildPools()
	solutionMat = Soln.lengDeeDeeSaiMangLeoi(periodP, courseP, croomP)

	solutionMat.printMatrix()


##########################################################################

def main():

	#testPeriodPool()
	#testCoursePool()
	#testClassroomPool()

	#testCapacityVector()
	#testPeriodCountVector()
	#testSchedulingMatrix()
	#testAssignmentAvailabilityMatrix()

	testModelSolution()
	

##########################################################################

if __name__ == "__main__":
	main()


##########################################################################
