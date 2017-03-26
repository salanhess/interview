#coding=utf-8

#冒泡排序 插入排序， 快速排序  等实现 ，需要能够讲述其复杂度

#冒泡排序
'''
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
时间复杂度 O(n^2)
'''
def bubble_sort(slist):
    print("=====bubble_sort====")
    for i in range(len(slist)-1):
        #print("Before %s Time sort: %s" % (i,slist))
        for j in range(len(slist)-i-1):
            if slist[j] > slist[j+1]:
                slist[j],slist[j+1] = slist[j+1],slist[j]
            #print("After j[%s] Time sort: %s" % (j, slist))
    return (slist)

#插入排序

'''
插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，
算法适用于少量数据的排序，时间复杂度为O(n^2)。
是稳定的排序方法。插入算法把要排序的数组分成两部分：
第一部分包含了这个数组的所有元素，但将待插入元素除外（让数组多一个空间才有插入的位置），
而第二部分就只包含这一个元素（即待插入元素）。在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中。
时间复杂度 O(n^2)
'''


def insert_sort(nums):
    #print("=====insert_sort====\nOriginal list is %s" % nums)
    print("=====insert_sort====")
    for i in range(1,len(nums)):
        key = nums[i]
        #print("In [%d],Current key is %d\nBefore sort list is %s" % (i,key,nums))
        j = i-1
        while j >=0:
            if nums[j] > key:
                nums[j+1],nums[j] = nums[j],key
            j -=1
        #print("Now list is %s" % nums)
    return (nums)


#快速排序
'''
通过一趟排序将要排序的数据分割成独立的两部分，
其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，
整个排序过程可以递归进行，以此达到整个数据变成有序序列。
不稳定，时间复杂度 最理想 O(nlogn) 最差时间O(n^2)
'''
#这个算法必须要清楚，参考 http://blog.csdn.net/morewindows/article/details/6684558
def quick_sort(lists, left, right):
    #print("=====quick_sort====")
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    #print("Original list is: %s,left is %s, right is %s " % (lists, left, right))
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    #print("After sort with Key[%s], current list is %s" % (key,lists))
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists



l1 = [9,8,6,4,3,2,1]
print(bubble_sort(l1))
print(insert_sort(l1))
l1 = [4,8,6,9,1,2,3]
print(quick_sort(l1,0,len(l1)-1))

import random


# '''
# 希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
# 希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。
# 希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
# 随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止
# #但是这种排序算法不是太完善，所有不在此进行详细的讨论和学习，参考 https://www.zhihu.com/question/39288741
# '''
# #todo I don't know why the group is float after convert to int type already :(
# def shell_sort(lists):
#     print("=====insert_sort====\nOriginal list is %s" % lists)
#     # 希尔排序
#     count = len(lists)
#     step = 2
#     group = int(count / step)
#     print("group is %s ,type is %s " % (group,type(group)))
#     while group > 0:
#         for i in range(0, int(group)):
#             j = i + int(group)
#             print("Index[%s]" % i)
#             while j < count:
#                 k = j - int(group)
#                 key = lists[j]
#                 while k >= 0:
#                     if lists[k] > key:
#                         lists[k + int(group)] = lists[k]
#                         lists[k] = key
#                     k -= int(group)
#                 j += int(group)
#             print(lists)
#         group /= step
#     print(lists)
#shell_sort(l1)
