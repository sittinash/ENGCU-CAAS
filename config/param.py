# FILE DIRECTORIES

periodFile = "dataset/production/final/periods.csv"
courseFile = "dataset/production/final/courses.csv"
classroomFile = "dataset/production/final/classrooms.csv"
"""
periodFile = "dataset/test1/final/periods.csv"
courseFile = "dataset/test1/final/courses.csv"
classroomFile = "dataset/test1/final/classrooms.csv"
"""


capacityVectorFile = "dataset/production/vam/capacityVector.csv"
periodCountVectorFile = "dataset/production/vam/periodCountVector.csv"
schedulingMatrixFile = "dataset/production/vam/schedulingMatrix.csv"
aaMatrixFile = "dataset/production/vam/assignmentAvailabilityMatrix.csv"
"""
capacityVectorFile = "dataset/test1/vam/capacityVector.csv"
periodCountVectorFile = "dataset/test1/vam/periodCountVector.csv"
schedulingMatrixFile = "dataset/test1/vam/schedulingMatrix.csv"
aaMatrixFile = "dataset/test1/vam/assignmentAvailabilityMatrix.csv"
"""


solutionLogFile = "output/production/solutionLog.txt"
solutionMatrixDirectory = "output/production/solutionMatrix/"
assignmentTableFile = "output/production/assignmentTable.csv"
"""
solutionLogFile = "output/test1/solutionLog.txt"
solutionMatrixDirectory = "output/test1/"
assignmentTableFile = "output/test1/assignmentTable.csv"
"""


def getSolutionMatrixFile(index):

	global solutionMatrixDirectory

	return solutionMatrixDirectory + "solutionMatrixOfPeriod_" + str(index) + ".csv"


# PERIOD COLUMN POINTERS
periodNoCol = 0
periodDayCol = 1
periodStartTimeCol = 2
periodEndTimeCol = 3

# COURSE COLUMN POINTERS
courseNoCol = 0
courseCodeCol = 1
courseNameCol = 2
courseSectionCol = 3
courseTypeCol = 4
courseDayCol = 5
courseStartTimeCol = 6
courseEndTimeCol = 7
courseEnrollCol = 8

# CLASSROOM COLUMN POINTERS
croomNoCol = 0
croomBuildingCol = 1
croomCodeCol = 2
croomTypeCol = 3
croomCapacityCol = 4

# ASSIGNMENT TABLE COLUMN POINTERS
assignmentTableColumnNameList = ('COURSE_NO', 'COURSE_CODE', 'COURSE_NAME', 'COURSE_SECTION', 'COURSE_TYPE', 'COURSE_DAY', 'COURSE_STARTTIME', 'COURSE_ENDTIME', 'ROOM_BUILDING', 'ROOM_CODE', 'ENROLL', 'CAPACITY')
'''
* Changing global variable solutionFileColumnNameList forces functions;
	-> exportSolutionDotCSV(self, coursePool, classroomPool, solutionFile)
to be changed too.
'''

# DON'T TOUCH, BITCH !
dummyDate = "2009-01-01"
dayList = ('MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU')