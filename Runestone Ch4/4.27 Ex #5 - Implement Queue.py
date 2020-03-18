class Queue:
	def __init__(self):
		self.data = []

	def isEmpty(self):
		return self.data == []

	def enqueue(self, item):
		self.data.append(item)

	def dequeue(self):
		temp = self.data[0]
		del self.data[0]
		return temp

	def size(self):
		return len(self.data)
