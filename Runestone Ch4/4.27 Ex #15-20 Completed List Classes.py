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

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
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

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def pop(self):
        current = self.head
        previous = None
        while current.getNext() is not None:
            previous = current
            current = current.getNext()

        previous.setNext(None)
        return current.getData()

    def insert(self, pos, item):
        current = self.head
        i = 0
        while i != pos:
            current = current.getNext()
            i += 1
        tmp = Node(item)
        tmp.setNext(current.getNext())
        current.setNext(tmp)

    def append(self, item):
        current = self.head
        previous = None
        while current is not None:
            previous = current
            current = current.getNext()

        previous.setNext(Node(item))

    def index(self, item):
        current = self.head
        i = 0
        while current.getData() != item:
            current = current.getNext()
            i += 1
        return i

    def __str__(self):
        current = self.head
        s = '['
        while current.getNext() is not None:
            s += str(current.getData())
            s += ', '
            current = current.getNext()

        s += str(current.getData()) + ']'
        return s

    def __getitem__(self, key):
        if isinstance(key, slice):
            i = 0
            current = self.head
            while i < key.start:
                current = current.getNext()
                i += 1

            tmp = []

            while i < key.stop:
                tmp.append(current.getData())
                current = current.getNext()
                i += 1

            return tmp
        return []  # should never be reached


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def remove(self, item):
        current = self.head
        previous = None

        while current.getData() != item:
            previous = current
            current = current.getNext()

        previous.setNext(current.getNext())

    def index(self, item):
        current = self.head
        i = 0
        while current.getData() != item:
            current = current.getNext()
            i += 1
        return i

    def pop(self, pos=-1):
        current = self.head
        previous = None
        if pos == -1:
            while current.getNext() is not None:
                previous = current
                current = current.getNext()

            previous.setNext(None)

        else:
            i = 0
            while i < pos:
                previous = current
                current = current.getNext()

            previous.setNext(current.getNext())

    def __str__(self):
        current = self.head
        s = '['
        while current.getNext() is not None:
            s += str(current.getData())
            s += ', '
            current = current.getNext()

        s += str(current.getData()) + ']'
        return s


mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.add(100)
print(mylist[0:2])
