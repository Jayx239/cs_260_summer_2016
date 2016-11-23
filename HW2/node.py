
class node:
	def __init__(self,inValue):
		self.value = inValue	
	
	value = 0 
	nextNode = None

	def print_val(self):
		print(self.value);
	def get_val(self):
		return self.value

	def set_val(self,value):
		self.value = value

	def get_next(self):
		return self.nextNode

	def set_next(self,nextNode):
		self.nextNode = nextNode


	def empty(self):
		return self.nextNode is None
