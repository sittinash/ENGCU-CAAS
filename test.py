import config.param as Param
from entities import *
import vector_and_matrix as VAM

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

def testVectorAndMatrix():

	return -1


##########################################################################

def main():

	#testPeriodPool()
	#testCoursePool()
	#testClassroomPool()

	testVectorAndMatrix()
	

if __name__ == "__main__":
	main()