#coding=utf-8

'''2. 已知字典：
ainfo = {'b':'python','a':'haha','c':'hehe','f':'xiaoming'}

2.1 迭代字典，输出结果：
('a', 'haha')
('c', 'hehe')
('b', 'python')
('f', 'xiaoming')

2.2 用2种方法输出结果：
a
c
b
f

2.3 写出查找字典里面值等于'haha'的key的代码
'''
ainfo = {'b':'python','a':'haha','c':'hehe','f':'xiaoming'}
#2.1
print(sorted(ainfo.items(),key = lambda x: x[0]))

#2.2
#Method1:
print(sorted(ainfo.keys()))

#2.3 写出查找字典里面值等于'haha'的key的代码
for key,value in ainfo.items():
    if value == 'haha':
        print(key)
print("==================")

#iterable
lst = range(3)
it = iter(lst)
print(next(it))
print(next(it))
print(next(it))

#TBD: generater with yiedl

#tanslate maketrans
str1 = "My name is cary"
intab="cary"
outtab="1234"
transtab = str1.maketrans(intab,outtab)
print(str1.translate(transtab))
print(transtab)

#with:
somefileName = r'C19.py'
with open(somefileName,encoding='utf-8') as somefile:
    for line in somefile:
        #print(line)
        continue
        # ...more code
