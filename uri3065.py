i = 1
while True:
    n = int(input())
    if(n == 0):
        break
    else:
        x = input()
        x = x.replace('+0+','A')
        x = x.replace('+0-','B')
        x = x.replace('-0+','C')
        x = x.replace('-0-','D')
        x = x.replace('-0','-')
        x = x.replace('+0','+')
        x = x.replace('A','+0+')
        x = x.replace('B','+0-')
        x = x.replace('C','-0+')
        x = x.replace('D','-0-')
        if(x[-1]=='-' or x[-1]=='+'):
          x = x[:-1]
        x = eval(x)
        print("Teste",i)
        print(x)
        print("")
        i = i+1
