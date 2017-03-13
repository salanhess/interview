#coding=utf-8
'''
1.已知字符串
a = "aAsmr3idd4bgs7Dlsf9eAF", 要求如下
1.1 请将a字符串的大写改为小写，小写改为大写。
1.2 请将a字符串的数字取出，并输出成一个新的字符串。
1.3 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a': 4, 'b': 2}
1.4 请去除a字符串多次出现的字母，仅留最先出现的一个。例 'abcabb'，经过去除后，输出 'abc'
1.5 请将a字符串反转并输出。例：'abc'的反转是 'cba'
1.6 去除a字符串内的数字后，请将该字符串里的单词重新排序（a - z），并且重新输出一个排序后的字符串。（保留大小写, a与A的顺序关系为：A在a前面。例：AaBb）
1.7 请判断'boy' 里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输出False.
1.8 要求如1.7，此时的单词判断，由'boy'改为四个，分别是'boy', 'girl', 'bird', 'dirty'，请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。
1.9 输出a字符串出现频率最高的字母
'''
a = "aAsmr3idd4bgs7Dlsf9eAF"
b = []
#1.1
for i in range(0,len(a)):
    #print(a[i])
    if a[i].islower():
        b.append(a[i].upper())
    elif a[i].isupper():
        b.append(a[i].lower())
    else:
        b.append(a[i])
print(''.join(b))
#1.2
b = []
for i in range(0,len(a)):
    #print(a[i])
    if a[i].isdigit():
        b.append(a[i])
print(''.join(b))
#1.3
d = {}
a = a.upper()
for i in range(0,len(a)):
    if a[i] not in d.keys() and not a[i].isdigit():
        d[a[i]]=a.count(a[i])
print(d)
print(sorted(d.items(),key = lambda x :x[0]))
#1.4
a = "aAsmr3idd4bgs7Dlsf9eAF"
b=[]
for i in range(0,len(a)):
    if a[i] not in b:
        b.append(a[i])
print(''.join(b))

#1.5 reverse string
print(a[::-1])

#1.6 resort after remove digit
a = "aAsmr3idd4bgs7Dlsf9eAF"
b=[]
for i in range(0,len(a)):
    if not a[i].isdigit():
        b.append(a[i])
b.sort()
print(''.join(b))

#1.7 check 'boy' whether in list a
Flag = 0
a = "aAsmr3idd4bgs7Dlsf9eAFbby"
for i in range(0,len(a)):
        if a[i] == 'b':
            Flag+=1
        elif a[i] == 'o':
            Flag+=10
        elif a[i] == 'y':
            Flag+=100
print(True if Flag > 111 else False)

#1.8 check 'boy', 'girl', 'bird', 'dirty' whether is a
a = "aAsmr3idd4bgs7Dlsf9eAFbbyboygirlbirddirtyhah"
#a = "aAsmr3idd4bgs7Dlsf9eAFbbyboygirlbirddirty"
verfiyL = ['boy', 'girl', 'bird', 'dirty','haha']
#new_verfiyL = ''.join(sorted(''.join(verfiyL)))
new_verfiyL = ''.join(verfiyL)
new_a = ''.join(a)

def count_alpha(s):
    tmp = {}
    for i in range(0,len(s)):
        if s[i] not in tmp.keys():
            tmp[s[i]] = s.count(s[i])
    return tmp
# print(count_alpha(new_verfiyL))
# print(count_alpha(new_a))

tmpstr=[]
for i in count_alpha(new_verfiyL).keys():
    if i in count_alpha(new_a).keys():
        if count_alpha(new_a)[i] >= count_alpha(new_verfiyL)[i]:
            tmpstr.append(i)

print( True if len(count_alpha(new_verfiyL)) == len(tmpstr) else False)


#2. 在python命令行里，输入import this 以后出现的文档，统计该文档中，"be" "is" "than"的出现次数。
import_this="The Zen of Python, by Tim Peters\
Beautiful is better than ugly.\
Explicit is better than implicit.\
Simple is better than complex.\
Complex is better than complicated.\
Flat is better than nested.\
Sparse is better than dense.\
Readability counts.\
Special cases aren't special enough to break the rules.\
Although practicality beats purity.\
Errors should never pass silently.\
Unless explicitly silenced.\
In the face of ambiguity, refuse the temptation to guess.\
There should be one-- and preferably only one --obvious way to do it.\
Although that way may not be obvious at first unless you're Dutch.\
Now is better than never.\
Although never is often better than *right* now.\
If the implementation is hard to explain, it's a bad idea.\
If the implementation is easy to explain, it may be a good idea.\
Namespaces are one honking great idea -- let's do more of those!"

print(import_this.count("be"))
print(import_this.count("is"))
print(import_this.count("then"))


#3.一文件的字节数为102324123499123，请计算该文件按照kb与mb计算得到的大小。
fsize = 102324123499123
print(fsize/1024)
print(fsize/1024/1024)

#4.已知a = [1, 2, 3, 6, 8, 9, 10, 14, 17], 请将该list转换为字符串，例如'123689101417'.
a = [1, 2, 3, 6, 8, 9, 10, 14, 17]
print(''.join([str(x) for x in a]))
