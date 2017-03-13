#coding=utf-8
__author__='Cary'

#sorted and generate new List with reversed sequence
a = [3,2,5,1,6]
print(sorted(a,reverse=True))


L = [('b',1),('a',2),('c',4),('d',3)]
#sorted according first element
print(sorted(L))
#sorted according 2nd element
print(sorted(L,key = lambda x:x[1]))
L = [('d', 2), ('a', 4), ('b', 3), ('c', 2)]
#sorted according 2nd element
print(sorted(L,key = lambda x:(x[1])))
#!!! sorted accoring 2nd element,then sorted accoring first element
print(sorted(L,key = lambda x:(x[1],x[0])))
