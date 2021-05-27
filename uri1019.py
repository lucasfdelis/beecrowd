# -*- coding: utf-8 -*-

N=int(input())
h=N//3600
N=(N-((N//3600)*3600))
m=N//60
N=(N-((N//60)*60))
print ("%d:%d:%d" % (h, m, N))
