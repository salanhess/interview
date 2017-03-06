#!/bin/bash

import os

#Case1:lambda func
a = lambda x,y:x+y
print a(3,11)

#Case2: a /b switch without temp variable
def switch(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b
print "Original is 3,5, after switch is:"
print switch(3,5)

#Case3:reverse string
s1 = 'abcdef'
def str_reverse(strs):
    tmp = []
    for i in range(0,len(strs)):
        tmp.append(strs[len(strs)-i-1])
    return ''.join(tmp)

print "Original string is %s" % (s1)
print str_reverse(s1)
#print len(s1)

