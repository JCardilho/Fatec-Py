colidiuX = colidiuY = False

entrada1= str(input())
entrada2 = str(input())

x01, y01, x11, y11 = map(int, entrada1.split(" "))
x02, y02, x12, y12 = map(int, entrada2.split(" "))

if (x01 < x11) and (x02 < x12) and (y01 < y11) and (y02 < y12):
    for i in range(x01,x11+1):
        if (x02 == i):
            colidiuX = True

    if (colidiuX == True):
        for i in range(y01,y11+1):
            if (y02 == i):
                colidiuY= True

    if (colidiuX == True) and (colidiuY == True):
        print(1)
    else:
        print(0)
