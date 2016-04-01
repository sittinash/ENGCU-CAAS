# FILE DIRECTORIES
courseFile = "dataset/production/courses.csv"
classroomFile = "dataset/production/classrooms.csv"
solutionDotTxtFile = "output/solution.txt"
solutionDotCSVFile = "output/solution.csv"

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

# COLUMN VALUES
courseTypeValueList = ('DISC', 'FWK', 'IDPS', 'L/L', 'L/P', 'LAB', 'LECT', 'PRAC', 'SMNA')

# SOLUTION FILE COLUMNS
solutionFileColumnNameList = ('COURSE_NO', 'COURSE_CODE', 'COURSE_NAME', 'COURSE_SECTION', 'COURSE_TYPE', 'COURSE_DAY', 'COURSE_STARTTIME', 'ROOM_BUILDING', 'ROOM_CODE', 'ENROLL', 'CAPACITY')
'''
* Changing global variable solutionFileColumnNameList forces functions;
	-> exportSolutionDotCSV(self, coursePool, classroomPool, solutionFile)
to be changed too.
'''

# DON'T TOUCH, BITCH !
dummyDate = "2009-01-01"
dayList = ('MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU')