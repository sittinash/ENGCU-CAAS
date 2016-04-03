import csv
import numpy as Numpie

import config.param as Param
import gateway as Gate

##########################################################################

class Period:

	def __init__(self, periodRow):

		self.no = int(periodRow[Param.periodNoCol])
		self.day = str(periodRow[Param.periodDayCol])
		self.startTime = str(periodRow[Param.periodStartTimeCol])
		self.endTime = str(periodRow[Param.periodEndTimeCol])


	def printPeriod(self):

		print "###############################"
		print "No.: " + str(self.no)
		print "Day: " + str(self.day)
		print "Time: " + self.startTime + " - " + self.endTime
		print "###############################"


##########################################################################

class Course:

	def __init__(self, listCourse):

		self.no = int(listCourse[Param.courseNoCol])
		self.code = str(listCourse[Param.courseCodeCol])
		self.name = str(listCourse[Param.courseNameCol])
		self.section = int(listCourse[Param.courseSectionCol])
		self.type = str(listCourse[Param.courseTypeCol])
		self.day = str(listCourse[Param.courseDayCol])
		self.startTime = str(listCourse[Param.courseStartTimeCol])
		self.endTime = str(listCourse[Param.courseEndTimeCol])
		#self.timetable = periodPool.toTimetable(listCourse[Param.courseDayCol], listCourse[Param.courseStartTimeCol], listCourse[Param.courseEndTimeCol])
		self.enroll = int(listCourse[Param.courseEnrollCol])


	def printCourse(self):

		print "###############################"
		print "No.: " + str(self.no)
		print "Code: " + self.code
		print "Name: " + self.name
		print "Section: " + str(self.section)
		print "Type: " + self.type
		print "Day: " + self.day
		print "Time: " + self.startTime + " - " + self.endTime
		#print "Tmetable: " 
		#for i in range(len(self.timetable)):
		#	print str(i) + " -> " + str(self.timetable[i])
		print "Enroll: " + str(self.enroll)
		print "###############################"
			

##########################################################################

class Classroom:

	def __init__(self, listClassroom):

		self.no = int(listClassroom[Param.croomNoCol])
		self.building = str(listClassroom[Param.croomBuildingCol])
		self.code = str(listClassroom[Param.croomCodeCol])
		self.capacity = int(listClassroom[Param.croomCapacityCol])
		self.type = str(listClassroom[Param.croomTypeCol])


	def printClassroom(self):

		print "###############################"
		print "No.: " + str(self.no)
		print "Building: " + self.building
		print "Code: " + self.code
		print "Capacity: " + str(self.capacity)
		print "Type: " + self.type
		print "###############################"


##########################################################################

class SolutionMatrix:

	def __init__(self, t, m, n, objectiveValue, solutionStatus):

		self.solutionDict = {}
		self.t = t
		self.m = m
		self.n = n
		self.objectiveValue = objectiveValue
		self.solutionStatus = solutionStatus


	def setValueAtIndexes(self, p, i, j, value):

		self.solutionDict[str(p)+"_"+str(i)+"_"+str(j)] = value


	def getValueByIndexes(self, p, i, j):

		return self.solutionDict[str(p)+"_"+str(i)+"_"+str(j)]


	def printMatrix(self):

		for p in xrange(self.t):

			print "##############################"
			print "PERIOD = " + str(p)
			print "Classroom:    " + str(range(self.n)).strip('[]')

			for i in xrange(self.m):
				tempList =[]
				for j in xrange(self.n):
					tempList.append(self.solutionDict[str(p)+"_"+str(i)+"_"+str(j)])
				print "Course: " + str(i) + " => " + str(tempList)

			print "##############################"


	def getClassroomByCourseIndex(self, index, classroomPool):

		for j in xrange(self.n):
			for p in xrange(self.t):
				if self.solutionDict[str(p)+"_"+str(index)+"_"+str(j)] == 1:
					return classroomPool.getClassroomByIndex(j)


	def exportSolutionLogFile(self, fly = Param.solutionLogFile):

		with open(fly, 'w') as fh:

			fh.write("Problem Size: " + str(self.t) + ", " + str(self.m) + ", " + str(self.n) + "\n")
			fh.write("Objective Value: " + str(self.objectiveValue) + "\n")
			fh.write("Solution Status: " + str(self.solutionStatus))


	def exportSolutionMatrixFiles(self):

			for p in xrange(self.t):
				self._exportSolutionMatrixFile(p)


	def _exportSolutionMatrixFile(self, index):

		with open(Param.getSolutionMatrixFile(index), 'w') as fh:

			writer = csv.writer(fh)

			for i in xrange(self.m):
				listTempRow = []
				for j in xrange(self.n):
					listTempRow.append(self.solutionDict[str(index)+"_"+str(i)+"_"+str(j)])
				writer.writerow(listTempRow)

	
	def exportAssignmentTableFile(self):

		with open(Param.assignmentTableFile, 'w') as fh:

			writer = csv.writer(fh)
			writer.writerow(Param.assignmentTableColumnNameList)

			for i in xrange(self.m):
				course = Gate.getCourse(i)
				room = self._getMatchedClassroom(i)
				tempList = []

				for item in Param.assignmentTableColumnNameList:

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
						tempList.append(room.building)
					elif item == 'ROOM_CODE':
						tempList.append(room.code)
					elif item == 'ENROLL':
						tempList.append(course.enroll)
					elif item == 'CAPACITY':
						tempList.append(room.capacity)
					else:
						tempList.append('N/a')

				writer.writerow(tempList)


	def _getMatchedClassroom(self, i):

		for p in xrange(self.t):

			if Gate.schedulingMatrixGetValue(i, p) == 0:
				continue

			for j in xrange(self.n):
				if self.getValueByIndexes(p, i, j) == 1:
					return Gate.getClassroom(j)

		return -1
	

##########################################################################
