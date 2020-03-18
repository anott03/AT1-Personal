class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, data):
		self.data = data

	def setNext(self, new_next):
		self.next = new_next


class OrderedList:
	def __init__(self):
		self.head = None
		self.last = None
		self.size = 0

	def size(self):
		return self.size

	def add(self, item):
		temp = Node(item)
		if self.head is None:
			self.head = temp
			self.last = self.head
		else:
			temp.setNext(self.head)
			self.head = temp
		self.size += 1

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		# iterating through elements of the list
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		if found and previous is None:  # if the item is the head
			self.head = current.getNext()
			self.size -= 1
		elif found:
			previous.setNext(current.getNext())
			self.size -= 1
		else:
			raise RuntimeError("Item not in list!")

	def search(self, item):
		current = self.head
		found = False
		while current is not None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found

	def pop(self, pos=None):
		# if no position is passed in
		if pos is None:
			current = self.head
			previous = None
			while not current == self.last:
				previous = current
				current = current.getNext()

			if self.last == self.head:  # to deal with the situation in which the head is the only element in the list
				temp = self.head
				self.head = None
				return temp
			else:
				temp = self.last
				self.last = previous
				self.last.setNext(None)
				return temp
		# if a position is passed in
		else:
			current = self.head
			for i in range(pos-1):
				current = current.getNext()
			temp = current.getNext()
			current.setNext(temp.getNext())
			return temp

	def isEmpty(self):
		return self.head is None

	def index(self, item):
		pos = 0
		current = self.head
		found = False
		# iterates through the elements of the list
		# if there is more than one occurrence of an element,
		# the index of the first occurrence is returned
		while current is not None and not found:
			if current.getData() == item:
				found = True
			current = current.getNext()
			pos += 1
		return pos

	def __str__(self):
		current = self.head
		final_string = "["
		# iterating through the elements of the list
		while current is not None:
			final_string += str(current.getData()) + ", "
			current = current.getNext()
		# to get rid of the ", " that follows the last element and to add the closing "]"
		final_string = final_string[:len(final_string)-2] + "]"
		return final_string


class UnorderedList (OrderedList):
	def __init__(self):
		super(OrderedList)
		super().__init__()

	def insert(self, pos, item):
		current = self.head
		# iterating through elements of the list
		if pos == 0:
			temp = self.head
			self.head = Node(item)
			self.head.setNext(temp)
		else:
			count = 0
			while count < pos:
				current = current.getNext()
				count += 1
			temp = Node(item)
			temp.setNext(current.getNext())
			current.setNext(temp)

	def append(self, item):
		temp = Node(item)
		self.last.setNext(temp)
		self.last = temp


ol = OrderedList()
ol.add(1)
ol.add(2)
ol.add("hello")
print(ol)

ul = UnorderedList()
ul.add(1)
ul.add(2)
ul.add("hello")
ul.append("last element")
print(ul)
