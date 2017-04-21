#coding=utf-8
#1. Study how to get text by attrs
# <span class="body"> xxx  </span>  ==> tag.find(attrs="body")
#<div class="content">  ==>  tag.find(attrs="content").get_text()[1:]
# <div id="qiushi_tag_118914192" class="article block untagged mb15">  ==>  soup.find_all(attrs="article block untagged mb15"), tag['id']
#2. Study to use raw_input control

import urllib2
from bs4 import BeautifulSoup

def getHtml(url):
    header = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'}
    request = urllib2.Request(url,headers=header)  #init user request with url and headers
    response = urllib2.urlopen(request)            #open url
    text = response.read()
    return text

#get url from source page
def get_tag_html(html):
    soup = BeautifulSoup(html,'lxml')
    all_tag = soup.find_all(attrs="article block untagged mb15")
    Num = 1
    for tag in all_tag:
        #Get article
        full_content = tag.find(attrs="content").get_text()[1:]
        if len(full_content) > 50:
            print str(Num) + ": " + full_content[:50]
            print full_content[51:]
        else:
            print  str(Num) + ": " + full_content

        #Get comments
        href = 'http://www.qiushibaike.com/article/' + tag['id'].strip()[-9:]
        commpage = getHtml(href)
        commentFloor =1
        soup = BeautifulSoup(commpage, 'lxml')
        for comments in soup.find_all(attrs="body"): #
            print "   ",commentFloor," reply ",comments.get_text()
            commentFloor +=1
        Num +=1

articleUrl = "http://www.qiushibaike.com/textnew/page/%d"
commentUrl = "http://www.qiushibaike.com/article/%s"
page = 0

while True:
    raw = raw_input("Print Enter or exit,pls make your choice:")
    if raw == "exit":
        break
    page += 1
    html = getHtml(articleUrl % page)
    get_tag_html(html)