import csv

#########################################################

def fetchDatasetAsList(fileLocation):

	datasetList = []

	with open(fileLocation,'rb') as fh:
		reader = csv.reader(fh)
		for row in reader:
			datasetList.append(row)

		datasetList.pop(0)

	fh.close()

	return datasetList


def getCapacityVector(classroomsList):

	capacityVector = []

	for room in classroomsList:
		capacityVector.append(int(room[3]))

	return capacityVector


def getScheduleMatrix(periodsList, coursesList):

	scheduleMatrix = []

	for course in coursesList:
		day = course[3]
		start = course[4]
		end = course[5]

	return None

def getAssignmentAvailMatrix(coursesList, classroomsList):

	#for course in coursesList:
	#	for room in classroomsList:

	return None

#def _timeTokens():


#########################################################

def main():

	periodsList = fetchDatasetAsList('dataset_verify/periods.csv')
	for item in periodsList:
		print item

	#print len(periodsList)

	coursesList = fetchDatasetAsList('dataset_verify/courses.csv')
	for item in coursesList:
		print item

	#print len(coursesList)

	classroomsList = fetchDatasetAsList('dataset_verify/classrooms.csv')
	for item in classroomsList:
		print item

	#print len(classroomsList)

	capacityVector = getCapacityVector(classroomsList)

	i = 0
	for item in capacityVector:
		print (i, item)
		i += 1


#########################################################

if __name__ == "__main__":
	main()