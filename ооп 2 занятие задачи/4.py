class circle_plane:
    def __init__(self, r, x, y):
        self._r = r
        if r < 0:
            self._r = -r
        self._x = x
        self._y = y
    
    def check(self, other):
        if self._r == other._r:
            print("Площади равны!")
        else:
            print("Площади не равны!")

    def print_info(self):
        print(self._r, self._x, self._y)

a = circle_plane(11, 0, 0)
a.print_info()
b = circle_plane(11, 3, 5)
b.print_info()
a.check(b)
