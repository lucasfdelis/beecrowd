n = int(input())
total = n*n
divisao = total/2
if(divisao%2 == 0):
    print(f'{int(divisao)} casas brancas e {int(divisao)} casas pretas')
else:
    print(f'{int(divisao+0.5)} casas brancas e {int(divisao-0.5)} casas pretas')