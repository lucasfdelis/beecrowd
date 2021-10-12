a = 1
while True:
    try:
        n = int(input())
        lista = list(range(201))
        lista2 = []
        soma1 = 0
        soma2 = 0
        lista2 = [0] * 201
        if(n == 0):
            break
        else:
            i = 0
            while(i < n):
                x,y = input().split()
                x = int(x)
                y = int(y)
                soma1 = soma1+x
                soma2 = soma2+y
                z = y/x
                z = str(z)
                z = z.split('.')
                z = z[0]
                z = int(z)
                lista2[z] = lista2[z]+(x)
                i = i+1
            if(a > 1):
                print('')
                print('Cidade# {}:'.format(a))
            else:
                print('Cidade# {}:'.format(a))
            a = a+1
            lista3 = 'a'
            for i in range(201):
                print(end='')
                if(lista2[i]>0):
                   lista3 = lista3+" "+("{}-{}".format(lista2[i],lista[i]))
            lista3 = lista3.replace('a ','')
            print(lista3)
            consumo = soma2/soma1
            consumo = str(consumo)
            consumo = consumo.split('.')
            dig = consumo[1]
            if(len(dig) == 1):
                dig = dig+'0'
            dig = dig[:2]
            consumo = consumo[0]+'.'+dig
            print('Consumo medio: {} m3.'.format(consumo))
    except EOFError:
        break
