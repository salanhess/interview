#  coding=utf-8
#C5: digui check
#递归基本思想: 如果字符串小于等于1，肯定是回文。 如果不相等，直接返回错误，反之则将字符串首尾截断再次递归
#非递归思路: 如果字符串小于等于1，肯定是回文。然后设置一个标记位，循环获取字符串长度进行比较(这里有待优化)进行比较

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