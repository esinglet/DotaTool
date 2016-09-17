
class ConvertError(Exception):
	def __init__(self):
		message = "Match -> Object conversion error"
	def __str__(self):
		return message