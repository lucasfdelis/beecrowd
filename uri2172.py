while True:
    a,b = input().split()
    if(a==b=='0'):
        break
    else:
        a = int(a)
        b = int(b)
        print(a*b)
