a,b = input().split()
a = int(a)
b = int(b)
i = 0
lista1 = []
while(i < a):
    c = input()
    c = c.lower()
    lista1.append(c)
    i = i+1
i = 0
lista2 = ''
while(i < b):
    c = input()
    c = c.lower()
    c = c[::-1]
    lista2 = lista2+'0'+c
    i = i+1
i = 0
while(i < a):
    c = lista1[i]
    if(lista2.find(lista1[i])!= -1 or lista2.find(c[::-1]) != -1):
        print("Sheldon come a fruta",c)
    else:
        print("Sheldon detesta a fruta",c)
    i = i+1
