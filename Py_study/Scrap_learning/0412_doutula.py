coding='utf-8'
import urllib2

url = r'https://www.doutula.com/article/list/?page=1'
def getHtml(url):
    header = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'}
    request = urllib2.Request(url)  #init user request with url and headers
    response = urllib2.urlopen(request)            #open url
    text = response.read()
    return text

print getHtml(url)