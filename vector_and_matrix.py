import csv
import numpy as Numpie

from config import param as Param
from entities import *

##########################################################################

class CapacityVector:

	def __init__(self, classroomPool):

		self.capacityDict, self.size = self._capacityDictWithSize(classroomPool)


	def _capacityDictWithSize(self, classroomPool): # SAM-KAN-MAK

		size = classroomPool.count
		capDict = {}

		for i in xrange(size):
			room = classroomPool.getClassroomByIndex(i)
			capDict[i] = room.capacity

		return (capDict, size)


	def printVector(self):

		for key, val in self.capacityDict.iteritems():
			print "Classroom: " + str(key) + ", Capacity: " + str(val)


	def getCapacityByClassroomIndex(self, index):

		return self.capacityDict[index]


##########################################################################

class PeriodCountVector:

	def __init__(self, coursePool):

		self.periodCountDict, self.size = self._periodCountDictWithSize(coursePool)


	def _periodCountDictWithSize(self, coursePool): # SAM-KAN-MAK

		size = coursePool.count
		countDict = {}

		for i in xrange(size):
			course = coursePool.getCourseByIndex(i)
			countDict[i] = self._periodCount(course.timetable)

		return (countDict, size)


	def _periodCount(self, listTimetable):

		count = 0

		for item in listTimetable:
			if item == 1:
				count = count + 1

		return count


	def printVector(self):

		for key, val in self.periodCountDict.iteritems():
			print "Course: " + str(key) + ", Period count: " + str(val)


	def getPeriodCountByCourseIndex(self, index):

		return self.periodCountDict[index]


##########################################################################

class SchedulingMatrix:
	# ROW -> Course
	# COL -> Period

	def __init__(self, coursePool):

		self.schedulingDict, self.m, self.n = self._schedulingDictWithSize(coursePool)


	def _schedulingDictWithSize(self, coursePool):

		m = coursePool.count
		n = -1
		schedulDict = {}

		for i in xrange(m):
			timetable = coursePool.getCourseByIndex(i).timetable
			schedulDict[i] = timetable
			if n == -1:
				n = len(timetable)

		return schedulDict, m, n


	def printMatrix(self):

		print "Period:       " + str(range(self.n)).strip('[]')

		for key, val in self.schedulingDict.iteritems():
			print "Course: " + str(key) + " => " + str(val)


	def getValueByIndexes(self, i, j):

		return self.schedulingDict[i][j]
		

##########################################################################

class AssignmentAvailabilityMatrix:

	def __init__(self, coursePool, classroomPool):

		self.assignmentAvailabilityDict, self.m, self.n = self._assignmentAvailabilityDict(coursePool, classroomPool)


	def _assignmentAvailabilityDict(self, coursePool, classroomPool):

		m = coursePool.count
		n = classroomPool.count
		aaDict = {}

		for i in xrange(m):
			courseType = coursePool.getCourseByIndex(i).type.lower()
			aaList = []
			for j in xrange(n):
				classroomType = classroomPool.getClassroomByIndex(j).type.lower()
				if courseType == classroomType:
					aaList.append(1)
				else:
					aaList.append(0)
			aaDict[i] = aaList[:]

		return (aaDict, m, n)


	def printMatrix(self):

		print "Classroom:    " + str(range(self.n)).strip('[]')

		for key, val in self.assignmentAvailabilityDict.iteritems():
			print "Course: " + str(key) + " => " + str(val)


	def getValueByIndexes(self, i, j):

		return self.assignmentAvailabilityDict[i][j]


##########################################################################

class SolutionMatrix:

	def __init__(self, t, m, n):

		self.solutionDict = {}
		self.t = t
		self.m = m
		self.n = n


	def printMatrix(self):

		for p in xrange(self.t):

			print "##############################"
			print "Period = " + str(p)
			print "Classroom:    " + str(range(self.n)).strip('[]')

			for i in xrange(self.m):
				tempList =[]
				for j in xrange(self.n):
					tempList.append(self.solutionDict[str(p)+"_"+str(i)+"_"+str(j)])
				print "Course: " + str(i) + " => " + str(tempList)

			print "##############################"


	def setValueAtIndexes(self, p, i, j, value):

		self.solutionDict[str(p)+"_"+str(i)+"_"+str(j)] = value


	def getValueByIndexes(self, p, i, j):

		return self.solutionDict[str(p)+"_"+str(i)+"_"+str(j)]

##########################################################################
