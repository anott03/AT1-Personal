class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.back = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def getBack(self):
		return self.back

	def setData(self, data):
		self.data = data

	def setNext(self, newnext):
		self.next = newnext

	def setBack(self, previous):
		self.back = previous


class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.last = None
		self.length = 0

	def add(self, item):
		self.length += 1
		temp = Node(item)
		if self.head is None:
			self.head = temp
			self.head.setNext(None)
			self.last = self.head
			self.head.setBack(self.last)
		else:
			temp.setNext(self.head)
			temp.setBack(self.last)
			self.head.setBack(temp)
			self.head = temp

	def remove(self, item):
		current = self.head
		previous = None
		while current.getData() != item and current is not None:
			previous = current
			current = current.getNext()

		if current is None:
			raise RuntimeError("item not in list")

		if current == self.last:
			previous.setNext(None)
			self.head.setBack(previous)
			self.last = previous
		elif previous is None:
			current.getNext().setBack(self.last)
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
			current.getNext().setBack(previous)
		self.length -= 1

	def size(self):
		return self.length

	def index(self, item):
		pos = 0
		current = self.head
		while current is not None:
			if current.getData() == item:
				return pos
			else:
				current = current.getNext()
				pos += 1
		raise RuntimeError("item not in ist")

	def pop(self, pos=None):
		if pos is None:
			temp = self.last
			self.last.getBack().setNext(None)
			self.head.setBack(self.last.getBack())
			self.last = self.last.getBack()
			return temp.getData()
			self.length -= 1
		else:
			current = self.head
			previous = None
			if 0 < pos < self.length-1:
				for i in range(pos):
					previous = current
					current = current.getNext()
				previous.setNext(current.getNext())
				self.length -= 1
				current.getNext().setBack(previous)
				return current.getData()
			elif pos == 0:
				temp = self.head
				self.head.getNext().setBack(self.last)
				self.head = self.head.getNext()
				self.length -= 1
				return temp.getData()
			elif pos == self.length-1:
				return self.pop()
			else:
				raise RuntimeError("Position out of bounds!")

	def search(self, item):
		current = self.head
		while current is not None:
			if current.getData() == item:
				return True
			current = current.getNext()
		return False

	def isEmpty(self):
		return self.head is None

	def append(self, item):
		self.length += 1
		temp = Node(item)
		self.last.setNext(temp)
		temp.setBack(self.last)
		self.head.setBack(temp)
		self.last = temp

	def insert(self, pos, item):
		count = 0
		current = self.head
		while count < pos:
			current = current.getNext()
			count += 1
		temp = Node(item)
		temp.setBack(current)
		temp.setNext(current.getNext())
		if current.getNext() is not None:
			current.getNext().setBack(temp)
		else:
			self.last = temp


dll = DoublyLinkedList()
dll.add("hello")
dll.add(1)
dll.add(2)
dll.append("yo")
print(dll.size())
print(dll.pop(3))
