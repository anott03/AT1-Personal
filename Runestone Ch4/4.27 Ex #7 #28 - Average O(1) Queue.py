class Queue:
	def __init__(self):
		self.data = {}
		self.i = 0
		self.dqcount = 0

	def enqueue(self, item):
		# append is O(1)
		self.data[str(self.i)] = item
		self.i += 1

	def dequeue(self):
		temp = self.data[str(0)]
		del self.data[str(0)]
		self.dqcount += 1
		return temp

	def isEmpty(self):
		return self.data == []

	def size(self):
		return len(self.data)

	def queue(self):
		arr = []
		for i in range(len(self.data)):
			arr.append(self.data[str(i + self.dqcount)])
		return arr


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.queue())
q.dequeue()
print(q.queue())
