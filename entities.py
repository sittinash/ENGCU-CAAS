import csv
import numpy as Numpie

import config.param as Param

##########################################################################

class Period:

	def __init__(self, day, startTime, endTime):

		self.day = day
		self.startTime = startTime
		self.endTime = endTime


	def printPeriod(self):

		print "###############################"
		print "Day: " + str(self.day)
		print "Time: " + self.startTime + " - " + self.endTime
		print "###############################"


	"""
	def isEqualTo(self, another):

		if self.day == another.day and self.startTime == another.startTime and self.endTime == another.endTime:
			return True

		return False
	"""


##########################################################################

class PeriodPool:

	def __init__(self, courseFile = Param.courseFile):

		self.periodDict = self._periodDict(courseFile)
		self.count = len(self.periodDict)


	def _periodDict(self, courseFile):

		with open(courseFile) as fh:
			reader = csv.reader(fh)
			courseList = list(reader)

		columnList = courseList[0]
		courseList.remove(courseList[0])

		smallestGap = self._smallestGap(courseList)
		earliestStart, latestEnd = self._earliestAndLatestTime(courseList)
		periodIndexDict = {}

		dayList = Param.dayList
		idx = 0

		for i in range(1):#len(dayList)):
			start = earliestStart
			while start < latestEnd:
				end = start + smallestGap
				prd = Period(dayList[i], self._stampStrFromTimestamp(start), self._stampStrFromTimestamp(end))
				periodIndexDict[idx] = prd
				idx = idx + 1
				start = end

		#print smallestGap
		#print (self._stampStrFromTimestamp(earliestStart), self._stampStrFromTimestamp(latestEnd))

		return periodIndexDict


	def _smallestGap(self, courseList):

		timestampList = []
		minDelta = Numpie.timedelta64(24, 'h')

		for item in courseList:
			timestampList.append(self._timestampFromStampString(item[Param.courseStartTimeCol]))
			timestampList.append(self._timestampFromStampString(item[Param.courseEndTimeCol]))

		for i in xrange(len(timestampList)-1):
			for j in xrange(i+1, len(timestampList)):
				if timestampList[i] > timestampList[j]:
					if timestampList[i] - timestampList[j] < minDelta:
						minDelta = timestampList[i] - timestampList[j]
				elif timestampList[i] < timestampList[j]:
					if timestampList[j] - timestampList[i] < minDelta:
						minDelta = timestampList[j] - timestampList[i]

		return minDelta


	def _earliestAndLatestTime(self, courseList):

		startTimeList = []
		endTimeList = []
		minStartTime = self._timestampFromStampString("23:59")
		maxEndTime = self._timestampFromStampString("04:00")

		for item in courseList:
			startTime = self._timestampFromStampString(item[Param.courseStartTimeCol])
			endTime = self._timestampFromStampString(item[Param.courseEndTimeCol])
			if startTime < minStartTime:
				minStartTime = startTime
			if endTime > maxEndTime:
				maxEndTime = endTime

		return (minStartTime, maxEndTime)


	def _timestampFromStampString(self, stampStr):

		if len(stampStr) < 5:
			stampStr = "0" + stampStr

		stampStr = Param.dummyDate + "T" + stampStr

		return Numpie.datetime64(stampStr)


	def _stampStrFromTimestamp(self, timestamp):

		stampStr = str(timestamp)

		return stampStr[-10:-5]


	def printPool(self):

		for key, val in self.periodDict.iteritems():
			print "Index => " + str(key)
			val.printPeriod()


	def getPeriodByIndex(self, index):

		return self.periodDict[index]

	"""
	def getIndexByPeriod(self, period):

		for key, val in self.periodDict.iteritems():
			if period.isEqualTo(val):
				return key

		return -1
	"""


	def toTimetable(self, day, startTime, endTime):

		if len(startTime) < 5:
			presentStart = "0" + startTime
		else: 
			presentStart = startTime

		if len(endTime) < 5:
			end = "0" + endTime
		else:
			end = endTime
		
		timetable = [0] * self.count

		for key, val in self.periodDict.iteritems():
			#print (day, startTime, endTime)
			#val.printPeriod()
			if val.day == day and val.startTime == presentStart:
				timetable[key] = 1
				presentStart = val.endTime
				if presentStart == end:
					return timetable

		return -1


##########################################################################

class Course:

	def __init__(self, listCourse, columnList, periodPool):

		self.no = int(listCourse[Param.courseNoCol])
		self.code = str(listCourse[Param.courseCodeCol])
		self.name = str(listCourse[Param.courseNameCol])
		self.section = int(listCourse[Param.courseSectionCol])
		self.timetable = periodPool.toTimetable(listCourse[Param.courseDayCol], listCourse[Param.courseStartTimeCol], listCourse[Param.courseEndTimeCol])
		self.type = str(listCourse[Param.courseTypeCol])
		self.enroll = int(listCourse[Param.courseEnrollCol])
		self.attributes = {}

		for i in range(Param.courseEnrollCol+1, len(listCourse)):
			attr = str(columnList[i])
			val = listCourse[i]
			self.attributes[attr] = val


	def printCourse(self):

		print "###############################"
		print "No.: " + str(self.no)
		print "Code: " + self.code
		print "Name: " + self.name
		print "Section: " + str(self.section)
		print "Tmetable: " 
		for i in range(len(self.timetable)):
			print str(i) + " -> " + str(self.timetable[i])
		print "Type: " + self.type
		print "Enroll: " + str(self.enroll)

		for key, val in self.attributes.iteritems():
			print key + ": " + str(val)

		print "###############################"
			

##########################################################################

class CoursePool:

	def __init__(self, periodPool, courseFile = Param.courseFile):

		self.courseDict = self._courseDict(courseFile, periodPool)
		self.count = len(self.courseDict)


	def _courseDict(self, courseFile, periodPool):

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
			course = Course(listCourse, columnList, periodPool)
			courseIndexDict[i] = course

		return courseIndexDict


	def printPool(self):

		for key, val in self.courseDict.iteritems():
			print "Index => " + str(key)
			val.printCourse()


	def getCourseByIndex(self, index):

		return self.courseDict[index]


##########################################################################

class Classroom:

	def __init__(self, listClassroom, columnList):

		self.no = int(listClassroom[Param.croomNoCol])
		self.building = str(listClassroom[Param.croomBuildingCol])
		self.code = str(listClassroom[Param.croomBuildingCol])
		self.capacity = int(listClassroom[Param.croomCapacityCol])
		self.type = str(listClassroom[Param.croomTypeCol])
		self.attributes = {}

		for i in range(Param.croomTypeCol+1, len(listClassroom)):
			attr = str(columnList[i])
			val = listClassroom[i]
			self.attributes[attr] = val


	def printClassroom(self):

		print "###############################"
		print "No.: " + str(self.no)
		print "Building: " + self.building
		print "Code: " + self.code
		print "Capacity: " + str(self.capacity)
		print "Type: " + self.type

		for key, val in self.attributes.iteritems():
			print key + ": " + str(val)

		print "###############################"


##########################################################################

class ClassroomPool():

	def __init__(self, classroomFile = Param.classroomFile):

		self.classroomDict = self._classroomDict(classroomFile)
		self.count = len(self.classroomDict)


	def _classroomDict(self, classroomFile):

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


	def printPool(self):

		for key, val in self.classroomDict.iteritems():
			print "Index => " + str(key)
			val.printClassroom()


	def getClassroomByIndex(self, index):

		return self.classroomDict[index]


##########################################################################
"""
class Day(Enum):

	MO = 1
	TU = 2
	WE = 3
	TH = 4
	FR = 5
	SA = 6
	SU = 7
"""