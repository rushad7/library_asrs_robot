import math

n = 100
i= 0
coor = []

while True:
    x = i%n
    y = int(i/n)
    coor.append([x,y])
    i = i + 1

    if (i == n*n):
        break
