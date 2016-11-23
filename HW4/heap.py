import math
DEBUG=False

class Heap:
	def __init__(self):
		heap = [None]
	heap = [None]
	def __str__(self):
		outputString = ""
		for i in range(0,len(self.heap)):
			outputString += str(self.heap[i]) + "\n"
		return outputString
		

	def makenull(self):
		self.heap = [None]

	def insert(self,x):
		if self.heap[0] == None:
			self.heap[0] = x
			return
		self.heap.append(x)

	def parent(self,i):
		parentIndex = (i-1)/2
		return parentIndex
		if self.outofheap(parentIndex):
			return -1
		if(i>0):
			return self.heap[int(math.floor(parentIndex))]
			
	def left(self,i):
		leftIndex = ((i+1)*2)-1
		return leftIndex
		if self.outofheap(leftIndex):
			return -1
		return leftIndex

	def right(self,i):
		rightIndex = (i+1)*2
		return rightIndex
		if self.outofheap(rightIndex):
			return -1
		return rightIndex

	def swap(self,a,b):
		temp = self.heap[a]
		self.heap[a] = self.heap[b]
		self.heap[b] = temp

	def upheap(self,i):
		parentIndex = self.parent(i)
		if self.outofheap(i) or self.outofheap(parentIndex):
			return False
		if self.heap[i] < self.heap[parentIndex]:
			self.swap(i,parentIndex)
		return True
	def downheap(self,i):
		
		if self.outofheap(i) or self.outofheap(self.left(i)):
			return -1
#		if not(outofheap(self.left(i))):
		leftmiddlerighet = 0
		left = False
		right = False
		if self.heap[i] > self.heap[self.left(i)]:
			self.swap(i,self.left(i))
			left = True
		if not(self.outofheap(self.right(i))):
			if self.heap[i] > self.heap[self.right(i)]:
				self.swap(i,self.right(i))
				right = True

		if left:
			return self.left(i)
		elif right:
			return self.right(i)
		return -1
				
	def inorder(self,i):
		if self.outofheap(i):
			return -1
		
                if self.left(i) >= 0:
                        self.inorder(self.left(i))
		print(self.heap[i])

		if self.right(i) >= 0:
			self.inorder(self.right(i))

	def preorder(self,i):
		if self.outofheap(i):
                        return -1
		print(self.heap[i])
                if self.left(i) >= 0:
                        self.preorder(self.left(i))

                if self.right(i) >= 0:
                        self.preorder(self.right(i))

	def postorder(self,i):
		if self.outofheap(i):
                        return -1
                if self.left(i) >= 0:
                        self.postorder(self.left(i))

                if self.right(i) >= 0:
                        self.postorder(self.right(i))
		print(self.heap[i])
	def sort(self):
		maxIndex = self.downheap(0)
                print(maxIndex)
                while maxIndex != -1:
                        maxIndex = self.downheap(maxIndex)
                        print("deleteminasdasdas a")
                        print(self)
		heapIndex = len(self.heap) - 1
                while self.upheap(heapIndex):
                        heapIndex = self.parent(heapIndex)


	def min(self):
		return self.heap[0]

	def deletemin(self):
		self.sort()
		print(self.min())
		self.heap[0] = self.heap[len(self.heap)-1]
		self.heap.pop()
		self.sort()
		return len(self.heap)

	def outofheap(self,i):
		global DEBUG
		if i >= len(self.heap) or i < 0 or i is None:
			if DEBUG:
				print("node index not found in heap")
			return True
		return False
heaper = Heap()
heaper.insert(0)
heaper.insert(1)
heaper.insert(2)
heaper.insert(3)
heaper.insert(4)
heaper.insert(5)
heaper.insert(6)

print(heaper)
print("inorder")
heaper.inorder(0)
print("preorder")
heaper.preorder(0)
print("inorder")
heaper.inorder(0)
#print(str(heaper))
print(heaper.min())
print("delete min")
heaper.deletemin()
print("Print new min")
print(heaper.min())
print("all values")
print(heaper)
