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
