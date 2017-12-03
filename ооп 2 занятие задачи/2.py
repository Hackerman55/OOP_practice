class Stroka:
    def setx(self, value):
        self.__s = value
    
    def getx(self):
        return self.__s*3
    
    def delx(self):
        del self.__s
    
    s = property(getx, setx, delx, "Енто строка")

a = Stroka()
a.s = "1"
print(a.s)
del a.s