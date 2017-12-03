class circle_plane:
    def __init__(self, r, x, y):
        self.r = r
        if r < 0:
            self.r = -r
        self.x = x
        self.y = y
    
    def check(self, other):
        if self.r == other.r:
            print("Площади равны!")
        else:
            print("Площади не равны!")

    def print_info(self):
        print(self.r, self.x, self.y)

a = circle_plane(11, 0, 0)
#a.print_info()
b = circle_plane(11, 3, 5)
a.check(b)
