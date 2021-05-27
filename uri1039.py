while True:
    try:
        r1,x1,y1,r2,x2,y2 = input().split()
        r1 = int(r1)
        x1 = int(x1)
        y1 = int(y1)
        r2 = int(r2)
        x2 = int(x2)
        y2 = int(y2)
        temp = 0
        distancia = (((x1)-(x2))**2)+(((y1)-(y2))**2)
        distancia = (distancia)**0.5
        if(r1 >= (distancia)+r2):
            print('RICO')
        else:
            print('MORTO')
    except EOFError:
        break
