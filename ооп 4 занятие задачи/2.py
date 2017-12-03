class Point:
	count = 0
	def __init__(self, x, y):
		self.x = x
		self.y = y
		Point.count += 1
	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)
	@staticmethod
	def print_count():
		return Point.count
	@classmethod
	def print_object(cls, a, b):
		return cls(a, b)

firstpoint = Point(2, 1)
secondpoint = Point(2, 4)
result = firstpoint + secondpoint
print(result.x)
print(result.y)
print(Point.print_count())
thirdpoint = Point.print_object(5, 6)
print(thirdpoint.x)
print(thirdpoint.y)