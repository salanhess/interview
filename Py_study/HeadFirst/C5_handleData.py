#coding=utf-8
#step1: with open file
# 2. convert to list with , split
# 3. repace - : , return sorted string

def sanitize(time_string):
    time_string = time_string.replace('-','.').replace(':','.')
    mins,secs = time_string.split('.')
    return(mins + '.' + secs)

tstr = '2-18'
print(sanitize(tstr))

def get_coatch_data(fname):
    try:
        with open(fname) as jaf:
            data = jaf.readline()
        tmp = data.strip().split(',')
        return {"Name":tmp.pop(0),"DOB":tmp.pop(0),"Times":sorted(set([sanitize(i) for i in tmp]))[0:3]}
    except Exception as Err:
        print(Err)
        return None

james = get_coatch_data('james.txt')
print(james)
#常规方式
# clean_james = []
# for line in james:
#     clean_james.append(sanitize(line))
#
# print(sorted(clean_james))

#采用列表推导式的方式
# james = sorted([sanitize(j) for j in james])

#List 常规方式去除重复元素
# unique_james = []
# for i in range(len(james)):
#     if james[i] not in unique_james:
#         unique_james.append(james[i])
# print(unique_james[:3])

#采用工厂函数set首先去除重复元素，然后在sorted排序并取值
# print(sorted(set([sanitize(j) for j in james]))[0:3])
