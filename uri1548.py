n = int(input())
i = 0
lista = []
while(i < n):
    m = int(input())
    lista = input().split()
    lista2 = lista
    j = 0
    while(j < m):
        lista[j]=int(lista[j])
        j = j+1
    lista = sorted(lista)
    lista = lista[::-1]
    j = 0
    while(j < m):
        if(lista[j]==lista2[j]):
            lista2[j]='#'
        j = j+1
    lista2 = ''.join(str(lista2))
    print(lista2.count('#'))
    i = i+1
