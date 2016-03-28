import csv
import numpy as Numpie

from config import param as Param
from entities import *

##########################################################################

class CapacityVector:

	def __init__(self, classroomPool):

		self.capacityDict, self.size = self._capacityDictWithSize(classroomPool)


	def _capacityDictWithSize(self, classroomPool):

		size = classroomPool.count
		capDict = {}

		for i in range(size):
			room = classroomPool.getClassroomByIndex(i)
			capDict[i] = room.capacity

		return (capDict, size)


	def printCapacityVector(self):

		for key, val in self.capacityDict.iteritems():
			print "Classroom: " + str(key) + ", Capacity: " + str(val)


	def getCapacityByIndex(self, index):

		
		

"""
def capacityVector(classroomDict):

	# TEST VECTOR
	"""
	#capacityVectorList = [60, 60, 10, 40, 40, 120, 65, 90, 35, 100]
	capacityVectorList = [100, 200, 300, 90, 250]
	"""

	# DATASET
	"""
	dictCapacityVector = {}

	for key, val in classroomDict.iteritems():
		dictCapacityVector[key] = val.capacity 

	return dictCapacityVector
	"""
"""


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


def assignmentAvailabilityMatrix(courseFile, classroomPool):
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