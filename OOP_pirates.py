from random import randint

#класс пиратов
class Pirate:
    def __init__(self, name, load):
        self.name = name
        self.load = load
        if load > 60:
            self.load = 60
        self.gold = 0
        self.curse = 0
        self.box = 0
        self.empty = 0
        self.n = 0

#содержимое сундука
def search_content(n):
    if n == 0:
        return 0
    elif n == 1:
        gold = randint(15,100)
        return gold
    else:
        curse = randint(3,10)
        return curse

#класс монет
class Box:
    def __init__(self):
        self.weight = randint(4,10)
        self.content = search_content(randint(0,2))

p = []
p1 = Pirate("Jack", 50)
p.append(p1)
p2 = Pirate("Torrent", 50)
p.append(p2)
p3 = Pirate("White", 50)
p.append(p3)
p4 = Pirate("Black", 50)
p.append(p4)

weight = 0
new_weight = 0

namegold = ""
maxgold = 0

namecurse = ""
maxcurse = 0

min_empty = 100
nameempty = ""

for i in range(len(p)):
    #1
    while weight + new_weight < p[i].load:
        a = Box()
        p[i].box += 1
        weight += a.weight
        if a.content > 14:
            p[i].gold += a.content
            p[i].n += 1
        elif a.content < 11 and a.content != 0:
            p[i].curse += a.content
        else:
            p[i].empty += 1
        new_weight = a.weight
        #print("loool")
        del a

    weight = 0
    print("Имя пирата: ",p[i].name)
    print("Количество сундуков: ",p[i].box)
    print("Золото: ",p[i].gold)
    print("Дней болел: ",p[i].curse)
    print("Пустых сундуков: ",p[i].empty,"\n")

    #2
    if maxgold < p[i].gold:
        namegold = ""
        namegold += p[i].name
        namegold += " "
        maxgold = p[i].gold
    elif maxgold == p[i].gold:
        namegold += p[i].name
        namegold += " "

    #3
    if maxcurse < p[i].curse:
        namecurse = ""
        namecurse += p[i].name
        namecurse += " "
        maxcurse = p[i].curse
    elif maxcurse == p[i].curse:
        namecurse += p[i].name
        namecurse += " "

    #4
    if min_empty > p[i].empty:
        nameempty = ""
        nameempty += p[i].name
        nameempty += " "
        min_empty = p[i].empty
    elif min_empty == p[i].empty:
        nameempty += p[i].name
        nameempty += " "

print("Золотой(-ые) пират(-ы): ",namegold)
print("Золота: ",maxgold)
print("\nБольной(-ые) пират(-ы): ",namecurse)
print("Дней болел: ",maxcurse)
print("\nМеньше всего пустых сундуков у ",nameempty," ")
