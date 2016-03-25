# FILE DIRECTORIES
courseFile = "dataset/test/courses.csv"
classroomFile = "dataset/test/classrooms.csv"

# SETTINGS
periodsCountPerDay = 9
earliestStartTime = "8:00"
latestEndTime = "12:30"

# DONT TOUCH !
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