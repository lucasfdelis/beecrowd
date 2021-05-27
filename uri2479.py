n = int(input())
i = 0
lista = []
comportou = 0
ncomportou = 0
while(i < n):
    a,b=input().split()
    lista.append(b)
    if(a=='+'):
        comportou = comportou+1
    else:
        ncomportou = ncomportou+1
    i = i+1
lista = sorted(lista)
i = 0
while(i < n):
    print(lista[i])
    i = i+1
print('Se comportaram:',comportou,'| Nao se comportaram:',ncomportou)
