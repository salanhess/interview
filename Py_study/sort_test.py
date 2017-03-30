#coding=utf-8
#算法复杂度参考 http://blog.sina.com.cn/s/blog_771849d301010ta0.html

#left,right, loop
#1. This is a test,so add time decorator to test
#2. But 1000 random will cause sort_quick out of interation, then need to change sys.setrecursionlimit(1500)
#3. But 50000 random will cause python error. then use find_recursionlimit.py to check, found current sys Max is 15200
'''
sort_bubble cost 18.666366 second
sort_insert cost 10.140411 second
sort_quick cost 11.785992000000004 second
==============10000 END================
sort_bubble cost 519.985739 second
sort_insert cost 310.2120050000001 second
Process finished with exit code 139 (interrupted by signal 11: SIGSEGV)
-------------------
Limit of 15200 is fine
recurse
add
Segmentation fault: 11
bogon:~ hbai$ python find_recursionlimit.py
'''
import time

def time_me(fn):
    def _wrapper(*args,**kwargs):
        start = time.clock()
        fn(*args,**kwargs)
        print("%s cost %s second" % (fn.__name__,time.clock()-start))
    return _wrapper

#@time_me 递归函数不适合使用装饰器
#复杂度  O(nlog(n))
def sort_quick(nums,left,right):
    if left >= right:
        return
    low = left
    high = right
    key = nums[left]
    while left < right:
        while left < right and nums[right]>= key:
            right-=1
        nums[left] = nums[right]
        while left < right and nums[left]<= key:
            left+=1
        nums[right] = nums[left]
    nums[right] = key
    sort_quick(nums,left,low-1)
    sort_quick(nums,low+1,high)
    return nums


#复杂度  O(n^2) : use j-1 to compare with i
#@time_me
def sort_insert(nums):
    for i in range(1,len(nums)):
        key = nums[i]
        j = i -1
        while j >=0:
            if nums[j] > key:
                nums[j+1],nums[j] = nums[j],nums[j+1]
            j-=1
    return nums


#@time_me
#need switch key[j],key[j+1] after cmp,#复杂度  O(n^2)
def sort_bubble(nums):
    for i in range(0,len(nums)-1):
        for j in range(0,len(nums)-i-1):
            if nums[j+1] < nums[j]:
                nums[j+1],nums[j] = nums[j], nums[j+1]
    return nums

# @time_me
# def test(x,y):
#     time.sleep(0.2)
#     return True
#
# test(1,2)

nums = [9,3,6,5,2,1]
print(sort_bubble(nums))

nums = [9,3,6,5,2,1]
print(sort_insert(nums))

nums = [9,3,6,5,2,1]
start = time.clock()
print(sort_quick(nums,0,len(nums)-1))
print("%s cost %s second" % ("sort_quick",time.clock()-start))
print("==============sample END================")
# import random
# nums = [int(10000*random.random()) for i in  range(10000)]
# sort_bubble(nums)
# sort_insert(nums)
# start = time.clock()
# import sys
# sys.setrecursionlimit(15000)
# sort_quick(nums,0,len(nums)-1)
# sys.setrecursionlimit(100)
# print("%s cost %s second" % ("sort_quick",time.clock()-start))
# print("==============10000 END================")


# nums = [int(13000*random.random()) for i in  range(13000)]
# sort_bubble(nums)
# sort_insert(nums)
# start = time.clock()
# import sys
# sys.setrecursionlimit(15000)
# sort_quick(nums,0,len(nums)-1)
# sys.setrecursionlimit(100)
# print("%s cost %s second" % ("sort_quick",time.clock()-start))
# print("==============13000 END================")

