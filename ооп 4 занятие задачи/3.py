class MyQueue:
	def __init__(self):
		self.items = []
	def enqueue(self, item):
		self.items.insert(0, item)
	def dequeue(self):
		return self.items.pop()
	def size(self):
		return len(self.items)
	def isEmpty(self):
		if len(self.items) != 0:
			return True
		else:
			return False
a = MyQueue()
print(a.isEmpty())
a.enqueue(19)
a.enqueue(20)
a.enqueue(21)
print(a.size())
a.dequeue()
print(a.size())
print(a.isEmpty())