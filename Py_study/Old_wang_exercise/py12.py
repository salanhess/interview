#coding=utf-8
#dic normal operation

ainfo = {'ab':'liming','ac':20}
#method1 to add key
# ainfo['sex']='man'
# ainfo['age']=20
# print(ainfo)

#Method2 to add key: update
ainfo.update({'sex':'man','age':20})
print(ainfo)

del ainfo['sex']
del ainfo['age']
print(ainfo.keys())
print(ainfo.values())
#Two methods to get value from key: del and pop
print(ainfo['ab'])
print(ainfo.get('ab'))

#Two method to del key 'ac'
#del ainfo['ac']
ainfo.pop('ac')
print(ainfo)
print("######################################")
#init dict
info = {'name':'lilei', 'age': 20}
#info =dict(name='cary',age=33)
print(info)

#add dict element
info['sex']='male'
print(info)

#modify dict element
info['sex']='female'
print(info)

#updated dict element
info.update({'name':'Cary', 'age':40, 'sex':'male'})
print(info)

#del pop clear
del info['sex']
print(info)

info.pop('age')
print(info)

info.clear()
print(info)

#in ONLY check key,not check value
info =dict(name='cary',age=33)
print('age' in info)
print(33 in info)

#search value in keys/values
print(info.keys())
print(info.values())
print(33 in info.values())

#get value from key
#print(info['age'])
print(info.get('name'))
print(info.get('age'))
