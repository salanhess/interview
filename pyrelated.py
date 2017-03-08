import string

#<Old Wang Based Python>
str1 = "  pythonisgreat  "
#1.remove space in the left
print(str1.lstrip())
#2.remove space in the right
print(str1.rstrip())

#3. remove all the space
print (str1.strip())
#print(''.join(str1.split()))

#4.upper chars
print(str1.upper().strip())

#5.lower chars
str2="AbC"
print(str2.lower())

#6.check var type:str/list
print(type(str2))
print(type(str1.split()))

#Chapter5
info = 'abdd'
#replace d with c,count=1 means ONLY replace once
print(info.replace('d','c',1))

#convert string to int then can add
a = '1'
b = 2
print(int(a)+b)
