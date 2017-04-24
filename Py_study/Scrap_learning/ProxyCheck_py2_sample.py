#!/usr/bin/env <a href="http://lib.csdn.net/base/python" class='replace_word' title="Python知识库" target='_blank' style='color:#df3434; font-weight:bold;'>Python</a>
# coding=utf-8
import urllib
import http.cookiejar
import re
import socket


class OpenUrl:
    def __init__(self):
        self.result = ""

    def openpage(self):  # url为相对路径
        try:
            url = "http://www.baidu.com"

            self.result = self.opener.open(url).read().decode("gb2312")
        except urllib.error.HTTPError as ex:
            self.mute.release()
            self.result = "openpage error: %s" % ex
            return False
        except ssl.SSLError as ex:
            self.mute.release()
            self.result = "openage  error: %s" % ex
            return False

        return self.result.find("京ICP证030173号")

    def getHtmlTdInfo(self, context):
        result = []
        p = re.compile("/d{1,3}/./d{1,3}/./d{1,3}/./d{1,3}[/w|/W]+?<td width=/"60 / ">/d{2,4}")
        ret = p.findall(str(context))

        if ret is None:
            return None

        for x in ret:
            element = []
            q = re.compile("^(/d{1,3}/./d{1,3}/./d{1,3}/./d{1,3})[/w|/W]+?(/d{2,4})$")
            subRet = q.search(x);
            if subRet == None:
                continue
            element.append(subRet.group(1))
            element.append(subRet.group(2))
            result.append(element)
        return result

    def getAgencyIP(self, url=""):
        socket.setdefaulttimeout(20)  # 20秒内没有打开web页面，就算超时

        url = "http://5uproxy<a href="
        http: // lib.csdn.net / base / dotnet
        " class='replace_word' title=".NET知识库
        " target='_blank' style='color:#df3434; font-weight:bold;'>.Net</a>/http_fast.html"  # 获取最新代理服务器
        self.result = str(urllib.request.urlopen(url).read())
        if self.result == None:
            return
        AgencyIP = self.getHtmlTdInfo(self.result)
        print(len(AgencyIP))

        url = "http://5uproxy.net/http_anonymous.html"  # 获取匿名访问代理服务器
        self.result = str(urllib.request.urlopen(url).read())
        if self.result == None:
            return
        AgencyIP += self.getHtmlTdInfo(self.result)
        print(len(AgencyIP))

        url = "http://5uproxy.net/http_non_anonymous.html"  # 获取透明访问代理服务器
        self.result = str(urllib.request.urlopen(url).read())
        if self.result == None:
            return
        AgencyIP += self.getHtmlTdInfo(self.result)
        print(len(AgencyIP))

        socket.setdefaulttimeout(5)  # 5内没有打开web页面，就算超时
        if len(AgencyIP) == 0:
            print("获取代理服务器失败")
            return
        for x in AgencyIP:
            if x[0] == "":
                continue
            try:
                proxy_support = urllib.request.ProxyHandler({'http': 'http://' + str(x[0]) + ':' + str(x[1])})
                self.opener = urllib.request.build_opener(proxy_support, urllib.request.HTTPHandler)
                urllib.request.install_opener(self.opener)
                if self.openpage() == False:
                    x[0] = ""
                    x[1] = ""
                    continue
                print("有效的代理服务器" + str(x[0]) + ":" + str(x[1]))
                print("等待2秒")
                time.sleep(2)
            except:
                continue


if __name__ == "__main__":
    test = OpenUrl()
    test.getAgencyIP()
