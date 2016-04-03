import csv

from config import param as Param
from entities import *

##########################################################################

def getPeriod(p):

	with open(Param.periodFile) as fh:
		reader = csv.reader(fh)
		listPeriod = list(reader)[1:]

	return Period(listPeriod[p])


def getCourse(i):

	with open(Param.courseFile) as fh:
		reader = csv.reader(fh)
		listCourse = list(reader)[1:]

	return Course(listCourse[i])


def getClassroom(j):

	with open(Param.classroomFile) as fh:
		reader = csv.reader(fh)
		listRoom = list(reader)[1:]

	return Classroom(listRoom[j])


##########################################################################

def capacityVectorGetValue(j):

	print "CAPACITY VECTOR: get value at index  " + str(j)

	with open(Param.capacityVectorFile) as fh:
		reader = csv.reader(fh)
		return int(list(reader)[j][0])


def periodCountVectorGetValue(i):

	print "PERIOD COUNT VECTOR: get value at index " + str(i)

	with open(Param.periodCountVectorFile) as fh:
		reader = csv.reader(fh)
		return int(list(reader)[i][0])


def schedulingMatrixGetValue(i, p):

	print "SCHEDULING MATRIX: get value at index (" + str(i) + ", " + str(p) + ")"

	with open(Param.schedulingMatrixFile) as fh:
		reader = csv.reader(fh)
		return int(list(reader)[i][p])


def aaMatrixGetValue(i, j):

	print "AA MATRIX: get value at index (" + str(i) + ", " + str(j) + ")"

	with open(Param.aaMatrixFile) as fh:
		reader = csv.reader(fh)
		return int(list(reader)[i][j])


def getPeriodCount():

	with open(Param.schedulingMatrixFile) as fh:
		reader = csv.reader(fh)
		return len(list(reader)[0])


def getCourseCount():

	with open(Param.periodCountVectorFile) as fh:
		reader = csv.reader(fh)
		return len(list(reader))


def getClassroomCount():

	with open(Param.capacityVectorFile) as fh:
		reader = csv.reader(fh)
		return len(list(reader))


##########################################################################
