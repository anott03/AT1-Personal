from pythonds.basic import Queue
from random import randrange


def hotPotato(namelist, num):
	simqueue = Queue()
	for name in namelist:
		simqueue.enqueue(name)

	while simqueue.size() > 1:
		for i in range(randrange(0, simqueue.size())):
			simqueue.enqueue(simqueue.dequeue())

		simqueue.dequeue()

	return simqueue.dequeue()


print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
