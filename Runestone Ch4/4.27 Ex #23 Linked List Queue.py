class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext


class Queue:
	def __init__(self):
		self.head = None
		self.last = None
		self.size = 0

	def enqueue(self, item):
		if self.head is None:
			self.head = Node(item)
			self.last = self.head
		else:
			temp = Node(item)
			self.last.setNext(temp)
			self.last = temp
		self.size += 1

	def dequeue(self, item):
		temp = self.head
		self.head = self.head.getNext()
		self.size -= 1
		return temp

	def isEmpty(self):
		return self.head is None

	def size(self):
		return self.size
