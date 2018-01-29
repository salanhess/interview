import urllib
import httplib



def getHtml(url, fpath):
    try:
        retval = urllib.urlretrieve(url, fpath)
    except (IOError, httplib.InvalidURL) as e:
        retval = ('*** error: bad url "%s" : %s') % (url, e)
    return retval

# def getHtml2(url):
#     header = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'}
#     request = urllib2.Request(url,headers=header)  #init user request with url and headers
#     response = urllib2.urlopen(request)            #open url
#     text = response.read()
#     return text
#
# #get link with re
# def getUrls(html):
#     #pattern = re.compile('<a href="/story/(.*?)"',re.S)
#     pattern = re.compile('<a href="/story/(\d{0,9})"', re.S)
#     items = re.findall(pattern,html)
#     urls = ["http://daily.zhihu.com/story/"+str(item) for item in items]
#     return urls

#url = 'http://python.org'
url = 'ftp://ftp.python.org/pub/python/README'
fpath = 'my.txt'
print getHtml(url, fpath)
