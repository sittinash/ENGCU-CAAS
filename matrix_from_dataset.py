def capacityVector(classroomFilename):

	#capacityVectorList = [60, 60, 10, 40, 40, 120, 65, 90, 35, 100]
	capacityVectorList = [100, 200, 300, 90, 250]

	return capacityVectorList


def schedulingMatrix(coursesFilename, timetableFilename):

	schedulingMatrixList = []

	"""#1
	schedulingMatrixList.append([1, 1, 1, 0, 0, 0, 0, 0, 0])
	schedulingMatrixList.append([1, 1, 1, 0, 0, 0, 0, 0, 0])
	schedulingMatrixList.append([1, 1, 0, 0, 0, 0, 0, 0, 0])
	schedulingMatrixList.append([0, 0, 0, 1, 1, 1, 0, 0, 0])
	schedulingMatrixList.append([0, 0, 0, 1, 1, 1, 0, 0, 0])
	#6
	schedulingMatrixList.append([0, 0, 0, 1, 1, 1, 0, 0, 0])
	schedulingMatrixList.append([0, 0, 0, 0, 0, 0, 1, 1, 1])
	schedulingMatrixList.append([1, 1, 1, 0, 0, 0, 1, 1, 1])
	schedulingMatrixList.append([0, 0, 1, 1, 1, 1, 1, 1, 0])
	schedulingMatrixList.append([0, 0, 1, 1, 1, 1, 1, 1, 0])"""

	schedulingMatrixList.append([1, 0, 1, 1])
	schedulingMatrixList.append([0, 1, 1, 1])
	schedulingMatrixList.append([0, 0, 1, 0])

	return schedulingMatrixList

	#ประเภทห้อง
	#ห้องที่สลับกัน ความเหมาะสม?


def periodsCountVector(coursesFilename, timetableFilename):

	"""periodsCountVectorList = [1, 1, 3, 2]

	#1
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	#6
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])
	periodsCountVectorList.append([3, 3, 2, 3, 3, 3, 3, 6, 6, 6])"""

	periodsCountVectorList = [1, 1, 3, 2]

	return periodsCountVectorList


def assignmentAvailabilityMatrix(coursesFilename, classroomFilename):

	assignmentAvailabilityMatrixList = []

	"""#1						  1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20
	assignmentAvailabilityMatrixList.append([0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1])
	assignmentAvailabilityMatrixList.append([0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1])
	assignmentAvailabilityMatrixList.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	assignmentAvailabilityMatrixList.append([0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	assignmentAvailabilityMatrixList.append([0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	#6						  1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20
	assignmentAvailabilityMatrixList.append([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	assignmentAvailabilityMatrixList.append([0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1])
	assignmentAvailabilityMatrixList.append([0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1])
	assignmentAvailabilityMatrixList.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	assignmentAvailabilityMatrixList.append([0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1])"""

	assignmentAvailabilityMatrixList.append([1, 1, 1, 1, 1])
	assignmentAvailabilityMatrixList.append([0, 1, 1, 0, 1])
	assignmentAvailabilityMatrixList.append([0, 0, 1, 0, 1])
	assignmentAvailabilityMatrixList.append([0, 0, 1, 0, 1])

	return assignmentAvailabilityMatrixList


