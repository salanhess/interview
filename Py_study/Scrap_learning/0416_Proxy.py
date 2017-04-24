#coding=utf-8
# Proxy1: http://www.xicidaili.com/
# Proxy2: http://www.haoip.cc/index/2377233.htm
# proxy = {'http':'ip:port'}  # dictionary
# html = requests.get('https://www.baidu.com',proxies=proxy)
#refer to http://www.cnblogs.com/wly923/archive/2013/05/07/3057122.html
'''
1. Get IP list from Proxy1: http://www.xicidaili.com/
2. Verify one by one at baidu.com
3. Store them on JSON file
4. If JSON file exsit/within 3 days ,keep and use
5. Else, re-scrap agains
'''
import urllib2
import random
from bs4 import BeautifulSoup
import time
import socket
import ssl
import json
import os

class DownLoad():
    #Create constractor
    def __init__(self):
        self.xiciurl = 'http://www.xicidaili.com/'
        self.check_url = "http://www.baidu.com"
        self.dumpJsonf = 'agent.conf'
        self.ip_list = []
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
        self.result = ""
        self.verifiedList = []

    def get_AgentList(self):
        header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04'}
        request = urllib2.Request(self.xiciurl, headers=header)  # init user request with url and headers
        response = urllib2.urlopen(request)  # open url
        html = response.read()
        soup = BeautifulSoup(html, "lxml")
        for ips in soup.find_all('tr', attrs='odd'):
            ip = ips.find_all('td')[1].get_text().strip()
            port = ips.find_all('td')[2].get_text().strip()
            type = ips.find_all('td')[5].get_text().strip()
            self.ip_list.append(ip + ':' + port + ":" + type)
        print self.ip_list

    def openpage(self):  # url为相对路径
        self.opener = urllib2.build_opener(urllib2.HTTPHandler)
        try:
            self.result = self.opener.open(self.check_url).read().decode("utf-8")
        except urllib2.HTTPError, ex:
            self.result = "openpage error: %s" % ex
            return False
        except urllib2.URLError,ex:
            self.result = "openpage error: %s" % ex
            return False
        except ssl.SSLError, ex:
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
                proxy_support = urllib2.ProxyHandler({'http': 'http://' + str(ip) + ':' + str(port)})
            else:
                proxy_support = urllib2.ProxyHandler({'https': 'https://' + str(ip) + ':' + str(port)})
            self.opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
            UA = random.choice(self.user_agent_list)
            header = ("User-Agent",UA)
            self.opener.addheaders.append(header) #refer to http://stackoverflow.com/questions/15455482/how-do-i-add-these-headers-to-my-python-urllib-opener
            urllib2.install_opener(self.opener) #install it globally so it can be used with urlopen.
            if self.openpage() == False:
                print "Proxy %s is invalid." % v_proxy
                continue
            print "Proxy %s is OK." % v_proxy
            time.sleep(random.randint(1,4))
            self.verifiedList.append(v_proxy)
            continue

    #refer to http://www.tuicool.com/articles/Q32Y3q
    def dump_to_jsonf(self):
        with open(self.dumpJsonf,'w') as f:
            json.dump(self.verifiedList, f, indent=4)

    def load_jsonf(self):
        with open(self.dumpJsonf, 'r') as f:
            self.verifiedList = json.load(f)

    # time convert refer to http://stackoverflow.com/questions/16994696/python-get-time-stamp-on-file-in-mm-dd-yyyy-format
    # cmp with current time,refer to http://stackoverflow.com/questions/415511/how-to-get-current-time-in-python
    #todo: Here is ONlY window, for other refer to http://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python
    def check_file_date(self):
        if not os.path.exists(self.dumpJsonf):
            return 0
        # ctime detail format refer to https://docs.python.org/2/library/time.html
        mtime = os.path.getmtime(self.dumpJsonf)
        l_modify = time.strftime("%Y%m%d", time.gmtime(mtime))
        nowtime = time.strftime("%Y%m%d", time.gmtime())
        #nowtime = time.strftime("%Y%m%d %H%M%S", time.gmtime())
        print "last modified: %s" % l_modify
        print "now time is %s" % nowtime
        return int(nowtime) - int(l_modify)

    def get(self, url):
        print "Try to access... %s via %s agents" % (url,len(self.verifiedList))
        proxy = random.choice(self.verifiedList)
        if proxy.split(':')[2] == 'http':
            proxy_support = urllib2.ProxyHandler({'http': 'http://' + str(proxy.split(':')[0]) + ':' + str(proxy.split(':')[1])})
        else:
            proxy_support = urllib2.ProxyHandler({'https': 'https://' + str(proxy.split(':')[0]) + ':' + str(proxy.split(':')[1])})
        self.opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
        UA = random.choice(self.user_agent_list)
        header = ("User-Agent", UA)
        self.opener.addheaders.append(header)
        urllib2.install_opener(self.opener)
        try:
            self.result = self.opener.open(url).read().decode("utf-8")
            return self.result
        except urllib2.URLError , ex:
            self.result = "openpage error: %s" % ex
            return False

    def post(self):
        pass


xz = DownLoad()
if xz.check_file_date() <=3: #within 3 days
    xz.load_jsonf()
    print xz.verifiedList
    html = xz.get(r'http://ip.chinaz.com/')
    soup = BeautifulSoup(html,'lxml')
    for i in soup.select('#rightinfo > dl > dd.fz24'):
        print "Current access IP is: %s" % i.get_text()
        if i.get_text() not in xz.verifiedList:
            print "Error!.This IP is still local PC's IP,not Agent!"

else:
    print "Need updated agent list..."
    xz.get_AgentList()
    xz.socket_verify()
    xz.dump_to_jsonf()
    html = xz.get(r'http://cn.bing.com/')
    soup = BeautifulSoup(html,'lxml')
    for i in soup.select('#rightinfo > dl > dd.fz24'):
        print i


