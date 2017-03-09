#coding=utf-8
#@description: Charpter 9
#[expr for iter_var in iterable]
print([x*2 for x in range(1,11) if x %2 == 1])

#sort/reverse
l1 = [33,11,22,44]
l1.sort()
print(l1)
l1.reverse()
print(l1)

#append,insert
a = [1,99,33,44,55,22]
b = [11,33,54]
a.append(b)
print(a)
a.pop()
a.insert(3,101)
print(a)

#[]list auto-generated
print([x for x in range(1,101) if x %2 == 0])

