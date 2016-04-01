import csv
import random

# PRIMARY FILE DIRECTORIES
sciPrimaryFile = "dataset/production/23S20152.txt"
engPrimaryFile = "dataset/production/21S20152.txt"
culiPrimaryFile = "dataset/production/55S20152.txt"

# SECONDARY FILE DIRECTORIES
sciSecondaryFile = "dataset/production/processed_23S20152.csv"
endSecondaryFile = "dataset/production/processed_21S20152.csv"
culiSecondaryFile = "dataset/production/processed_55S20152.csv"
secondaryFile = "dataset/production/processed_combinedSchedule.csv"

# FINAL FILE DIRECTORIES
courseFinalFile = "dataset/production/courses.csv"
classroomFinalFile = "dataset/production/classrooms.csv"

# COLUMN POINTER
primaryFileColumnDict = {'COURSE_CODE': 0, 'COURSE_NAME': 1, 'COURSE_SECTION': 8, 'COURSE_TYPE': 9, 'COURSE_DAY': 10, 'COURSE_TIME': 17, 'ROOM_BUILDING': 18, 'ROOM_CODE': 19, 'ENROLL': 24,}
secondaryFileColumnDict = {'COURSE_NO': 0, 'COURSE_CODE': 1, 'COURSE_NAME': 2, 'COURSE_SECTION': 3, 'COURSE_TYPE': 4, 'COURSE_DAY': 5, 'COURSE_STARTTIME': 6, 'COURSE_ENDTIME': 7, 'ROOM_BUILDING': 8, 'ROOM_CODE': 9, 'ENROLL': 10, 'CAPACITY': 11}
courseFinalFileColumnDict = {'COURSE_NO': 0, 'COURSE_CODE': 1, 'COURSE_NAME': 2, 'COURSE_SECTION': 3, 'COURSE_TYPE': 4, 'COURSE_DAY': 5, 'COURSE_STARTTIME': 6, 'COURSE_ENDTIME': 7, 'ENROLL': 8}
classroomFinalFileColumnDict = {'ROOM_NO': 0, 'ROOM_BUILDING': 1, 'ROOM_CODE': 2, 'ROOM_TYPE': 3, 'CAPACITY': 4}
'''
* Secondary file's columns must match exactly to solution file's columns.
* Changing global variable secondaryFileColumnDict may force functions;
	-> _essentialColumnList(listRow, no) 
to be changed too.
'''

# COLUMN VALUES
typeValueList = ('DISC', 'FWK', 'IDPS', 'L/L', 'L/P', 'LAB', 'LECT', 'PRAC', 'SMNA')
unwantedTypeValueList = ('LAB')
buildingValueList = ('CE', 'CELAB', 'CHE', 'CHEMT', 'EE', 'EN100', 'ENG1', 'ENG2', 'ENG3', 'ENG4', 'ENG5', 'ENV', 'HANS', 'HV', 'NT', 'SALAB', 'SVBLD')

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

		 	if ('AR' not in listRow) and ('IA' not in listRow) and ('AR-AR' not in listRow) and (listRow[primaryFileColumnDict['ROOM_BUILDING']] in buildingValueList):
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

	global courseFinalFile
	global classroomFinalFile

	global secondaryFileColumnDict
	global courseFinalFileColumnDict
	global classroomFinalFileColumnDict

	sortedCourseColumnList = sorted(list(courseFinalFileColumnDict), key = _valueToSortCourseFinalFileColumns)
	sortedCroomColumnList = sorted(list(classroomFinalFileColumnDict), key = _valueToSortClassroomFinalFileColumns)

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

def main():

	primaryPreprocess()
	secondaryPreprocess()
	finalPreprocess()


#########################################################

if __name__ == "__main__":
	main()

#########################################################
