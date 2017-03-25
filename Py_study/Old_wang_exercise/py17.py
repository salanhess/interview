#coding=utf-8
__author__='Cary Bai'

#print 1~10 use while two method
#Method1:
i = 1
while i < 11:
    print(i)
    i+=1

print("#########################################")
#Method 2
i =1
while True:
    print(i)
    i+=1
    if i > 10:
        break

print("use for and continue to output 1 3 5 7 9")
i =1
for i in range(1,10):
    if i % 2 ==0:
        continue
    else:
        print(i)
    i+=1

a = [x for x in range(1,7)]
print('a = %s' % a)
for i in a:
    if 8 in a:
        print('find')
    else:
        print('not find')

#change a to [2,3,4,5,6,7]
# a.remove(1)
# a.append(7)
# print(a)
i =0
while True:
    #print(a[i])
    if a[i] == 1:
         print(a[i])
         #a.pop(i)
    i+=1
    if i > 5:
        break
print(a)
