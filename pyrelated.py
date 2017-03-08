import string

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
