#coding=utf-8

#Study bs4 according https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
from bs4 import BeautifulSoup
from lxml import etree

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,"lxml")
#print soup.prettify()  #format for output

#get title, find_all by tag a, find by properties id="link1"
print soup.title
print soup.title.name
print soup.title.parent.name
print soup.find_all('a')
print soup.find(id="link1")

#find all link from TAG
#use TAG.attri to get ALL the method
for link in soup.find_all('a'):
    print link.attrs
    print link.get('href'),link.get('id')

print "============="
index = 0
for contents in soup.body.contents:
    print str(index) + str(type(contents)) + ": " + str(contents)
    index +=1
print "============="
#Regular Expression: to find TAG start with b
import re
for tag in soup.find_all(re.compile('^b')):
    print tag.name

print "============="
#Regular Expression: to get tag A/B
for tag in soup.find_all(['a','b']):
    print tag