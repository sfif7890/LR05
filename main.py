import random

while True:
    towers = int(input("Введите количество башен  от 3 до 10 "))
    if towers >= 3 and towers <= 10:
        break
while True:
    rings = int(input("Введите количество колец  от 3 до 20 "))
    if rings >= 3 and rings <= 20:
        break
while True:
    start = int(input("Введите начальную башню "))
    if start >= 1 and start <= towers:
        break
while True:
    end = int(input("Введите конечную башню "))
    if end >= 1 and end <= towers:
        break
pole = []
for i in range(towers):
    a = []
    pole.append(a)
    for j in range(rings):
        if i == (start - 1):
            pole[i].append(j+1)
        else:
            pole[i].append(0)

while True:
    t3 = random.randint(1,towers)
    if t3 != start and t3 != end:
        break
print("\033[38m{}".format("█"),"\033[0m{}".format("█"),"\033[39m{}".format("█"))

def kadr():
    for k in range(15):
        print("")
    for o in range(rings):
        stroka = " "
        for p in range(towers):
            kolco = ""
            color = pole[p][o]%9
            if color == 0:
                kolco = '\033[30m{}'.format("█")*pole[p][o] + '\033[38m{}'.format("█")+'\033[30m{}'.format("█")*pole[p][o]
            elif color == 1:
                kolco = '\033[31m{}'.format("█")*pole[p][o] + '\033[38m{}'.format("█")+'\033[31m{}'.format("█")*pole[p][o]
            elif color == 2:
                kolco = '\033[32m{}'.format("█")*pole[p][o] + '\033[38m{}'.format("█")+'\033[32m{}'.format("█")*pole[p][o]
            elif color == 3:
                kolco = '\033[33m{}'.format("█")*pole[p][o] + '\033[38m{}'.format("█")+'\033[33m{}'.format("█")*pole[p][o]
            elif color == 4:
                kolco = '\033[34m{}'.format("█")*pole[p][o] + '\033[38m{}'.format("█")+'\033[34m{}'.format("█")*pole[p][o]
            elif color == 5:
                kolco = '\033[35m{}'.format("█")*pole[p][o] + '\033[38m{}'.format("█")+'\033[35m{}'.format("█")*pole[p][o]
            elif color == 6:
                kolco = '\033[36m{}'.format("█")*pole[p][o] + '\033[38m{}'.format("█")+'\033[36m{}'.format("█")*pole[p][o]
            elif color == 7:
                kolco = '\033[37m{}'.format("█")*pole[p][o] + '\033[38m{}'.format("█")+'\033[37m{}'.format("█")*pole[p][o]
            elif color == 8:
                kolco = '\033[38m{}'.format("█")*pole[p][o] + '\033[38m{}'.format("█")+'\033[38m{}'.format("█")*pole[p][o]
            stroka = stroka + (rings - pole[p][o])* " " + kolco + " "*(rings - pole[p][o]) + " " * rings
        print(stroka)
kadr()