import math
from Queue import Queue


def radix(n):
	# a Queue for each digit (0-9)
	bins = [Queue() for _ in range(10)]
	# the length of the longest number
	max_digits = int(math.ceil(math.log(max(n), 10)))

	for k in range(max_digits):
		for num in n:
			# 10 ** k --> 10, 100, 1000...
			digit = num / 10 ** k % 10  # find digit's value
			bins[int(digit)].enqueue(num)

		# resetting n for the next iteration of k
		n = []
		for b in bins:
			# loop to dequeue all values
			while not b.isEmpty():
				n.append(b.dequeue())
	# returns the sorted array
	return n


print(radix([4, 1, 2, 4, 5, 1, 3, 240]))
