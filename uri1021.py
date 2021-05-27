N = float(input())
cem = N//100
N = N%100
cinquenta = N//50
N = N%50
vinte = N//20
N = N%20
dez = N//10
N = N%10
cinco = N//5
N = N%5
dois = N//2
N = N%2
um = N//1
N = N%1
N = N*100
cinquentam = N//50
N = N%50
vintem = N//25
N = N%25
dezm = N//10
N = N%10
cincom = N//5
N = N%5
umm = N//1
N = N%1
print("NOTAS:")
print(format(int(cem)),"nota(s) de R$ 100.00")
print(format(int(cinquenta)),"nota(s) de R$ 50.00")
print(format(int(vinte)),"nota(s) de R$ 20.00")
print(format(int(dez)),"nota(s) de R$ 10.00")
print(format(int(cinco)),"nota(s) de R$ 5.00")
print(format(int(dois)),"nota(s) de R$ 2.00")
print("MOEDAS:")
print(format(int(um)),"moeda(s) de R$ 1.00")
print(format(int(cinquentam)),"moeda(s) de R$ 0.50")
print(format(int(vintem)),"moeda(s) de R$ 0.25")
print(format(int(dezm)),"moeda(s) de R$ 0.10")
print(format(int(cincom)),"moeda(s) de R$ 0.05")
print(format(int(umm)),"moeda(s) de R$ 0.01")
