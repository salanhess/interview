#coding=utf-8
from urllib import request
from bs4 import BeautifulSoup


#基本思路：使用XXX方式获取的页面context
# 参考 http://cuiqingcai.com/1319.html
# https://www.crummy.com/software/BeautifulSoup/
#http://www.bjjtgl.gov.cn/zhuanti/10weihao/index.html

#Note: according http://stackoverflow.com/questions/34475051/need-to-install-urllib2-for-python-3-5-1
'''
urllib2 is the name of the library included in Python 2.
 You can use the urllib.request library included with Python 3, instead.
The urllib.request library works the same way urllib2 works in Python 2.
Because it is already included you don't need to install it.
'''

url = r'http://www.bjjtgl.gov.cn/zhuanti/10weihao/index.html'
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
    'Connection': 'keep-alive'
}
req = request.Request(url, headers=headers)
page = request.urlopen(req).read()
content = page.decode('utf-8')
#print(content)

soup = BeautifulSoup(content,"lxml")
""
#print(soup.prettify())
limitInfo = ''
td_list = soup.find_all('td')
for i in range(len(td_list)):
    if i == 2:
        #print("%d: %s" % (i,td_list[i]))
        limitInfo = td_list[i]

print(limitInfo)
print("=============")
print(type(limitInfo))
print(str(limitInfo).split("<br/>"))

# from lxml import etree
#
# print("=============")
# import urllib.request
# from lxml import etree
#
# selector = etree.HTML(content)
# links = selector.xpath('html/body/div[1]/table[1]/tbody/tr[2]/td[2]/text()')
# for link in links:
#     print(link)