import csv
import numpy as Numpie

from config import param as Param
from entities import *

##########################################################################

def periodDictionary(courseFile):

	with open(courseFile) as fh:
		reader = csv.reader(fh)
		courseList = list(reader)

	columnList = courseList[0]
	courseList.remove(courseList[0])

	smallestGap = _smallestGap(courseList)
	earliestStart, latestEnd = _earliestAndLatestTime(courseList)
	periodIndexDict = {}

	dayList = Param.dayList
	idx = 0

	for i in range(len(dayList)):
		start = earliestStart
		while start < latestEnd:
			end = start + smallestGap
			prd = Period(dayList[i], _stampStrFromTimestamp(start), _stampStrFromTimestamp(end))
			periodIndexDict[idx] = prd
			idx = idx + 1
			start = end

	#print smallestGap
	#print (_stampStrFromTimestamp(earliestStart), _stampStrFromTimestamp(latestEnd))

	return periodIndexDict


def _smallestGap(courseList):

	timestampList = []
	minDelta = Numpie.timedelta64(24, 'h')

	for item in courseList:
		timestampList.append(_timestampFromStampString(item[4]))
		timestampList.append(_timestampFromStampString(item[5]))

	for i in xrange(len(timestampList)-1):
		for j in xrange(i+1, len(timestampList)):
			if timestampList[i] > timestampList[j]:
				if timestampList[i] - timestampList[j] < minDelta:
					minDelta = timestampList[i] - timestampList[j]
			elif timestampList[i] < timestampList[j]:
				if timestampList[j] - timestampList[i] < minDelta:
					minDelta = timestampList[j] - timestampList[i]

	return minDelta


def _earliestAndLatestTime(courseList):

	startTimeList = []
	endTimeList = []
	minStartTime = _timestampFromStampString("23:59")
	maxEndTime = _timestampFromStampString("04:00")

	for item in courseList:
		startTime = _timestampFromStampString(item[4])
		endTime = _timestampFromStampString(item[5])
		if startTime < minStartTime:
			minStartTime = startTime
		if endTime > maxEndTime:
			maxEndTime = endTime

	return (minStartTime, maxEndTime)


def _timestampFromStampString(stampStr):

	if len(stampStr) < 5:
		stampStr = "0" + stampStr

	stampStr = Param.dummyDate + "T" + stampStr

	return Numpie.datetime64(stampStr)


def _stampStrFromTimestamp(timestamp):

	stampStr = str(timestamp)

	return stampStr[-10:-5]


##########################################################################

def classroomDictionary(classroomFile):
	
	with open(classroomFile) as fh:
		reader = csv.reader(fh)
		classroomList = list(reader)

	columnList = classroomList[0]
	classroomList.remove(classroomList[0])
	classroomCount = len(classroomList)
	classroomIndexDict = {}

	#for item in classroomList:
	#	print item
	#print columnList

	for i in xrange(classroomCount):
		listRoom = classroomList[i]
		room = Classroom(listRoom, columnList)
		#room.printClassroom()
		classroomIndexDict[i] = room

	return classroomIndexDict


def courseDictionary(courseFile):

	with open(courseFile) as fh:
		reader = csv.reader(fh)
		courseList = list(reader)

	columnList = courseList[0]
	courseList.remove(courseList[0])
	courseCount = len(courseList)
	courseIndexDict = {}

	#for item in courseList:
	#	print item
	#print columnList

	for i in xrange(courseCount):
		listCourse = courseList[i]
		course = Course(listCourse, columnList)
		courseIndexDict[i] = course

	return courseIndexDict


def capacityVector(classroomDict):

	# TEST VECTOR
	"""
	#capacityVectorList = [60, 60, 10, 40, 40, 120, 65, 90, 35, 100]
	capacityVectorList = [100, 200, 300, 90, 250]
	"""

	# DATASET
	#"""
	dictCapacityVector = {}

	for key, val in classroomDict.iteritems():
		dictCapacityVector[key] = val.capacity 

	return dictCapacityVector
	#"""


def schedulingMatrix(courseFile, periodFile):
	"""
	Row -> prd
	Col -> course
	"""

	listSchdulingMatrix = []

	# TEST MATRIX
	"""
	#1
	listSchdulingMatrix.append([1, 1, 1, 0, 0, 0, 0, 0, 0])
	listSchdulingMatrix.append([1, 1, 1, 0, 0, 0, 0, 0, 0])
	listSchdulingMatrix.append([1, 1, 0, 0, 0, 0, 0, 0, 0])
	listSchdulingMatrix.append([0, 0, 0, 1, 1, 1, 0, 0, 0])
	listSchdulingMatrix.append([0, 0, 0, 1, 1, 1, 0, 0, 0])
	#6
	listSchdulingMatrix.append([0, 0, 0, 1, 1, 1, 0, 0, 0])
	listSchdulingMatrix.append([0, 0, 0, 0, 0, 0, 1, 1, 1])
	listSchdulingMatrix.append([1, 1, 1, 0, 0, 0, 1, 1, 1])
	listSchdulingMatrix.append([0, 0, 1, 1, 1, 1, 1, 1, 0])
	listSchdulingMatrix.append([0, 0, 1, 1, 1, 1, 1, 1, 0])

	listSchdulingMatrix.append([1, 0, 1, 1])
	listSchdulingMatrix.append([0, 1, 1, 1])
	listSchdulingMatrix.append([0, 0, 1, 0])
	"""

	# DATASET
	#"""

	#"""

	return listSchdulingMatrix


def periodsCountVector(courseFile, timetableFilename):
	# Row -> periods count
	# Col -> course

	# TEST DATA
	"""periodsCountVectorList = [1, 1, 3, 2]

	#1
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	#6
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])"""

	periodsCountVectorList = [1, 1, 3, 2]

	return periodsCountVectorList


def assignmentAvailabilityMatrix(courseFile, classroomFile):
	# Row -> course
	# Col -> classroom

	# TEST DATA
	assignmentAvailabilityMatrixList = []

	"""#1						  1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20
	assignmentAvailabilityMatrixList.append([0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1])
	assignmentAvailabilityMatrixList.append([0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1])
	assignmentAvailabilityMatrixList.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	assignmentAvailabilityMatrixList.append([0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	assignmentAvailabilityMatrixList.append([0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	#6						  1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20
	assignmentAvailabilityMatrixList.append([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	assignmentAvailabilityMatrixList.append([0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1])
	assignmentAvailabilityMatrixList.append([0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1])
	assignmentAvailabilityMatrixList.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	assignmentAvailabilityMatrixList.append([0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1])"""

	assignmentAvailabilityMatrixList.append([1, 1, 1, 1, 1])
	assignmentAvailabilityMatrixList.append([0, 1, 1, 0, 1])
	assignmentAvailabilityMatrixList.append([0, 0, 1, 0, 1])
	assignmentAvailabilityMatrixList.append([0, 0, 1, 0, 1])

	return assignmentAvailabilityMatrixList