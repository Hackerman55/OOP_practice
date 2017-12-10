class circle_plane:
    def setr(self, r):    
        self._r = r
        if r < 0:
            self._r = -r
    
    def setx(self, x):
        self._x = x
    
    def sety(self, y):
        self._y = y
    
    def check(self,other):
        if self._r == other._r:
            self._q = "Площади равны!"
            return self._q
        else:
            self._q = "Площади не равны!"
            return self._q

    def getq(self):
        return self._q


    r = property(setr, 0)
    x = property(setx, 0)
    y = property(sety, 0)
    q = property(getq, 0)

a = circle_plane()
a._r = 12
a._x = 0
a._y = 0

b = circle_plane()
b._r = 11
b._x = 3
b._y = 5

a.check(b)
print(a._q)
