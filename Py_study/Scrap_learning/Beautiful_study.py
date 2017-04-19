#coding=utf-8

#Study bs4 according https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
#Study xPath, refer to http://www.w3school.com.cn/xpath/xpath_syntax.asp,according sample page: BS4_sample.html

# For ZH coding,refer to https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#unicode-dammit
# If have ZH strange character,use UnicodeDammit to convert it.
#Only lxml > etree support Xpath, refer to line30.
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
print soup.prettify()  #format for output
print "=====5555555555555========"
#get title, find_all by tag a, find by properties id="link1"
print soup.title,soup.title.name,soup.title.parent.name
print soup.find_all('a'), soup.find(id="link1")

print "=====Only lxml > etree support Xpath========"
from lxml import etree
soup_etree = etree.HTML(html_doc)
for item in soup_etree.xpath('//a'):
    print item.tag,item.attrib

#Open file:///C:/Tools/interview/Py_study/Scrap_learning/BS4_sample.html,use Firepath to eval
## .//p/a[@id='link1']|.//p/a[@id='link2']
print "=====Xpath========"
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

print "============="
#find_parents check
a_string = soup.find(text="Lacie")
print a_string
print a_string.find_parents("a")
print a_string.find_parents("p")

#Following not work
#print a_string.find_parents("p",class='story')

print "============="
#CSS selecter
print soup.select("body a")

#CSS tag > tag select
print soup.select("p > a")

#CSS by class name
print soup.select(".sister")

#CSS by property
print soup.select('a[href="http://example.com/lacie"]')

#BS will auto check feed html coding type
print soup.original_encoding

#You can specify the output code type,default is UTF-8
#print(soup.prettify("latin-1"))  #print(soup.prettify("utf-8"))

#Alternate, you can specify the coding type
print soup.p.encode("utf-8")


