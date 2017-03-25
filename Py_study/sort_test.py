#coding=utf-8

def sort_insert(nums):
    for i in range(1,len(nums)):
        key = nums[i]
        j = i -1
        while j >= 0:
            if nums[j] > key:
                nums[j+1],nums[j] = nums[j],key
            j -=1
    return  nums

def sort_bubble(nums):
    for i in range(0,len(nums)-1):
        for j in range(0,len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

nums = [9,3,6,5,2,1]

print(sort_bubble(nums))
print(sort_insert(nums))