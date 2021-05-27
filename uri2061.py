n,m = input().split()
n = int(n)
m = int(m)
i = 0
while(i < m):
    a = input()
    if(a == 'fechou'):
        n = n+1
    else:
        n = n-1
    i = i+1
print(n)
