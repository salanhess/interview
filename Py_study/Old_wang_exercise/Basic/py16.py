#coding=utf-8
__author__='Cary Bai'

a,b = 5,3
# if a > 1 and a < 10:
#     print('haha,a = {}'.format(a))
if a==5 and b==3:
    print('a = %d, b = %d' % (a,b))

a,b = 1,2
# if b > a:
#     print('b > a' )
if b-a > 0:
    print('b > a')

#三元运算符
print(a if a<b else b)
print('b' if a>b else b-a)
