#coding=utf-8
import urllib2,re
import requests
import HTMLParser

#目前的问题： 只爬取了最上面的文章链接，手工拖拽滚动条获取的标题内容无法直接获取到，网上建议用selenium来解决
#task1: use selenium scroll to the end,then get.

def getHtml(url):
    header = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'}
    request = urllib2.Request(url,headers=header)  #init user request with url and headers
    response = urllib2.urlopen(request)            #open url
    text = response.read()
    return text

def getTitleLink(html):
    pattern1 = re.compile('<a class="title" target="_blank" href="/p/(\w{0,12})"', re.S)
    links = re.findall(pattern1,html)
    urls = ["www.jianshu.com/p/"+str(link) for link in links]

    pattern2 = re.compile('<a class="title" target="_blank" href="/p/.*?">(.*?)</a>',re.S)
    titles = re.findall(pattern2,html)
    for title,url in zip(titles,urls):
        if r'目录' not in title:
            print "["+title+"](" + url + ")"
    #return urls


#duduma test menu
#url = 'http://www.jianshu.com/u/696b477cccd9'

#BaBa's menu
url = 'http://www.jianshu.com/u/c0238b72b6f9'
html = getHtml(url)
getTitleLink(html)