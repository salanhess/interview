# coding=utf-8

# page = http://www.pythonchallenge.com/pc/def/linkedlist.php

page = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
loopMainpage = 'http://www.pythonchallenge.com/pc/def/'
firstpage = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

from urllib import request
import time
import re

# response = request.urlopen(page)
# html = response.read()
# soup = BeautifulSoup(html,'html.parser')
#
# # print(soup.prettify())
# link1 = loopMainpage+ soup.find('a').get('href')
# print(link1)
#
#
# response = request.urlopen(link1)
# html = response.read()
# print(firstpage + html[-5:].decode("utf-8"))

def looppage(page,num):
    response = request.urlopen(page+str(num))
    html = response.read()
    print(html.decode("utf-8"))
    pattern = re.compile('and the next nothing is (\d{1,10}).*?')
    target = re.findall(pattern,html.decode("utf-8"))
    print(page + target[0])
    return target[0]


# soup = BeautifulSoup(html,'html.parser')
#
# link2 = loopMainpage+ soup.text[-5:]
# print(link2)

# return_num = looppage(firstpage,'12345')
# i = 0
# while i < 401:
#     print('Index %s:' % i)
#     return_num = looppage(firstpage,return_num)
#     time.sleep(11)
#     i +=1
#
#
# #Index84: 8022
# Index 84+53=137 :82682
import random
return_num = looppage(firstpage,'82682')
i = 0
while i < 300:
    print('Index %s:' % i)
    return_num = looppage(firstpage,return_num)
    time.sleep(random.randint(5,10))
    i +=1


# Index 108:
# and the next nothing is 66831
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831
# Index 109:
# peak.html
