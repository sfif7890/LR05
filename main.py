import random
import keyboard
import time

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
for i in range(towers):
    pole[i].append(0)
#print(pole)




while True:
    t3 = random.randint(1,towers)
    if t3 != start and t3 != end:
        break

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

def hod(position1,position2,colco):
    while True:
        if keyboard.is_pressed('enter'):
            time.sleep(0.1)
            break

    for i in range(towers):
        for j in range(rings):
            if pole[i][j] == colco:
                pole[i][j] = 0
                #print(i," ",j)
                break
    for i in range(rings+1):
        #print(position2 - 1, " ", i," ",rings)
        if (pole[position2-1][i]!=0) or (i == rings):
            pole[position2-1][i-1] = colco

            break


    kadr()
    #print(position1," ",position2, " ", colco)

for i in range(1,towers+1):
    #print(i,' ',towers-i)
    if (rings%2)==0:
        hod(i-1,i,1)
    else:
        hod(towers-i+2,towers-i+1,1)


def moves(n, x=1, y=3):
    if x == 1:
        position1 = start
    elif x == 2:
        position1 = t3
    else:
        position1 = end
    if y == 1:
        position2 = start
    elif y == 2:
        position2 = t3
    else:
        position2 = end
    if n == 1:
        hod(position1,position2,n)
    else:
        moves(n - 1, x, 6 - x - y)
        hod(position1, position2,n)
        moves(n - 1, 6 - x - y, y)

moves(rings)