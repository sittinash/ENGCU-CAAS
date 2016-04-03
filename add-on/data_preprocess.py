import sys
import time
import csv
import random
import numpy as Numpie

# PRIMARY FILE DIRECTORIES

sciPrimaryFile = "dataset/production/primary/23S20152.txt"
engPrimaryFile = "dataset/production/primary/21S20152.txt"
culiPrimaryFile = "dataset/production/primary/55S20152.txt"

# SECONDARY FILE DIRECTORIES

sciSecondaryFile = "dataset/production/secondary/processed_23S20152.csv"
endSecondaryFile = "dataset/production/secondary/processed_21S20152.csv"
culiSecondaryFile = "dataset/production/secondary/processed_55S20152.csv"
secondaryFile = "dataset/production/secondary/processed_combinedSchedule.csv"
"""
secondaryFile = "dataset/test1/secondary/processed_combinedSchedule.csv"
"""

# FINAL FILE DIRECTORIES

periodFinalFile = "dataset/production/final/periods.csv"
courseFinalFile = "dataset/production/final/courses.csv"
classroomFinalFile = "dataset/production/final/classrooms.csv"
"""
periodFinalFile = "dataset/test1/final/periods.csv"
courseFinalFile = "dataset/test1/final/courses.csv"
classroomFinalFile = "dataset/test1/final/classrooms.csv"
"""

# VECTOR AND MATRICES FILE DIRECTORIES

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

# COLUMN POINTER
primaryFileColumnDict = {'COURSE_CODE': 0, 'COURSE_NAME': 1, 'COURSE_SECTION': 8, 'COURSE_TYPE': 9, 'COURSE_DAY': 10, 'COURSE_TIME': 17, 'ROOM_BUILDING': 18, 'ROOM_CODE': 19, 'ENROLL': 24,}
secondaryFileColumnDict = {'COURSE_NO': 0, 'COURSE_CODE': 1, 'COURSE_NAME': 2, 'COURSE_SECTION': 3, 'COURSE_TYPE': 4, 'COURSE_DAY': 5, 'COURSE_STARTTIME': 6, 'COURSE_ENDTIME': 7, 'ROOM_BUILDING': 8, 'ROOM_CODE': 9, 'ENROLL': 10, 'CAPACITY': 11}
periodFinalFileColumnDict = {'PERIOD_NO': 0, 'COURSE_DAY': 1, 'COURSE_STARTTIME': 2, 'COURSE_ENDTIME': 3}
courseFinalFileColumnDict = {'COURSE_NO': 0, 'COURSE_CODE': 1, 'COURSE_NAME': 2, 'COURSE_SECTION': 3, 'COURSE_TYPE': 4, 'COURSE_DAY': 5, 'COURSE_STARTTIME': 6, 'COURSE_ENDTIME': 7, 'ENROLL': 8}
classroomFinalFileColumnDict = {'ROOM_NO': 0, 'ROOM_BUILDING': 1, 'ROOM_CODE': 2, 'ROOM_TYPE': 3, 'CAPACITY': 4}
'''
* Secondary file's columns must match exactly to solution file's columns.
* Changing global variable secondaryFileColumnDict may force functions;
	-> _essentialColumnList(listRow, no) 
to be changed too.
'''

# COLUMN VALUES
typeValueList = ('DISC', 'FWK', 'IDPS', 'L/L', 'L/P', 'LECT', 'PRAC', 'SMNA') #'LAB'
buildingValueList = ('CE', 'CELAB', 'CHE', 'CHEMT', 'EE', 'EN100', 'ENG1', 'ENG2', 'ENG3', 'ENG4', 'ENG5', 'ENV', 'HANS', 'HV', 'NT', 'SALAB', 'SVBLD')

# DON'T TOUCH, BITCH !
dummyDate = "2009-01-01"

#########################################################

def primaryPreprocess():

	global sciPrimaryFile
	global engPrimaryFile
	global culiSheduleDotTxtFile

	global sciSecondaryFile
	global endSecondaryFile
	global culiSheduleDotCSVFile

	csvFileFromTxtFile(sciPrimaryFile, sciSecondaryFile)
	csvFileFromTxtFile(engPrimaryFile, endSecondaryFile)
	csvFileFromTxtFile(culiPrimaryFile, culiSecondaryFile)


def csvFileFromTxtFile(txtFile, csvFile):

	global primaryFileColumnDict
	global secondaryFileColumnDict
	global buildingValueList

	with open(txtFile, 'r') as inFile, open (csvFile, 'w') as outFile:

		 text = inFile.readlines()
		 writer = csv.writer(outFile)

		 writer.writerow(sorted(list(secondaryFileColumnDict), key = _valueToSortSecondaryFileColumns))

		 counter = 0

		 for line in text:

		 	listRow = line.split('\t')
		 	listRow = map(lambda x: x.strip(), listRow)
		 	#if listRow[1] == 'WORK PROC DES IPV':
		 	#	print listRow

		 	if ('AR' not in listRow) and ('IA' not in listRow) and ('AR-AR' not in listRow) and (listRow[primaryFileColumnDict['ROOM_BUILDING']] in buildingValueList) and (listRow[primaryFileColumnDict['COURSE_TYPE']] not in typeValueList):
				counter = counter + 1
				listRow = _essentialColumnList(listRow, counter)
				writer.writerow(listRow)


def _valueToSortSecondaryFileColumns(key):

	global secondaryFileColumnDict

	return secondaryFileColumnDict[key]


def _essentialColumnList(listRow, no):

	global primaryFileColumnDict
	global secondaryFileColumnDict
	newListRow = []

	for key in sorted(list(secondaryFileColumnDict), key = _valueToSortSecondaryFileColumns):

		if key == 'COURSE_NO':
			newListRow.append(no)
		elif key == 'COURSE_STARTTIME':
			newListRow.append(_startTime(listRow[primaryFileColumnDict['COURSE_TIME']]))
		elif key == 'COURSE_ENDTIME':
			newListRow.append(_endTime(listRow[primaryFileColumnDict['COURSE_TIME']]))
		elif key == 'CAPACITY':
			enroll = listRow[primaryFileColumnDict['ENROLL']]
			cap = _randomizedCapacity(enroll)
			newListRow.append(cap)
		else:
			newListRow.append(listRow[primaryFileColumnDict[key]])

	return newListRow


def _startTime(timeStr):

	startTime, endTime = timeStr.split('-')

	if len(startTime) < 4:
		startTime = '0' + startTime[0] + ':' + startTime[1:]
	else:
		startTime = startTime[:2] + ':' + startTime[2:]

	return startTime


def _endTime(timeStr):

	startTime, endTime = timeStr.split('-')

	if len(endTime) < 4:
		endTime = '0' + endTime[0] + ':' + endTime[1:]
	else:
		endTime = endTime[:2] + ':' + endTime[2:]

	return endTime


def _randomizedCapacity(enroll):

	lowerBound = int(enroll)/5
	if lowerBound < 1:
		lowerBound += 1

	upperBound = (int(enroll) * 2)/5
	if upperBound < 2:
		upperBound += 1

	return random.randint(lowerBound, upperBound) * 5


#########################################################

def secondaryPreprocess():

	global sciSecondaryFile
	global endSecondaryFile
	global culiSecondaryFile

	global secondaryFile

	global secondaryFileColumnDict

	counter = 0

	with open(secondaryFile, 'w') as outFile:

		writer = csv.writer(outFile)
		writer.writerow(sorted(list(secondaryFileColumnDict), key = _valueToSortSecondaryFileColumns))

		for fly in (endSecondaryFile, sciSecondaryFile, culiSecondaryFile):
			with open(fly) as inFile:
				reader = csv.reader(inFile)
				for row in reader:
					if row[0] not in secondaryFileColumnDict.keys():
						counter = counter + 1
						row[secondaryFileColumnDict['COURSE_NO']] = counter
						writer.writerow(row)


#########################################################

def finalPreprocess():

	global secondaryFile

	global periodFinalFile
	global courseFinalFile
	global classroomFinalFile

	global secondaryFileColumnDict

	global periodFinalFileColumnDict
	global courseFinalFileColumnDict
	global classroomFinalFileColumnDict

	sortedCourseColumnList = sorted(list(courseFinalFileColumnDict), key = _valueToSortCourseFinalFileColumns)
	sortedCroomColumnList = sorted(list(classroomFinalFileColumnDict), key = _valueToSortClassroomFinalFileColumns)

	# EXPORT COURSE FILE AND CLASSROOM FILE 
	with open(secondaryFile) as inFile, open(courseFinalFile, 'w') as outCourseFile, open(classroomFinalFile, 'w') as outCroomFile:

		reader = csv.reader(inFile)
		courseWriter = csv.writer(outCourseFile)
		croomWriter = csv.writer(outCroomFile)

		courseWriter.writerow(sortedCourseColumnList)
		croomWriter.writerow(sortedCroomColumnList)

		croomCount = 0
		croomBuffer = []

		for row in reader:

			if row[0] not in secondaryFileColumnDict.keys():
				
				courseRowList = []
				croomRowList = []

				for col in sortedCourseColumnList:
					courseRowList.append(row[secondaryFileColumnDict[col]])

				courseWriter.writerow(courseRowList)

				if (row[secondaryFileColumnDict['ROOM_BUILDING']], row[secondaryFileColumnDict['ROOM_CODE']]) not in croomBuffer:
					
					croomBuffer.append((row[secondaryFileColumnDict['ROOM_BUILDING']], row[secondaryFileColumnDict['ROOM_CODE']]))
					croomCount += 1
					#print croomCount

					for col in sortedCroomColumnList:
						if col == 'ROOM_NO':
							croomRowList.append(croomCount)
						elif col == 'ROOM_TYPE':
							croomRowList.append('LECT')
						else:
							croomRowList.append(row[secondaryFileColumnDict[col]])

					croomWriter.writerow(croomRowList)


	# EXPORT PERIOD FILE
	with open(courseFinalFile) as inFile, open(periodFinalFile, 'w') as outFile:

		reader = csv.reader(inFile)
		writer = csv.writer(outFile)

		courseList = list(reader)
		columnList = courseList[0]
		courseList.remove(courseList[0])

		minGap = _minGap(courseList)

		sortedPeriodColumnList = sorted(list(periodFinalFileColumnDict), key = _valueToSortPeriodFinalFileColumns)
		writer.writerow(sortedPeriodColumnList)

		periodCount = 0
		periodList = []

		for course in courseList:
			
			day = course[courseFinalFileColumnDict['COURSE_DAY']]
			startTime = course[courseFinalFileColumnDict['COURSE_STARTTIME']]
			endTime = course[courseFinalFileColumnDict['COURSE_ENDTIME']]

			periodList = periodList + _periodListFromStartAndEnd(periodList, day, startTime, endTime, minGap)
			#periodList = list(set(periodList))

			#print course
			#print len(periodList)
			#print "#############################"

		for period in periodList:

			periodRowList = []
			periodCount += 1

			for col in sortedPeriodColumnList:
				if col == 'PERIOD_NO':
					periodRowList.append(periodCount)
				#elif col == 'COURSE_STARTTIME' or col == 'COURSE_ENDTIME':
				#	periodRowList.append(period[periodFinalFileColumnDict[col]-1])
				else:
					periodRowList.append(period[periodFinalFileColumnDict[col]-1])

			writer.writerow(periodRowList)


def _periodListFromStartAndEnd(periodList, day, startTime, endTime, minGap):

	startStamp = _timestampFromStampString(startTime)
	endStamp = _timestampFromStampString(endTime)

	tempList = []

	while startStamp < endStamp:

		#print (day, startStamp, endStamp)
		#print startStamp + minGap
		#print (startStamp < endStamp)

		period = (day, _stampStrFromTimestamp(startStamp), _stampStrFromTimestamp(startStamp + minGap))

		if period not in periodList:

			#if period == ('FR', '09:00', '09:30'):
			#	print period not in periodList

			tempList.append(period)

		startStamp = startStamp + minGap

	#print "######################"

	return tempList


def _minGap(courseList):

		global courseFinalFileColumnDict

		timestampList = []
		minDelta = Numpie.timedelta64(24, 'h')

		for item in courseList:
			#print item
			#print item[Param.courseStartTimeCol]
			timestampList.append(_timestampFromStampString(item[courseFinalFileColumnDict['COURSE_STARTTIME']]))
			timestampList.append(_timestampFromStampString(item[courseFinalFileColumnDict['COURSE_ENDTIME']]))

		for i in xrange(len(timestampList)-1):
			for j in xrange(i+1, len(timestampList)):
				if timestampList[i] > timestampList[j]:
					if timestampList[i] - timestampList[j] < minDelta:
						minDelta = timestampList[i] - timestampList[j]
				elif timestampList[i] < timestampList[j]:
					if timestampList[j] - timestampList[i] < minDelta:
						minDelta = timestampList[j] - timestampList[i]

		return minDelta


def _timestampFromStampString(stampStr):

		if len(stampStr) < 5:
			stampStr = "0" + stampStr

		global dummyDate

		stampStr = dummyDate + "T" + stampStr

		return Numpie.datetime64(stampStr)


def _stampStrFromTimestamp(timestamp):

	stampStr = str(timestamp)

	return stampStr[-10:-5]


def _valueToSortPeriodFinalFileColumns(key):

	global periodFinalFileColumnDict

	return periodFinalFileColumnDict[key]


def _valueToSortCourseFinalFileColumns(key):

	global courseFinalFileColumnDict

	return courseFinalFileColumnDict[key]


def _valueToSortClassroomFinalFileColumns(key):

	global classroomFinalFileColumnDict

	return classroomFinalFileColumnDict[key]

"""
def _column(table, columnName):

	global classroomFinalFileColumnDict
	col = []

	for row in table:
		col.append(row[classroomFinalFileColumnDict[columnName]])

	return col
"""

#########################################################

def vamPreprocess():

	_exportCapacityVector()
	_exportPeriodCountVector()
	_exportSchedulingMatrix()
	_exportAssignmentAvailabilityMatrix()


def _exportCapacityVector():

	global classroomFinalFile
	global capacityVectorFile

	global classroomFinalFileColumnDict

	with open(classroomFinalFile) as inFile, open(capacityVectorFile, 'w') as outFile:

		reader = csv.reader(inFile)
		listTable = list(reader)
		writer = csv.writer(outFile)

		for i in xrange(1, len(listTable)):
			row = listTable[i]
			cap = row[classroomFinalFileColumnDict['CAPACITY']]
			writer.writerow([cap])


def _exportPeriodCountVector():

	global courseFinalFile
	global periodCountVectorFile
	
	global courseFinalFileColumnDict

	with open(courseFinalFile) as fh:

		courseReader = csv.reader(fh)
		listCourseTable = list(courseReader)
		listCourseTable = listCourseTable[1:]

	minGap = _minGap(listCourseTable)

	with open(periodCountVectorFile, 'w') as fh:

		writer = csv.writer(fh)

		for row in listCourseTable:

			counter = 0

			startTime = row[courseFinalFileColumnDict['COURSE_STARTTIME']]
			endTime = row[courseFinalFileColumnDict['COURSE_ENDTIME']]
			startStamp = _timestampFromStampString(startTime)
			endStamp = _timestampFromStampString(endTime)

			while startStamp < endStamp:
				counter += 1
				startStamp = startStamp + minGap

			writer.writerow([counter])


def _exportSchedulingMatrix():

	global periodFinalFile
	global courseFinalFile
	global schedulingMatrixFile
	
	global periodFinalFileColumnDict
	global courseFinalFileColumnDict

	with open(periodFinalFile) as fh:

		periodReader = csv.reader(fh)
		listPeriodTable = list(periodReader)
		listPeriodTable = listPeriodTable[1:]

	with open(courseFinalFile) as fh:

		courseReader = csv.reader(fh)
		listCourseTable = list(courseReader)
		listCourseTable = listCourseTable[1:]

	with open(schedulingMatrixFile, 'w') as fh:

		writer = csv.writer(fh)

		for cRow in listCourseTable:

			listTempRow = []

			cDay = cRow[courseFinalFileColumnDict['COURSE_DAY']]
			cStartTime = cRow[courseFinalFileColumnDict['COURSE_STARTTIME']]
			cEndTime = cRow[courseFinalFileColumnDict['COURSE_ENDTIME']]
			cStartStamp = _timestampFromStampString(cStartTime)
			cEndStamp = _timestampFromStampString(cEndTime)

			for pRow in listPeriodTable:

				pDay = pRow[periodFinalFileColumnDict['COURSE_DAY']]
				pStartTime = pRow[periodFinalFileColumnDict['COURSE_STARTTIME']]
				pEndTime = pRow[periodFinalFileColumnDict['COURSE_ENDTIME']]
				pStartStamp = _timestampFromStampString(pStartTime)
				pEndStamp = _timestampFromStampString(pEndTime)

				if (cDay == pDay) and (cStartStamp <= pStartStamp) and (cEndStamp >= pEndStamp):
					listTempRow.append(1)
				else:
					listTempRow.append(0)

			writer.writerow(listTempRow)


def _exportAssignmentAvailabilityMatrix():

	global courseFinalFile
	global classroomFinalFile
	global aaMatrixFile

	global courseFinalFileColumnDict
	global classroomFinalFileColumnDict

	with open(courseFinalFile) as fh:

		courseReader = csv.reader(fh)
		listCourseTable = list(courseReader)
		listCourseTable = listCourseTable[1:]

	with open(classroomFinalFile) as fh:

		roomReader = csv.reader(fh)
		listRoomTable = list(roomReader)
		listRoomTable = listRoomTable[1:]

	with open(aaMatrixFile, 'w') as fh:

		writer = csv.writer(fh)

		for cRow in listCourseTable:

			listTempRow = []
			cEnroll = int(cRow[courseFinalFileColumnDict['ENROLL']])

			for rRow in listRoomTable:

				rCap = int(rRow[classroomFinalFileColumnDict['CAPACITY']])

				if (cEnroll <= rCap):
					listTempRow.append(1)
				else:
					listTempRow.append(0)

			writer.writerow(listTempRow)


#########################################################

def main():

	if len(sys.argv) > 1:

		if sys.argv[1][0] == '1':
			print "  " + time.asctime( time.localtime(time.time()) ) + " >>>> PRIMARY PROCESSING"
			primaryPreprocess()

		if sys.argv[1][1] == '1':
			print "  " + time.asctime( time.localtime(time.time()) ) + " >>>> SECONDARY PROCESSING"
			secondaryPreprocess()

		if sys.argv[1][2] == '1':
			print "  " + time.asctime( time.localtime(time.time()) ) + " >>>> FINAL PROCESSING"
			finalPreprocess()

		if sys.argv[1][3] == '1':
			print "  " + time.asctime( time.localtime(time.time()) ) + " >>>> VECTOR AND MATRIX PROCESSING"
			vamPreprocess()

	print "  " + time.asctime( time.localtime(time.time()) ) + " >>>> FINISH PREPROCESSING"


#########################################################

if __name__ == "__main__":
	main()

#########################################################
