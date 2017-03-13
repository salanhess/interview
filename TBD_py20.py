#coding=utf-8

def Max(a,b,c):
    maxVal = a
    if a < b:
        maxVal = b
    if b < c:
        maxVal = c
    return maxVal

print(Max(123,345,444))

#Get max value from not fixed parameters list
def Maxtuple(*T):
    maxVal=T[0]
    #print(len(T))
    for i in range(1,len(T)):
        if maxVal < T[i]:
            maxVal = T[i]
    return maxVal

print(Maxtuple(123,345,444))

# def ainfo(x,y,z):
#     print(y,z,x)

#refer to http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000
#函数的参数
# def ainfo(x,y,z):
#     print(y,z,x)

def ainfo1(x,y,z,**kw):
    print(y, z, x)

def ainfo2(**kw):
    print([i+'aay' for i in kw.keys()])

ainfo1(x=88,y=22,z=44)
ainfo2(x=88,y=22,z=44)
