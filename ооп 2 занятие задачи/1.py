class Dog:
    name = "Alex"
    _color = "ginger"
    __age = 2

corgi = Dog()
print(corgi.name)
print(corgi._color)
print(corgi._Dog__age)
