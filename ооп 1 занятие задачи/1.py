class Dog(object):
	def __init__(self, name):
		self.name = name
	def print_name(self):
		print(self.name)	

corgi = Dog("Charlie")
corgi.print_name()


class Little_child:
    def __init__(self, noise):
        self.noise = noise
    
    def print_noise(self):
        print(self.noise)

kid = Little_child(10)
kid.print_noise()
