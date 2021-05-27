while True:
    try:
        a,b=input().split()
        a = int(a)
        b = int(b)
        i = 0
        lista = []
        while(i < a):
            lista.append(int(input()))
            i = i+1
        lista = sorted(lista)
        lista = lista[::-1]
        i = 0
        c = 0
        while(i < b):
            c = int(input())
            print(lista[c-1])
            i = i+1
    except EOFError:
        break
