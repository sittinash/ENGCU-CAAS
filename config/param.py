# FILE DIRECTORIES
courseFile = "dataset/test/courses.csv"
classroomFile = "dataset/test/classrooms.csv"
solutionFile = "solution.txt"

# COLUMN NO. IN COURSE FILE
courseNoCol = 0
courseCodeCol = 1
courseNameCol = 2
courseSectionCol = 3
courseDayCol = 4
courseStartTimeCol = 5
courseEndTimeCol = 6
courseTypeCol = 7
courseEnrollCol = 8

# COLUMN NO. IN CLASSROOM FILE
croomNoCol = 0
croomBuildingCol = 1
croomCodeCol = 2
croomCapacityCol = 3
croomTypeCol = 4

# SYNONYMS
LectureSynonym = ["LECTURE", "LEC", "PRACTICE", "PRAC"]
LabSynonym = ["LAB", "LABS"]

# DON'T TOUCH, BITCH !
dummyDate = "2009-01-01"
dayList = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']

"""
COURSE FILE FORMAT

CLASSROOM FILE FORMAT
	- The first column is always CLASSROOM_NO starting with 1.
	- The second column is always BUILDING which contains information of which building a classroom resides in. 
	- The third column is always CLASSROOM_CODE.
	- The forth column is always CAPACITY.
	- The fifth column is always TYPE.
	- The first 5 columns are mandatory as specified above. Another may contain optional attributes.
"""