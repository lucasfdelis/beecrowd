while True:
    try:
        a,b,c = input().split()
        a = int(a)
        b = int(b)
        if(b < a):
            t = a
            a = b
            b = t
        c = int(c)
        i = 0
        while(i < c):
            x,y = input().split()
            x = int(x)
            y = int(y)
            if(y < x):
             t = x
             x = y
             y = t
            if(int(x) > a or int(y)>b):
                print("Nao")
            else:
                print("Sim")
            i = i+1
    except EOFError:
        break
