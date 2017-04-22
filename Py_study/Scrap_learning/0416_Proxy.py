#coding=utf-8
# Proxy1: http://www.xicidaili.com/
# Proxy2: http://www.haoip.cc/index/2377233.htm
# proxy = {'http':'ip:port'}  # dictionary
# html = requests.get('https://www.baidu.com',proxies=proxy)

import urllib2
import random
from bs4 import BeautifulSoup
import time
import requests

class DownLoad():
    #Create constractor
    def __init__(self):
        url = 'http://www.xicidaili.com/'
        self.ip_list = []
        header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04'}
        request = urllib2.Request(url, headers=header)  # init user request with url and headers
        response = urllib2.urlopen(request)  # open url
        html = response.read()
        soup = BeautifulSoup(html, "lxml")
        for ips in soup.find_all('tr', attrs='odd'):
            ip = ips.find_all('td')[1].get_text().strip()
            port = ips.find_all('td')[2].get_text().strip()
            self.ip_list.append(ip+':'+port)

        print self.ip_list
        #refer to http://www.cnblogs.com/VAllen/articles/UserAgentList.html
        self.user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
        'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.9.168 Version/11.52',
        'Opera/9.80 (Windows NT 6.1; WOW64; U; en) Presto/2.10.229 Version/11.62',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
        'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
        ]
        #
        
    def get(self,url,proxy=None,timeout=10,num=5):
        print "Requesting...",url
        #random.choice from list
        UA = random.choice(self.user_agent_list)
        header = {"User-Agent": UA}
        if proxy == None:
            try:
                return requests.get(url, headers=header, timeout=timeout)
            except:
                if num > 0:
                    time.sleep(1)
                    print "Current Num is : %s" % num
                    return self.get(url,num = num -1)
                else:
                    print "Max %s times out,need use proxy..." % num
                    IP = ''.join(random.choice(self.ip_list))
                    proxy = {'http':IP}
                    return self.get(url,timeout=timeout,proxy=proxy,num=5)
        else:
            #Some proxy is invalid
            try:
                IP = ''.join(random.choice(self.ip_list))
                proxy = {'http': IP}
                print "Using proxy... "
                return requests.get(url,headers=header,proxies=proxy,timeout=timeout)
            except:
                if num > 0:
                    time.sleep(1)
                    #Use new IP
                    IP = ''.join(random.choice(self.ip_list))
                    proxy = {'http': IP}
                    return self.get(url, timeout=timeout,num=num - 1,proxy=proxy)

    def post(self):
        pass
#Setp2

xz = DownLoad()
xz.get('baidu.com')


