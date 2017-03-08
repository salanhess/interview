'''In general, the string handling all need space
There are three methods of treatment to deal with strings, lstrip, rstrip, strip.
x = '    hej   '
print '|', x.lstrip( ), '|', x.rstrip( ), '|', x.strip( ), '|'
| hej    |     hej | hej |'''

import string

str1 = "  pythonisgreat  "
#1.remove space in the left
print(str1.lstrip())
#2.remove space in the right
print(str1.rstrip())

#3. remove all the space
print (str1.strip())
#print(''.join(str1.split()))
