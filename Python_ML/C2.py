#coding=utf-8

def lev(a,b):
    if not a: return len(b)
    if not b: return len(a)
    return min(lev(a[1:],b[1:])+(a[0] != b[0]),lev(a[1:],b)+1,lev(a,b[1:])+1)

a = "abc11"
b = "def11111"
print(lev(a,b))