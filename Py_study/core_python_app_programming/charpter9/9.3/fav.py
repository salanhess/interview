from urllib2 import urlopen
from cStringIO import StringIO
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup, SoupStrainer

def output(x):
    print '\n'.join(sorted(set(x)))


def fasterBS(url,f):
    output(urljoin(url, x['href']) for x in BeautifulSoup(f,parseOnlyThese=SoupStrainer('a')))

# url = 'http://python.org'
url = 'http://www.baidu.com'
#url =r'C:\Users\test\PycharmProjects\MyInterview\Py_study\core_python_app_programming\charpter9\9.1\bookmarks_2018_1_30.html'
f = urlopen(url)
data = StringIO(f.read())
f.close()
print data
fasterBS(url, data)
data.seek(0)
print data
