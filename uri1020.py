# -*- coding: utf-8 -*-

idd = int(input())
print(idd//365,"ano(s)")
idd = (idd-((idd//365)*365))
print(idd//30,"mes(es)")
idd = (idd-((idd//30)*30))
print(idd,"dia(s)")
