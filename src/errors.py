
class ConvertError(Exception):
	def __init__(self):
		self.message = "Match -> Object conversion error"
	def __str__(self):
		return repr(self.message)