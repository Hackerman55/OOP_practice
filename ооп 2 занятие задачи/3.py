class circle_plane:
    def setr(self, r):    
        self.__r = r
        if r < 0:
            self.r = -r
    
    def setx(self, q):    
        self.__x = q
    
    def sety(self, y):
        self.__y = y
    
    def getr(self, other):
        if self.r == other.r:
            return "Площади равны!"
        else:
            return "Площади не равны!"

    r = property(getr, setr, 0)
    x = property(setx, 0)
    y = property(sety, 0)

a = circle_plane()
a.r = 12
a.x = 0
a.y = 0

b = circle_plane()
b.r = 11
b.x = 3
b.y = 5

print(a.r)
#ЧТО НУЖНО СДЕЛАТЬ В ЭТОЙ ЗАДАЧЕ???