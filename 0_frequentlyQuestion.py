#coding=utf-8

#normal py questions refer to https://taizilongxu.gitbooks.io/stackoverflow-about-python/content/index.html
#yield /generator /iterator

#1 yeild iterator 迭代, range, 列表推导器的使用
for i in range(0,10):
    print(i )

for i in [x*x for x in range(1,5)]:
    print(i)
print("=========")

#b. generator 生成器: 生成器也是迭代器的一种,但是你只能迭代它们一次.原因很简单,因为它们不是全部存在内存里,它们只在要调用的时候在内存里生成
#c. yield, return, but only do operation while this func be called
def Create_generator():
    for i in (x+2 for x in range(3,6)):
        yield i

a = Create_generator()
#assert(type(a) == 'class')
print(type(a))

for i in a:
    print(i)
print("=========")

#
class Bank():
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield '$100'


hsbc = Bank()
corner_street_atm = hsbc.create_atm()
#In py3 ,use next(generator)    while py2 use generator.next()
print(next(corner_street_atm))
print(next(corner_street_atm))

wall_street_atm = hsbc.create_atm()
print(next(wall_street_atm))

hsbc.crisis = True
#print(next(corner_street_atm))
#print(next(wall_street_atm))

hsbc.crisis = False
print(next(corner_street_atm))

#Decorator Python 装饰器如何使用

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def say():
    return "hello"

print(say())

#3 自己动手实现装饰器
def my_shiny_new_decorator(a_func_to_decorator):
# 这个函数将被包装在原始函数的外面,所以可以在原始函数之前和之后执行其他代码..
    def the_wrapper_around_the_original_func():
        #把要在原始函数被调用前的代码放在这里
        print("Before call original ,runs")
        # 调用原始函数(用括号!!)
        a_func_to_decorator()
        # 把要在原始函数被调用后的代码放在这里
        print("After call func, runxxx")
    return the_wrapper_around_the_original_func

#装饰器实际上做的事情就是如下：定义了一个新函数，该函数是定义的装饰器函数的返回值，其装饰器函数参数就是需要被装饰的函数
# a_stand_along_func_decoratored = my_shiny_new_decorator(a_stand_along_func)
# a_stand_along_func_decoratored()

@my_shiny_new_decorator
# 加入你建了个函数,不想修改了
def a_stand_along_func():
    print("I dare you can't modify me~")

a_stand_along_func()
print("=========")

#4 如何检测一个文件是否存在
import os
fpath = r't.txt'
print(os.path.exists(fpath))

#5 三元运算符
a,b,c = 1,2,3
print(a if a > b else c)

#6 在Python中调用外部命令
print(os.system("ls |grep txt"))

#7 在Python里如何用枚举类型?
from enum import Enum
Animal = Enum('Animal','ant bee cat dog')
print(Animal['cat'])
myAnimal = Animal.cat
print(myAnimal)

#8如何在一个表达式里合并两个字典?
d1 = {'name':'cary','age':24}
d2 = {'job':'IT','salary':1000}
#py3
d3 = dict(list(d1.items())+list(d2.items()))
#py2
#d3 = dict(d1.items()+d2.items())
print(d3)
#print(d1.items())

#11 用字典的值对字典进行排序
import operator
#use key to sort
x = {1: 2, 3: 4, 4:3, 2:1, 0:0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
#Method2:
sorted_x2 = sorted(x.items(),key= lambda x:x[1])
print(sorted_x)
print(sorted_x2)
#use key to sort
sorted_x = sorted(x.items(), key=operator.itemgetter(0))
print(sorted_x)

#12 如何在一个函数里用全局变量?
global_bear = 'Cary'

#declear global first,then can modify this value in func
#如果不加上line143的声明，全局变量的值不会被修改
def func_call():
    global global_bear
    global_bear = 'susan'
    bear = global_bear
    print(bear)

func_call()
print(global_bear)


#13 一个函数是一个被它自己定义而执行的对象;默认参数是一种"成员数据",所以它们的状态和其他对象一样,会随着每一次调用而改变.
def foo(a=[]):
    a.append(5)
    return a

print(foo())
print(foo())
print(foo())

#装饰器@staticmethod和@classmethod有什么区别?
#a 对象实体调用方法的常用方式.对象实体a被隐藏的传递给了第一个参数.
#b 用classmethods装饰,隐藏的传递给第一个参数的是对象实体的类(class A)而不是self.
#c 用staticmethods来装饰,不管传递给第一个参数的是self(对象实体)还是cls(类).它们的表现都一样:
class A(object):
    def foo(self,x):
        print("execute foo(%s ,%s)" % (self,x) )

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("execute static_foo(%s)" % (x))

a = A()
a.foo(1)
a.static_foo(1)
a.class_foo(1)
# execute foo(<__main__.A object at 0x10216dfd0> ,1)
# execute static_foo(1)
# executing class_foo(<class '__main__.A'>,1)

#15 检查列表是否为空的最好方法:用隐藏的空列表的布尔值才是最Pythonic的方法.
a = []
if not a:
    print("empty")

#16 怎么用引用来改变一个变量?
#Answer:the_list参数是通过值进行传递的,那么为它赋值将会对方法以外没有影响.the_list是outer_list引用(注意,名词)的一个拷贝,
# 我们将the_list指向一个新的列表,但是并没有改变outer_list的指向.
#So: 你可以返回一个新值.这不会改变传过来的值,但是能得到你想要的结果.

#17 检查一个文件夹是否存在,如果不存在就创建它
fpath = r'tesxx.xx'
if not os.path.exists(fpath):
    os.makedirs(fpath)
    print("make %s" % fpath)

#18 if __name__ == "__main__":是干嘛的?
#用来告诉py当前的py为主模块执行入口

#19理解Python中super()和__init__()方法
#super()的好处就是可以避免直接使用父类的名字.但是它主要用于多重继承,这里面有很多好玩的东西.如果还不了解的话可以看看官方文档
class Base(object):
    def __init__(self):
        print("Base created")

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super().__init__()

print(ChildA(),ChildB())

#20 在循环中获取索引(数组下标) enumerate!!!
ints = [8, 23, 45, 12, 78]
for idx, val in enumerate(ints):
    print(idx, val)

#My ugly way :(
for i in range(0,len(ints)):
    print('Index %d: %s' % (i,ints[i]))

#21 Python中的append和extend
l1 = [1,2]
l2 = [3,4]
l1.append(l2)
#After append
print(l1)
#After extend
l1 = [1,2]
l1.extend(l2)
print(l1)

#22 字典里添加元素的方法
d1 = {'a':1,'b':2}
print(d1)
d1['c']=3
print(d1)
#Method2: use update
d1.update({'d':4,'e':5})
print(d1)

#23 Python中有检查字符串包含的方法吗?
s1 = 'abcdefg123'
substr = 'bcd'
print(substr in s1)

#24 在一行里获取多个异常: except (AssertionError,NotADirectoryError) as e:
def catch_exception():
    try:
        assert(1==2)
        print("error")
    except (AssertionError,NotADirectoryError) as e:
        print("other error")

catch_exception()

#26 类里的静态变量
#"i"变量是类级别的,所以它是和所有实体级的"i"变量是不一样的
#详细参考 https://docs.python.org/3/tutorial/classes.html#class-objects
class Myclass():
    i = 5
    def Mytest(self):
        #i = 111 如果不进行初始化，I的值是内存中的，并非类中定义的，类实例化后取得的i值才是类中所定义的值
        print("Mytest i is: %d" % (i))

my = Myclass()
my.i=1
my.Mytest()
print(Myclass.i,my.i)

#27 如何移除换行符?: 使用rstrip，类似的还有rstrip lstrip
print('test string\n')
print('test string\n'.rstrip())

#29 理解Python切片：重点需要记住的是::end值代表的是不被选中的第一个位置
'''a[start:end] # 从start开始到end-1结束
a[start:]    # 从start开始直到末尾
a[:end]      # 从头部开始直到end结束
a[:]         # 复制整个列表
a[-1]    # 列表最后一个元素
a[-2:]   # 列表最后两个元素
a[:-2]   # 除了最后两个元素剩下的部分
'''

#31 Python有没有静态方法使我可以不用实例化一个类就可以调用
#请少用staticmethod方法!在Python里只有很少的场合适用静态方法,其实许多顶层函数会比静态方法更清晰明了.
class Myclass(object):
    @staticmethod
    def NoInstance(x):
        print(x)

Myclass.NoInstance(2)

#33 把字符串解析成浮点数或者整数
a = '33.33123'
print(float(a))
assert(type(float(a)) == float)
#print(int(a))

#37 为什么是string.join(list)而不是list.join(string)?
#是因为所有的可迭代对象都能被join,不仅仅是列表,但结果是我们一般要join的都是字符串.
l1 = ['hello','world']
print("-".join(l1))

#Following not work in py3
# import urllib5
# print('\n############\n'.join(urllib5.urlopen('http://data.stackexchange.com/users/7095')))

#38 在Python里获取当前时间
import datetime
print(datetime.datetime.now().time())

#39 在Python中列出目录中的所有文件: os.listdir()
folderpath = r'/Users/hbai/000study'
print(os.listdir(folderpath))
f = []
for dirpath, dirnames, filenames in os.walk(folderpath):
    if '1024' in dirpath:
        #print(dirpath, dirnames, filenames)
        f.append(dirpath)
print(f)

#40 在Python怎么样才能把列表分割成同样大小的块?
#使用yield 生成器,注：这里必须使用生成器来进行，如果用return，是没有办法进行迭代继续操作的

l = [x for x in range(1,100)]
n = 10
def chunks(l,n):
    for i in range(0,len(l),n):
        yield l[i:i+n]

#import pprint
#pprint.pprint(list(chunks(l, n)))
print(list(chunks(l, 10)))

#使用yield来生成斐波拉切数列

def fab(Max):
    a,b = 0,1
    while b < Max:
        yield b
        a, b = b,a+b

index = 0
for i in fab(5):
    index +=1
    print('Index %d: %d' % (index,i))

#41 检查字符串是否为数字 :查了一下区别，建议使用isdigit，比isalnum检查范围更广一些
s1 = '12ab3'
print(s1.isdigit())

s2 = '123'
print(s2.isalnum())

#给2n+1个数，其中n个数均出现了2次，有1个数只出现了1次，如何找出这个数？
L1 = [2,2,1,3,3,4,1,5,4,5,6]
dic = {}
Flag = ''
for i in L1:
    if i in dic.keys():
        dic[i]=2
    else:
        dic[i]=1
        Flag = i
print(Flag)

#string isnumberic isdigit的区别
# hbaitekiMacBook-Air:.ssh hbai$ python
# Python 2.7.6 (default, Sep  9 2014, 15:04:36)
# [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> unicode.isdigit.__doc__
# 'S.isdigit() -> bool\n\nReturn True if all characters in S are digits\n
#  and there is at least one character in S, False otherwise.'
# >>> unicode.isumberic.__doc__
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: type object 'unicode' has no attribute 'isumberic'
# >>> unicode.isnumeric.__doc__
# 'S.isnumeric() -> bool\n\nReturn True if there are only numeric characters in S,\nFalse otherwise.'
'''

    The method isnumeric() checks whether the string consists of only numeric characters.
    This method is present only on unicode objects.

    Digits include decimal characters and digits that need special handling,
    such as the compatibility superscript digits. Formally,
    a digit is a character that has the property value Numeric_Type=Digit or Numeric_Type=Decimal.
'''

#tuple和list可以做dict的key吗
#list可变，不能被hash，所以只有tuple可以做key
tuple1 = (2,1)
list1 = [1,2]
dic1 = {tuple1:list1}
print(dic1)
# dic2 = {list1:tuple1}
try:
    dic2 = {list1:tuple1}
except TypeError as e:
    print("xxx")
    print(TypeError)

#python的regex模块re，search和match的区别?
#re.match只匹配字符串的开始，而re.search匹配整个字符串
import re
p = 'abc'
str1 = '1abcdef'
print(re.search(p,str1))
print(re.match(p,str1))

str2 = 'abcdef'
print(re.search(p,str2))
print(re.match(p,str2))

#正则表达式文档参考 http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html
s = 'one1two2three3four4'
#如何分割得到['one','two','three','four'] ?
p = re.compile(r'\d+')
print(len(p.search(s).group())) #可以看出只有一个group
print(p.split(s)[:-1])

#如何得到里面的数字: ['1', '2', '3', '4']
p = re.compile(r'\d+')
print(p.findall(s))

#搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。返回 1 2 3 4
p = re.compile(r'\d+')
for i in p.finditer(s):
    print(i.group())

#sub 用法：替换，用组的方式替换制定单词，并且指定次数
s = "i say, hello world!"
p = re.compile(r'(\w+) (\w+)')
print(p.sub(r'\2 \1',s,2))

#找到并打印text中所有包含oo的单词: findall
text = "JGood is a handsome boy, he is cool, clever, and so on..."
p = re.compile(r'\w*oo\w*')
print(p.findall(text))
# #将字符串中含有'oo'的单词用[]括起来。
print(p.sub(lambda x: '[' + x.group(0) + ']',text ))

#调用工debug具pdb: l 查看  n 逐行执行  c 继续执行  p 查看变量 p <parametername>
import pdb
#pdb.set_trace()
print("I'm debuging")

#42 查找列表中某个元素的下标: 使用index命令
l = [1,3,6,5]
print(l.index(3))

#43 有什么方法获得一个字符串的字串,比如从一个字符串的第三个字符到最后.
print(l[2:])

#44 为什么代码在一个函数里运行的更快?
#运行比较慢，我注释掉了
'''
运算时间：4.9149510860443115
运算时间：7.055168151855469
'''
# import time
# now = time.time()  # 代码开始时间  # 前期准备，整理数据
# def main():
#     for i in range(10**8):
#         pass
# main()
#
# print('运算时间：%s'%(time.time() - now))  # 整体运行时间
#
# now = time.time()  # 代码开始时间  # 前期准备，整理数据
# for i in range(10**8):
#     pass
#
# print('运算时间：%s'%(time.time() - now))  # 整体运行时间

'''你或许想问为什么存取一个本地变量比全局变量要快.这有关于CPython的实现细节.

记住CPython解析器运行的是被编译过的字节编码(bytecode).当一个函数被编译后,局部变量被存储在了固定大小的数组(不是一个dict),
而变量名赋值给了索引.这就是为什么你不能动态的为一个函数添加局部变量.检查一个局部变量就好像是一个指针去查找列表,
对于在PyObject上的引用计数的增长是微不足道的.

相反的在查找全局变量(LOAD_GLOBAL)时,涉及到的是一个实实在在的dict的哈希查找.
顺便说一句,这就是为什么当你想要一个全局变量你必须要在前面加上global i:
如果你在一个区域内指定一个变量,编译器就会建立一个STORE_FAST的入口,除非你不让它那么做.
在说一句,全局查找速度也不慢.真正拖慢速度的是像foo.bar这样的属性查找!
'''
#45 合并列表中的列表
l = [[1,2,3],[4,5,6], [7], [8,9]]
new = []
def mergeList(l):
    for i in l:
        if isinstance(i,list):
            mergeList(i)
        else:
            new.append(i)

mergeList(l)
print(new)
#Note：following method is cool in stackoverflow but it's ONLY for list[list]
#l = [[1,2,3],[4,5,6], [7], [8,9],[1,[2,3]]]
print([item for sublist in l for item in sublist])

#47 检查一个键在字典中是否存在
dic1 = {'name':'cary','age':100}
print('name' in dic1.keys())

#48 在列表中随机取一个元素: random.choice()
foo = ['a', 'b', 'c', 'd', 'e']
import random
for i in range(0,len(l)):
    #print(foo[random.randrange(0,len(foo))])
    print(random.choice(foo))

#49 通过列表中字典的值对列表进行排序: sorted 函数，然后对每个list的字典元素使用k['name']获取值
l1 = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}, {'name':'Cart', 'age':2}]
print(sorted(l1,key= lambda k: k['name']))

#通过age排序
print(sorted(l1,key = lambda item: item['age']))

#50 复制文件: os 里面没有copy方法
import shutil
src = r'twit.txt'
dst = r'twit_copy.txt'
shutil.copyfile(src,dst)

#53 从相对路径引入一个模块
#TBD

#54 如何知道一个对象有一个特定的属性? 使用hasattr(objInstanceName,funcname)  ,类似 isinstance(objectName,expectedType)的用法
class Myclass(object):
    mystr = 'cary'
    def hello(self):
        print("hi %s" % self.mystr)

new = Myclass()
new.mystr = 'susan'
new.hello()
print(hasattr(new,'hello'))

#55 *args和 **kwargs的用法
#*args 不确定有多少参数的时候使用,可以看做是列表来使用
def get_args(*args):
    for i in range(0,len(args)):
        print("Index %d: args is : %s" % (i,args[i]))

get_args(1,2,3,4)
list_args = ['a','c','d','b']
get_args(*list_args)

#**kwargs是字典,使用时要用.item() 来调用
def get_dict_args(**kwargs):
    for key,value in kwargs.items():
        print("key is: %s , value is %s" % (key,value))

    print(kwargs)

get_dict_args(name='abc',value=100)

#56 如何获取实例的类名  type(Instancename).__name__ 属性
print(type(new).__name__)

#57 字典推导式语法:d = {key: value for (key, value) in iterable}
L = [1,2,3,4,5,6,7,8,9]
dic1 = {key:key*10 for key in L}
print(dic1)

#58 反转字符串
