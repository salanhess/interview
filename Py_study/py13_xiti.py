#coding=utf-8
a = [11,22,24,29,30,32]

#insert 28 to the end of a
a.append(28)
print(a)

#insert 57 after 29
a.insert(a.index(29)+1,57)
print(a)

#modify 11 to 26
a[a.index(11)]=26
print(a)

a.remove(32)
print(a)

#Two methods to display 1~8 in list
#Method1
b = [i for i in range(1,6)]
print(b)

b.extend([6,7,8])
print(b)
# #Method2>>>
# print(b+[6,7,8])
# for i in range(6,9):
#     b.append(i)
# print(b)

#Two method to display [5,4]
print(b[-1:-3:-1])
#Method1: split and reverse to display
new = b[3:5]
new.reverse()
print(new)

#Method2: x for to generate after reverse
b.reverse()
new2 = [x for x in b if x > 3 and x < 6]
print(new2)
#Indentify element whether in list
print(2 in b)


b = [23,45,22,44,25,66,78]
#Generate odd in list
print([x for x in b if x%2==1])
#print according requirement
print(['the content' + str(x) for x in b if x%2==1 and x!=25])
#print to add 2
print([x+2 for x in b])

print([x*11 for x in range(1,4)])

#indetify element in tuple
a = (1,4,5,6,7)
print(4 in a)
#modify tuple
tmp = []
for i in list(a):
    if i !=5:
        tmp.append(i)
    else:
        tmp.append(8)
print(tuple(tmp))

#set operation
setinfo = set('abcdefm')
finfo = set('sabcdef')
setinfo.add('abc')
print(setinfo)
setinfo.remove('m')
print(setinfo)

print(setinfo | finfo)
print(setinfo & finfo)

stu_dic = {'liming':{'name':'liming','age':25,'score':{'语文':80,'数学':75,'英语':85}}}
stu_dic['zhangqiang'] = {'name':'zhangqiang','age':23,'score':{'语文':75,'数学':82,'英语':78}}
print(stu_dic)
stu_dic['liming']['score']['python']=60
stu_dic['zhangqiang']['score']['python']=80
stu_dic['zhangqiang']['score']['数学']=89
del stu_dic['liming']['age']
print(stu_dic)
zhangqiang_scores = list(stu_dic['zhangqiang']['score'].values())
zhangqiang_scores.sort()
print(zhangqiang_scores)
