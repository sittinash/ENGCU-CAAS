import config.param as Param
from entities import *
import data_transformation as Transform

##########################################################################

def testDataTransformation():

	courseFile = Param.courseFile
	classroomFile = Param.classroomFile

	# TEST periodDictionary()
	#"""
	periodDict = Transform.periodDictionary(Param.courseFile)
	for key, val in periodDict.iteritems():
		val.printPeriod()
	#"""

	# TEST courseDictionary()
	"""
	courseDict = Transform.courseDictionary(Param.courseFile)
	for key, val in courseDict.iteritems():
		val.printCourse()
	"""
	
	# TEST classroomDictionary(), capacityVector()
	"""
	classroomDict = Transform.classroomDictionary(Param.classroomFile)
	dictCapVector = Transform.capacityVector(classroomDict)

	for key, val in classroomDict.iteritems():
		print key
		val.printClassroom()

	print ""
	for key, val in dictCapVector.iteritems():
		print (key, val)
	"""

def testClassroom():

	testListClassroom = ['12', 'ENG3', '412', '60', 'lecture', 'x', 'E990']
	testConlumnList = ['CLASSROOM_NO', 'BUILDING', 'CLASSROOM_CODE', 'CAPACITY', 'TYPE', 'ATTR1', 'ATTR2']

	room = Classroom(testListClassroom, testConlumnList)
	room.printClassroom()


def testCourse():

	testListCourse = ['6', '2110116', 'TEST COURSE 06', 'MO', '9:30', '11:00', 'LECTURE', '120']
	testColList =['COURSE_NO', 'COURSE_CODE', 'COURSE_NAME', 'DAY', 'START_TIME', 'END_TIME', 'TYPE', 'ENROLL']

	room = Course(testListCourse, testColList)
	room.printCourse()


##########################################################################

def main():

	testDataTransformation()
	#testClassroom()
	#testCourse()


if __name__ == "__main__":
	main()