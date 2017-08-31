#  coding=utf-8
#C5: digui check


def my(str, size):
    if size <= 1:
        return True
    if str[0] != str[size-1]:
        return False
    return my(str[1:size-1], size-2)

def my2(str):
    if len(str) <= 1:
        return True
    if str[0] != str[len(str)-1]:
        return False
    return my2(str[1:len(str)-1])

def nodigui(mystr):
    if len(mystr) <= 1:
        return True
    flag = False
    for i in range(len(mystr)):
        if mystr[i] == mystr[len(mystr)-i-1]:
            flag = True
        else:
            flag = False
    return flag

def unit():
    tstr1 = "1"
    tstr2 = "121"
    tstr3 = "1221"
    tstr4 = "1213"

    testsuite = [tstr1, tstr2, tstr3, tstr4]

    for tstr in testsuite:
        print my(tstr, len(tstr))
        print my2(tstr)
        print nodigui(tstr)

unit()