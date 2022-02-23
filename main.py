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
    for i in range(15):
        print("")
    for i in range(rings):
        stroka = '\033[{}m{}'.format(39," ")
        for j in range(towers):
            kolco = '\033[{}m{}'.format(39,"")
            color1 = pole[j][i]%8+30
            color2 = pole[j][i]//8+color1
            if color2>8:
                color1 = color1+1
                color2 = pole[j][i]//8+color1
            if pole[j][i]==15:
                color2 = 30
            for k in range(pole[j][i]*2+1):
                if k==pole[j][i]:
                    kolco = kolco+'\033[{}m{}'.format(39,"█")
                elif k%2==0:
                    kolco = kolco + '\033[{}m{}'.format(color1, "█")
                else:
                    kolco = kolco + '\033[{}m{}'.format(color2, "█")

            stroka = stroka + (rings - pole[j][i])* " " + kolco + " "*(rings - pole[j][i]) + " " * rings
        print(stroka)
kadr()