from random import randint

def matrix(boo,size):
    if boo == True:
        diap = int(input("\nВведите диапазон: "))
        m = [[int(randint(10,diap)) for i in range(size)] for j in range(size)]
        return m
    else:
        m = [[int(input()) for i in range(size)] for j in range(size)]
        return m


class square_matrix:
    n = 0
    def __init__(self, size, boo):
        self.size = size
        self.boo = boo
        self.m = matrix(boo,size)
        self.s = 0
        square_matrix.n += 1


#2. Размер и кол-во матриц
    def get_inform(self):
        return self.size, square_matrix.n
    x = property(get_inform)


#3. Вывод таблицей
    def __str__(self):
        s = "Уникальная матрица:\n"
        for i in range(self.size):
            for j in range(self.size):
                s += str(self.m[i][j])+" "
                self.s += self.m[i][j]
            s += "\n"
        return s


#4. Главная диагональ
    def main_diagonal(self):
        d = 0
        for i in range(self.size):
            d += self.m[i][i]
        print("Главная диагональ: ", d)


#5. Транспонирование
    def transposition(self):
        new = [[0 for i in range(self.size)] for j in range(self.size)]
        print("Транспонирование:")
        for i in range(self.size):
            for j in range(self.size):
                new[i][j] = self.m[j][i]
                print(new[i][j], end=" ")
            print()


#5. Сравнение
    def __lt__(self, other):
        if self.s < other.s:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.s == other.s:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.s > other.s:
            return True
        else:
            return False


#6. Сложение матриц
    def __add__(self,other):
        if self.size == other.size:
            summa = [[self.m[i][j] + other.m[i][j] for i in range(self.size)] for j in range(self.size)]
            return summa
        else:
            print("Сложение невозможно!!!")

#первая матрица
a = square_matrix(5, True)
print(a.x)
print(a)
a.main_diagonal()

#вторая матрица
b = square_matrix(5, True)
print(b.x)
print(b)
b.main_diagonal()

#третья матрица
c = square_matrix(4, True)
print(c.x)
print(c)
c.transposition()

#четвертая матрица
d = square_matrix(4, True)
print(d.x)
print(d)
d.transposition()

#пятая матрица
lol = square_matrix(5, True)
print(lol.x)
print(lol)
lol.main_diagonal()
lol.transposition()

#сравнение матриц
print("\nA больше B? ",a > b)
print("A меньше B? ",a < b)
print("A равно B? ",a == b)

#матрица сложения
mas = square_matrix(5, True)
mas.m = a + b
print(mas)

#наибольшая из трёх последних матриц
if d.s > c.s and d.s > lol.s:
    print("d - наибольшая матрица из трёх последних")
elif  c.s > d.s and c.s > lol.s:
    print("c - наибольшая матрица из трёх последних")
else: 
    print("lol - наибольшая матрица из трёх последних")

