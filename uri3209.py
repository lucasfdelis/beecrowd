n = int(input())
i = 0
lista = []
while(i < n):
  lista = input().split()
  x = int(lista[0])
  lista = lista[1:]
  j = total = 0
  while(j < x):
    total = total+(int(lista[j]))
    j = j+1
  print(total-(x-1))
  i = i+1
