#coding=utf-8

#2： how to get bigger version?
version1 = [1,22,2,6,3,1]
version2 = [1,22,2,4,5]

def cmp(s1,s2):
    if s1 == s2:
        return 0
    elif s1 > s2:
        return 1
    elif s1 < s2:
        return -1


def check_ver(v1,v2):
    #The base line should be the smaller length List
        for i in range(min(len(v1),len(v2))):
            flag = cmp(v1[i],v2[i])
            if flag !=0:
                if flag > 0:
                    print("s1 is bigger")
                    return
                else:
                    print("s2 is bigger")
                    return
        if len(v1) == len(v2):
            print("really same!")
        else:
            print("max len list %s is bigger" % (v1 if len(v1) > len(v2) else v2))

version1 = [1,22,2,6,3,1]
version2 = [1,22,2,4,5]
check_ver(version1,version2)

version1 = [1,22,2]
version2 = [1,22,2,3]
check_ver(version1,version2)


version1 = [1,22,2]
version2 = [1,22,2]
check_ver(version1,version2)

# #1 正则表达式：这一块处理较少，忘得差不多了
# codeNum = '44012'
# #get 12 from str by re
# import  re
# patten = re.compile(r'\d5')
# match = patten.match(codeNum)
# if match:
#     print(match.group())
#
# p = re.compile(r'(\w+) (\w+)')
# s = 'i say, hello world!'
#
# match = p.match(s)
# if match:
#     print(match.group())
#
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配