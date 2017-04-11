#coding=utf-8
import urllib2,re
import requests
import HTMLParser
#1.如何解决网络禁止爬虫:create request header
#2. 正则表达式获取超链接
url = "http://daily.zhihu.com/"

#Chrome > F12 > network > F5 > name - headers > user request headers
def getHtml(url):
    header = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'}
    request = urllib2.Request(url,headers=header)  #init user request with url and headers
    response = urllib2.urlopen(request)            #open url
    text = response.read()
    return text

#get link with re
def getUrls(html):
    #pattern = re.compile('<a href="/story/(.*?)"',re.S)
    pattern = re.compile('<a href="/story/(\d{0,9})"', re.S)
    items = re.findall(pattern,html)
    urls = ["http://daily.zhihu.com/story/"+str(item) for item in items]
    return urls

def getContent(url):
    html = getHtml(url)
    pattern = re.compile('<span class="title">(.*?)</span></a>',re.S)
    items = re.findall(pattern,html)
    for i in items:
        print i

#TBD
for url in getUrls(getHtml(url)):
    try:
        getContent(url)
    except Exception,e:
        print e







