#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = 'I,am,lilei'
print(s.split(',')[1])
print(s[2:4])

print(s.replace(',','=',1))
fpath = r'test.txt'
fnew = r'new.txt'
f = open(fpath)
# contents = f.read()
# print(contents)
# f.close()

fn = open(fnew,'w')
count = 0
for line in f:
    count +=len(line)
    print(line[:-1])
    if '2017' in line:
        line = line.replace('2017','2018')
    fn.write(line)
f.close()
fn.close()
print("total len is: %d" % (count))

#replace 2017=>2018
fn = open(fnew)
for line in fn:
    print(line[:-1])
    print("current line len is: %d" % (len(line)))
fn.close()

#reference in python: the a/b have same address in memory
a = 'abc'
b = ''
print("id(a) is: %s, id(b) is: %s" % (id(a),id(b)))

b = a
print("id(a) is: %s, id(b) is: %s" % (id(a),id(b)))

import sys
cinfo = '1234'
print(id(cinfo))
print(sys.getrefcount('1234'))

binfo = '1234'
print(id(binfo))
print(sys.getrefcount('1234'))
#four method to merge string together
#Method1:
a = '字符串拼接1'
b = '字符串拼接2'
print("c is {c}".format(c=a+b))
#Method2:
c = [a,b]
print(''.join(c))
#Method3
print('%s%s' % (a, b))
#Method4
print("{a}{b}".format(a=a,b=b))

import string
print(string.digits)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.ascii_letters)

strinfo = "%s%s%s%s" % (string.digits,string.punctuation,string.ascii_lowercase,string.ascii_uppercase)
print(strinfo)

a = "i,am,a,boy,in,china"
##1.假设boy和china是随时可能变换的，例boy可能改成girl或者gay，而china可能会改成别的国家，你会如何将上面的字符串，变为可配置的。
ac = "i,am,a,%(sex)s,in,%(country)s"  % {'sex':'girl','country':'china'}
bc = "i,am,a,{sex},in,{country}" .format (sex='girl',country='india')
print(ac)
print(bc)
#find the first i in string
print(a.index('i'))
print(len(a))
#find i in china pos
print(a.rfind('i'))
#count ',' in string
print(a.count(','))

f = open('test.log','w')
#redirect standard output from console to file handle
sys.stdout = f
help(string)
f.close()
