#coding=utf-8
import urllib2,re
import requests
import HTMLParser

#modify C:\Python27\Lib\site-packages\sitecustomize.py . not suggest this way...
'''
1. Error. 
'ascii' codec can't decode byte 0xe5 in position 9: ordinal not in range(128)
http://stackoverflow.com/questions/3828723/why-should-we-not-use-sys-setdefaultencodingutf-8-in-a-py-script
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
 solution: According https://q.cnblogs.com/q/56729/, modify C:\Python27\Lib\site-packages  to add sys.setdefaultencoding('utf-8')
 
2. Note:NOT suggest to use this way, due to https://toutiao.io/posts/8618yn/preview
'''

#1.如何解决网络禁止爬虫:create request header
#2. 正则表达式获取超链接

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
    pattern = re.compile('<h1 class="headline-title">(.*?)</h1>',re.S)
    title = re.findall(pattern,html)
    #Chinese input:Method1 to display with item[0]
    print "*******************" + title[0] + "*******************"
    #Method2: use for in to display:
    # for i in items:
    #     print i

    #Note: re.S so need to match \n for each line
    pattern = re.compile('<div class="content">\\n<p>(.*?)</div>',re.S)
    #Filter func to remove tag
    items_withtag = re.findall(pattern,html)
    for item in items_withtag:
        for content in characterProcessing(item):
            print content

#Filter to remove tags in content: replace /sub  tag with space
#sub(tag,space,htmlsource):regularX search
#replace(target,source)

def characterProcessing(html):
    htmlParser = HTMLParser.HTMLParser()
    pattern = re.compile('<p>(.*?)</p>|<li>(.*?)</li>.*?',re.S)
    items= re.findall(pattern,html)
    result = []
    for index in items:
        if index != '':
            for content in index:
                tag = re.search('<.*?>',content)
                http = re.search('<.*?http.*?',content)
                html_tag = re.search('&',content)
                if html_tag:
                    content = htmlParser.unescape(content)
                if http:
                    continue
                elif tag:
                    pattern = re.compile('(.*?)<.*?>(.*?)</.*/>(.*)')
                    items = re.findall(pattern,content)
                    content_tags = ''
                    if len(items) > 0:
                        for item in items:
                            if len(item) > 0:
                                for item_s in item:
                                    content_tags = content_tags + item_s
                            else:
                                content_tags = content_tags + item
                        content_tags = re.sub('<.*?>','',content_tags)
                        result.append(content_tags)
                    else:
                        continue
                else:
                    result.append(content)
    return result


def main():
    url = "http://daily.zhihu.com/"
    html = getHtml(url)
    urls = getUrls(html)
    for url in urls:
        try:
            getContent(url)
        except Exception,e:
            print e

if __name__ == "__main__": #indentify file entry
    main()