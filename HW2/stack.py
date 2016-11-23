import node
if __name__ == '__main__':
        import stack_test
 
class stack:
	def __init__(self):
		currentNode = None #node
	currentNode = None	

	def top(self):
		return self.currentNode;

	def pop(self):
		poppedNode = self.currentNode;
		self.currentNode = self.currentNode.get_next()
		return poppedNode

	def push(self, node):
		if self.currentNode == None:
			self.currentNode = node
			#self.set_next(None)
		else:
			node.set_next(self.currentNode)
			self.currentNode = node;

	def empty(self):
		if self.currentNode is None:
			return True
		return False

	def print_stack(self):
		topNode = self.currentNode
		stack_trace = "{"
		while(not(self.currentNode is None)):
			stack_trace+= "[" + str(self.currentNode.get_val()) + "]"
			self.currentNode = self.currentNode.get_next()
		stack_trace += "}"
		print(stack_trace)
		self.currentNode = topNode
