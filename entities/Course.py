import timestamp.py

class Course:

	def __init__(self, courseNo, day, start, end, typ, enroll):
		self.courseNo = courseNo
		self.periodsList = _getPeriodsList(day, start, end)
		self.type = typ
		self.enroll = enroll

	def _getPeriodsList(day, start, end):

