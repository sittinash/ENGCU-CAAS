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

	def __init__(self, coursePool, periodPool):

		self.periodCountDict, self.size = self._periodCountDictWithSize(coursePool, periodPool)


	def _periodCountDictWithSize(self, coursePool, periodPool): # SAM-KAN-MAK

		size = coursePool.count
		countDict = {}

		for i in xrange(size):
			course = coursePool.getCourseByIndex(i)
			countDict[i] = self._periodCount(course.timetable(periodPool))

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

	def __init__(self, coursePool, periodPool):

		self.schedulingDict, self.m, self.n = self._schedulingDictWithSize(coursePool, periodPool)


	def _schedulingDictWithSize(self, coursePool, periodPool):

		m = coursePool.count
		n = -1
		schedulDict = {}

		for i in xrange(m):
			timetable = coursePool.getCourseByIndex(i).timetable(periodPool)
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
			course = coursePool.getCourseByIndex(i)
			courseType = course.type.lower()
			courseEnroll = course.enroll
			aaList = []
			for j in xrange(n):
				croom = classroomPool.getClassroomByIndex(j)
				croomType = croom.type.lower()
				croomCap = croom.capacity
				if course.enroll <= croom.capacity: #and courseType == croomType:
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

	def __init__(self, t, m, n, objectiveValue, solutionStatus):

		self.solutionDict = {}
		self.t = t
		self.m = m
		self.n = n
		self.objectiveValue = objectiveValue
		self.solutionStatus = solutionStatus


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


	def getClassroomByCourseIndex(self, index, classroomPool):

		for j in xrange(self.n):
			for p in xrange(self.t):
				if self.solutionDict[str(p)+"_"+str(index)+"_"+str(j)] == 1:
					return classroomPool.getClassroomByIndex(j)


	def exportSolutionDotTxt(self, option, solutionFile = Param.solutionDotTxtFile):

		with open(solutionFile, 'w') as fh:

			if option > 0:

				for p in xrange(self.t):

					fh.write("Period = " + str(p) + "\n")
					print "Period = " + str(p)

					fh.write("Classroom:    " + str(range(self.n)).strip('[]') + "\n")
					print "Classroom:    " + str(range(self.n)).strip('[]')

					for i in xrange(self.m):
						tempList =[]
						for j in xrange(self.n):
							tempList.append(self.solutionDict[str(p)+"_"+str(i)+"_"+str(j)])
						fh.write("Course: " + str(i) + " => " + str(tempList) + "\n")
						print "Course: " + str(i) + " => " + str(tempList)
						if i == self.m-1:
							fh.write("#########################################################################" + "\n")
							print "#########################################################################"

				fh.write("Objective value: " + self.objectiveValue + "\n")
				print "Objective value: " + self.objectiveValue

				fh.write("Solution status: " + self.solutionStatus)
				print "Solution status: " + self.solutionStatus

			else:

				for p in xrange(self.t):
					
					fh.write("Period = " + str(p) + "\n")
					fh.write("Classroom:    " + str(range(self.n)).strip('[]') + "\n")

					for i in xrange(self.m):
						tempList =[]
						for j in xrange(self.n):
							tempList.append(self.solutionDict[str(p)+"_"+str(i)+"_"+str(j)])
						fh.write("Course: " + str(i) + " => " + str(tempList) + "\n")
						if i == self.m-1:
							fh.write("#########################################################################" + "\n")

				fh.write("Objective value: " + self.objectiveValue + "\n")
				fh.write("Solution status: " + self.solutionStatus)


	def exportSolutionDotCSV(self, coursePool, classroomPool, solutionFile = Param.solutionDotCSVFile):

		with open(Param.solutionDotCSVFile, 'w') as fh:

			writer = csv.writer(fh)
			writer.writerow(Param.solutionFileColumnNameList)

			for i in xrange(coursePool.count):
				course = coursePool.getCourseByIndex(i)
				croom = self.getClassroomByCourseIndex(i, classroomPool)
				tempList = []

				for item in Param.solutionFileColumnNameList:

					if item == 'COURSE_NO':
						tempList.append(course.no)
					elif item == 'COURSE_CODE':
						tempList.append(course.code)
					elif item == 'COURSE_NAME':
						tempList.append(course.name)
					elif item == 'COURSE_SECTION':
						tempList.append(course.section)
					elif item == 'COURSE_TYPE':
						tempList.append(course.type)
					elif item == 'COURSE_DAY':
						tempList.append(course.day)
					elif item == 'COURSE_STARTTIME':
						tempList.append(course.startTime)
					elif item == 'COURSE_ENDTIME':
						tempList.append(course.endTime)
					elif item == 'ROOM_BUILDING':
						tempList.append(croom.building)
					elif item == 'ROOM_CODE':
						tempList.append(croom.code)
					elif item == 'ENROLL':
						tempList.append(course.enroll)
					elif item == 'CAPACITY':
						tempList.append(croom.capacity)
					else:
						tempList.append('N/a')

				writer.writerow(tempList)


##########################################################################
