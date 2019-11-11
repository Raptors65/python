class Pointer:
	def __init__(self, value):
		self.container = value
		self._value = value[0]
	
	@property
	def value(self):
		return self._value
	
	@value.setter
	def value(self, value):
		self.container[0] = value
		self._value = value
