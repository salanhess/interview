#coding=utf-8
from inspect import isgeneratorfunction
import re
#lamda yield  regular normal use ,such as greedy search  etc.
#jason use

#regular :正则表达式
#参考文档 https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonre/
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143193331387014ccd1040c814dee8b2164bb4f064cff000
#a 正则表达式语法 * + ?    *是贪婪匹配， ？是非贪婪匹配   {m}重复次数 \ 转义   []字符集
#b 正则表达式特殊序列 \d = [0-9]  , \D = [^0-9]  , \s (任意空白字符) = [\t\n\r\f\v] , \S (任意非空白字符)
#                   \w (任意数字和字母) = [a-zA-Z0-9] \W 任意非数字和字母
#                   \A 只在字符串开头进行匹配  \Z 只在字符串结尾进行匹配   \b 匹配位于开头或者结尾的字符串  \B 匹配不位于开头或者结尾的空字符串
#c 正则表达式的主要功能： compile, search,match,sub,spit,findall
#compile 操作  便于读取和修改,为search和match准备
#  comp_pattern = re.compile(pattern, re.X)
#  result = comp_pattern.search(string)
# 或者  result = re.search(pattern,string)
fh = open('TV.html','r')
fh_str = fh.read()
#<a href="/shows/the-flash-2014/abra-kadabra-3449508/" class="ep_name_link">Abra Kadabra</a>
s1 = 'abra-kadabra-3449508'
ti = re.findall("\d{2,4}",s1)
print(ti)


#电话号码匹配:
tel = "My tel is 010-82451234"
tel_pattern = re.compile("\d{3}\-\d{8}")
print(re.search(tel_pattern,tel))

#邮箱匹配
mail = "My email is bill.gates@microsoft.com"
mail_pattern = re.compile("[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.com")
#todo <Tom Paris> tom@voyager.org
#print name, email
print(re.search(mail_pattern,mail))

print("======re test finished======")

#lamda, 匿名函数和列表推导生成器有些像，比较简洁的完成小功能，如相加相减等操作
list1 = [ x for x in range(10)]
print(list1)

g = lambda x: x**2
print(g(2))

m = lambda x,y,z: (x+y)*z
print(m(1,2,3))


#yield : 一种generator ，使用next调用，最后抛出 Stopiteration的异常
'''
一个带有 yield 的函数就是一个 generator，
它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。
看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。
yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，
比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。
如何判断一个函数是否是一个特殊的 generator 函数？可以利用 isgeneratorfunction 判断：
'''
def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n +=1

print("======Start yield======")
print(isgeneratorfunction(fab))
for i in fab(5):
    print(i)

print("======End yield======")

class fab3(object):

    def __init__(self,max):
        self.max = max
        self.n ,self.a, self.b = 0, 0, 1

    # def __iter__(self):
    #     return self

    def next(self):
        while self.n < self.max:
            # r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n +1
            return self.b
        raise StopIteration()

print("======StartIteration======")
f = fab3(5)
for i in range(6):
    try:
        print(f.next())
    except StopIteration:
        print("Finished")

print(isgeneratorfunction(fab3))

def fab2(max):
    l1 = []
    print("generate fab_list")
    n,a,b = 0,0,1
    while n < max:
        l1.append(b)
        a,b = b,a+b
        n +=1
    print(l1)

fab2(5)

def fab1(max):
    print("generate fab")
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n +1
fab1(5)




