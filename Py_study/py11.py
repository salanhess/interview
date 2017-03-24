#coding=utf-8

#元组不可变的好处。保证数据的安全，比如我们传给一个不熟悉的方法或者数据接口，确保方法或者接口不会改变我们的数据从而导致程序问题。
#tuple
def info(a):
    '''一个我们不熟悉的方法'''
    a[0] = 'haha'
a = [1, 2, 3]

info(a)
print(a)

#following will cause error, but as we expected.
#b = (1,2,3)
#info(b)

# python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素.
# 集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.
info = set(['a','b', 'c'])
#add only 1 element
info.add('def')
print(info)
#adds an element, update "adds" another iterable set, list or tuple
info.update('ef','gg')
print(info)
print('a' in info)
info.remove('a')
print('a' in info)
info.remove('b')
print(info)

#due to set is
listdup = [1,5,3,2,1,6,10,9]
print(listdup)
print(list(set(listdup)))

#交集，并集，差集 & | -
a1 = set('abc')
b1 = set('efg')
c1 = set('21a')
#cross
print(a1 & c1)
#merge
print(a1 ^ b1)
#diff
print(a1 -c1)

liststr = ['haha','gag','hehe','haha']
print(list(set(liststr)))

#remove duplicate element by list method
m = []
for i in liststr:
    if i not in m:
        m.append(i)
print(m)

#modify a = (1,2,3) to (5,2,3) with two method
#Method 1:modify in list then covernt to tuple
a = (1,2,3)
m = []
for i in a:
    if i == 1:
        m.append(5)
    else:
        m.append(i)
print(tuple(m))

#Method 2:merge two tuple together
b = (5,)+a[1:]
print(b)

#a = set(['a','b','c'])
a = set(['a','b','c'])
a.add('jay')
b = set(['b','e','f','g'])
print(a)
print(b)
#Method1: merge a and b, include element which contain in both a and b
#merge a and b ,include element which contain in both a and b
print(a | b)
#merge a and b ,include element which contain in both a and b
print(a ^ b)

#Method2: merge a and b, include element which contain in both a and b
#use list to store
m = []
for i in a:
    m.append(i)
for i in b:
    m.append(i)
print(set(m))
