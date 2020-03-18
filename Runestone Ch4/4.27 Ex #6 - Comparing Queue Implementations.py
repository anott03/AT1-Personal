from random import randrange
import time


class Queue1:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)


class Queue2:
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
	
	
def testQ1Enqueue():
	for i in range(1000, 10001, 1000):
		q = Queue1()
		for j in range(i):
			q.enqueue(j)
		start = time.time()
		q.enqueue(randrange(0, i))
		end = time.time()
		print("size: " + str(i) + " time: " + str(end - start))


def testQ2Enqueue():
	for i in range(1000, 10001, 1000):
		q = Queue2()
		for j in range(i):
			q.enqueue(j)
		start = time.time()
		q.enqueue(randrange(0, i))
		end = time.time()
		print("size: " + str(i) + " time: " + str(end - start))


def testQ1Dequeue():
	for i in range(1000, 10001, 1000):
		q = Queue1()
		for j in range(i):
			q.enqueue(j)
		start = time.time()
		q.dequeue()
		end = time.time()
		print("size: " + str(i) + " time: " + str(end - start))


def testQ2Dequeue():
	for i in range(1000, 10001, 1000):
		q = Queue2()
		for j in range(i):
			q.enqueue(j)
		start = time.time()
		q.dequeue()
		end = time.time()
		print("size: " + str(i) + " time: " + str(end - start))


'''
outputs times for each Queue model (Queue1 and Queue2) and each function (enqueue and dequeue)
outputs for enqueue generally indicate that Q1 enqueue is O(n) and Q2 enqueue is O(1)
outputs for dequeue generally indicate that Q1 dequeue is O(1) and Q2 dequeue is O(n) 
'''
testQ1Enqueue()
print()
testQ2Enqueue()
print()
testQ1Dequeue()
print()
testQ2Dequeue()
