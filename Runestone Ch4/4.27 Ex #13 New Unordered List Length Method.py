from pythonds.basic import *


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


class UnorderedList:
	def __init__(self):
		self.head = None
		self.length = 0
		self.last = None

	def isEmpty(self):
		return self.head is None

	def add(self, item):
		if self.last is None:
			self.last = Node(item)
		else:
			self.last = self.head
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
		self.length += 1

	def size(self):
		current = self.head
		count = 0
		while current is not None:
			count = count + 1
			current = current.getNext()

		return count

	def search(self, item):
		current = self.head
		found = False
		while current is not None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if found and previous is None:
			self.head = current.getNext()
			self.length -= 1
		else:
			previous.setNext(current.getNext())

	def length(self):
		return self.length

	def append(self, item):
		temp = Node(item)
		self.last.setNext(temp)
		self.last = temp
		self.length += 1

	def pop(self):
		temp = self.last
		current = self.head
		previous = None
		self.length -= 1
		while current != self.last:
			previous = current
			current = current.getNext()
		previous.setNext(None)
		return temp


myList = UnorderedList()
