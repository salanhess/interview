# coding=utf-8

# page = http://www.pythonchallenge.com/pc/def/linkedlist.php

page = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

import urllib2
import bs4 as BeautifulSoup

response = urllib2.urlopen(page)
html = response.read()
print html