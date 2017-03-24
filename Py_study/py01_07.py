#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Refore to <Old Wang Based Python> Charpter 1~7 exercise

import string

#<Old Wang Based Python>
str1 = "  pythonisgreat  "
#1.remove space in the left
print(str1.lstrip())
#2.remove space in the right
print(str1.rstrip())

#3. remove all the space
print (str1.strip())
#print(''.join(str1.split()))

str11 = "66  pythonisgreat  66"
print(str11)
print(str11.strip('66'))
#4.upper chars
print(str1.upper().strip())

#5.lower chars
str2="AbC"
print(str2.lower())

#6.check var type:str/list
print(type(str2))
print(type(str1.split()))

#Chapter5
info = 'abdd'
#replace d with c,count=1 means ONLY replace once
print(info.replace('d','c',1))

#convert string to int then can add
a = '1'
b = 2
print(int(a)+b)

#Chapter6  : / forward slash ; \backslash used to Escape Sequence
print('I\'m Lily')
#print('I'm Lily')  will error,because ' need to escape with \ backslash

#Assci unicode utf-8 diff (refer to http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000)
#py3 String is code with Unicode,so it support Chinese display
print('包含中文的str')
#a. ord convert character to int, chr convert int to char
print(ord('A'))
print(chr(25991))

#b. add b before str,convert string to bytes for network transfer
print(type('abc'))
print(type(b'abc'))

#c. encode convert unicode to ascii/utf-8 coding format
print('abc'.encode('ascii'))
print('中文'.encode('utf-8'))
#Following will get UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
#print('中文'.encode('ascii'))

#d. decode convert related format to unicode format,then can display for human read
NeedConvert = b'\xe4\xb8\xad\xe6\x96\x87'
print(NeedConvert + b'\' after decode with utf-8,is: ')
print(NeedConvert.decode('utf-8'))

#Format string with %   %d  for int / %f float / %s  string / %x 16 format int
print("%d , convert to float: %f, convert to string: %s, convert to 16int %x" % (100,100,'abc',17))
#charcter holder space format
print("{dict[host]}{dict[dot]}{dict[domain]}.cn".format(dict={"host":"www","domain":"163","dot":"."}))

#format to float and only left 1 after decimal
s1=72
s2=85
r=(s2-s1)/s1*100
#note: %% is convert escape character for %
print('小明成绩提升:%.1f %%' % r)

#pickup d with at least two method
a = 'abcd'
print(a[-1])
print(a[3])

#Charpter7
#string int tuple , replace ,find, dict  format : all the related operation
#Use dict and format method to display
#Note: detail format string refer to https://docs.python.org/2/library/string.html#format-string-syntax
a = 'pyer'
b = 'apple'
#print("my name is %s, I love %s" % (a,b))
print("my name is {dict[a]}, I love {dict[b]}".format(dict={"a":'pyer',"b":"apple"}))

# write file
import os
print(os.name)
# os.uname() ONLY work in linux
print(os.environ)
fpath = r'info.txt'
f = open(fpath,'w')
f.write("hhh")
f.close()

#print("after re-write,file {fpath} content is:".format(fpath= r'info.txt'))
print("%s content is: " % fpath)
f = open(fpath)
for line in f:
    print(line)
f.close()

import sys
#print(sys.path[0])  get current path
fullfpath = sys.path[0] + '\\'+ fpath
print(os.path.split(fullfpath))
print(os.path.splitext(fullfpath))



