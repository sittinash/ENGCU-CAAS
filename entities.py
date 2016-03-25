import config.param as Param

##########################################################################

class Classroom:

	def __init__(self, listClassroom, columnList):

		self.no = int(listClassroom[0])
		self.building = str(listClassroom[1])
		self.code = str(listClassroom[2])
		self.capacity = int(listClassroom[3])
		self.type = str(listClassroom[4])
		self.attributes = {}

		for i in range(5, len(listClassroom)):
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

class Course:

	def __init__(self, listCourse, columnList):

		self.no = int(listCourse[0])
		self.code = str(listCourse[1])
		self.name = str(listCourse[2])
		self.timetable = self._timetable(listCourse[3:6])
		self.type = str(listCourse[6])
		self.enroll = int(listCourse[7])
		self.attributes = {}

		for i in range(8, len(listCourse)):
			attr = str(columnList[i])
			val = listCourse[i]
			self.attributes[attr] = val


	def _timetable(self, listDayTime):

		day = listDayTime[0]
		time = listDayTime[1:3]

		return ""


	def printCourse(self):

		print "###############################"
		print "No.: " + str(self.no)
		print "Code: " + self.code
		print "Name: " + self.name
		print "Tmetable: " + self.timetable
		print "Type: " + self.type
		print "Enroll: " + str(self.enroll)

		for key, val in self.attributes.iteritems():
			print key + ": " + str(val)

		print "###############################"