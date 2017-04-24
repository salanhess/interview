# coding=utf-8
# Proxy1: http://www.xicidaili.com/
# Proxy2: http://www.haoip.cc/index/2377233.htm
# proxy = {'http':'ip:port'}  # dictionary
# html = requests.get('https://www.baidu.com',proxies=proxy)

#Org doc refer to https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen

#Now refer to http://blog.csdn.net/vah101/article/details/6279423
#总结归纳 http://www.open-open.com/lib/view/open1375945149312.html
#To be done: with thread method later,refer to http://www.cnblogs.com/baizx/archive/2011/01/19/1939619.html
import urllib,ssl
import random
from bs4 import BeautifulSoup
import time
import socket


class DownLoad():
    # Create constractor
    def __init__(self):
        url = 'http://www.xicidaili.com/'
        self.check_url = "http://www.baidu.com"
        self.ip_list = []
        header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04'}
        req = urllib.request.Request(url,headers=header)  # init user request with url and headers
        response = urllib.request.urlopen(req)  # open url

        html = response.read()
        soup = BeautifulSoup(html, "lxml")
        for ips in soup.find_all('tr', attrs='odd'):
            ip = ips.find_all('td')[1].get_text().strip()
            port = ips.find_all('td')[2].get_text().strip()
            type = ips.find_all('td')[5].get_text().strip()
            self.ip_list.append(ip + ':' + port + ":" + type)
        self.ip_list = self.ip_list[:40]
        print(self.ip_list)
        # refer to http://www.cnblogs.com/VAllen/articles/UserAgentList.html
        self.user_agent_list = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.9.168 Version/11.52',
            'Opera/9.80 (Windows NT 6.1; WOW64; U; en) Presto/2.10.229 Version/11.62',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
            'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
        ]
        self.result = ""
        self.verifiedList = []
    def openpage(self):  # url为相对路径
        try:
            self.result = self.opener.open(self.check_url).read().decode("utf-8")
        except urllib.error.URLError as ex:
            self.result = "openpage error: %s" % ex
            return False
        except urllib.error.HTTPError as ex:
            self.result = "openpage error: %s" % ex
            return False
        except ssl.SSLError as ex:
            self.result = "openpage  error: %s" % ex
            return False
        return self.result.find("京ICP证030173号")

    socket.setdefaulttimeout(5)  # 5内没有打开web页面，就算超时
    def socket_verify(self):
        while 1:
            if len(self.ip_list)>0:
                v_proxy = self.ip_list.pop()
            else:
                return "Finished proxy check"
            ip = v_proxy.split(':')[0]
            port = v_proxy.split(':')[1]
            type = v_proxy.split(':')[2]
            if type == 'http':
                proxy_support = urllib.request.ProxyHandler({'http': 'http://' + str(ip) + ':' + str(port)})
            else:
                proxy_support = urllib.request.ProxyHandler({'https': 'https://' + str(ip) + ':' + str(port)})
            self.opener = urllib.request.build_opener(proxy_support, urllib.request.HTTPHandler)
            UA = random.choice(self.user_agent_list)
            header = ("User-Agent",UA)
            self.opener.addheaders.append(header) #refer to http://stackoverflow.com/questions/15455482/how-do-i-add-these-headers-to-my-python-urllib-opener
            urllib.request.install_opener(self.opener) #install it globally so it can be used with urlopen.
            if self.openpage() == False:
                print("Proxy %s is invalid." % v_proxy)
                continue
            print("Proxy %s is OK." % v_proxy)
            self.verifiedList.append(v_proxy)
            continue

    def get(self, url):
        print("Requesting...", url)
        proxy = random.choice(self.verifiedList)
        if proxy.split(':')[2] == 'http':
            proxy_support = urllib.request.ProxyHandler({'http': 'http://' + str(proxy.split(':')[0]) + ':' + str(proxy.split(':')[1])})
        else:
            proxy_support = urllib.request.ProxyHandler({'https': 'https://' + str(proxy.split(':')[0]) + ':' + str(proxy.split(':')[1])})
        self.opener = urllib.request.build_opener(proxy_support, urllib.request.HTTPHandler)
        UA = random.choice(self.user_agent_list)
        header = ("User-Agent", UA)
        self.opener.addheaders.append(header)
        urllib.request.install_opener(self.opener)
        try:
            self.result = self.opener.open(url).read().decode("utf-8")
        except urllib.error.URLError as ex:
            self.result = "openpage error: %s" % ex
            return False

    def post(self):
        pass

# url = 'http://www.xicidaili.com/'
# header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04'}
# req = request.Request(url,headers=header)  # init user request with url and headers
# response = request.urlopen(req)
# the_page = response.read()
#print(the_page.decode("utf8"))

# Setp2
#
xz = DownLoad()
# xz.get('baidu.com')
xz.socket_verify()
print(xz.verifiedList)

print(xz.get(r'http://cn.bing.com/'))






