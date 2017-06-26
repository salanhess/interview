#coding=utf-8
# refer to http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001418612030427b1f1cf4ea04c41368e8a6753dca43070000


def is_odd(n):
    return n%2 ==1

numstr = [1,2,3,7,9,10,11,16]

print filter(is_odd, numstr)

def containcheck(line,flagstr = ["a","c","d"]):
    tmp = []
    for i in flagstr:
        if i in line:
            tmp.append(line.index(i))
    print tmp

line = "11ab90b39de90c2"

containcheck(line)

def is_odd(n):
    return n%2 ==1

numstr = [1,2,3,7,9,10,11,16]

print filter(is_odd, numstr)

def containcheck(line,flagstr = ["a","c","d"]):
    tmp = []
    for i in flagstr:
        if i in line:
            tmp.append(line.index(i))
    print tmp

line = "11ab90b39de90c2"

containcheck(line)

