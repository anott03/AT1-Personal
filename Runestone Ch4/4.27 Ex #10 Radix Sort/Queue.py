class Queue:
	def __init__(self):
		self.data = {}
		self.i = 0

	def enqueue(self, item):
		# append is O(1)
		self.data[str(self.i)] = item
		self.i += 1

	def dequeue(self):
		temp = self.data["0"]
		del self.data["0"]
		return temp

	def isEmpty(self):
		return self.data == []

	def size(self):
		return len(self.data)
