def print_name(name):
		return name

class Dog(object):
	n = 0
	def __init__(self, name):
		self.name = "Alex"
		self.method = print_name(self.name)
		Dog.n += 1

corgi = Dog("Charlie")
dalmatian = Dog("Jack")
print(corgi.method)
print(dalmatian.method)
print(Dog.n)