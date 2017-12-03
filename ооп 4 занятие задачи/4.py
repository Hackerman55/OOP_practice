def my_decorator(func):
	def wrap():
		print('Yesterday')
		func()
		print('Tomorrow')
	return wrap
@my_decorator
def my_function():
	print('Today')
my_function()