#coding=utf-8
from urllib import request
import re
import json
import time

#基本思路：使用regx处理request方式获取的页面context，然后将相关信息采用json dump/load的方式存取和读取，最后使用send_SMS发送到自己手机


#http://www.bjjtgl.gov.cn/zhuanti/10weihao/index.html
#todo refer to http://www.cnblogs.com/Lands-ljk/p/5467236.html ,and multi-thread etc...
#todo ,method1 not work due to http://cuiqingcai.com/990.html
#python 正则表达式在线调试工具： http://www.pyregex.com/
#正则表达式参考 http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html


#This method can't get page, due to not set headers as following
# response = request.urlopen(r'http://baidu.com/') # <http.client.HTTPResponse object at 0x00000000048BC908> HTTPResponse类型
# page = response.read()
# page = page.decode('utf-8')
#
# print(page)


#url = r'http://www.lagou.com/zhaopin/Python/?labelWords=label'
url = r'http://www.bjjtgl.gov.cn/zhuanti/10weihao/index.html'
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
    'Connection': 'keep-alive'
}
req = request.Request(url, headers=headers)
page = request.urlopen(req).read()
content = page.decode('utf-8')
#print(content)

# #<td width="356" class="hui14 bk">  (Xianhao info)  <td width="194"  class="bk" > ... </td>
pattern = re.compile('.*?\sclass="hui14\sbk">&\w{4};&\w{4};(.*)<br\s/>&\w{4};&\w{4};(.*)<br\s/>.*&\w{4};&\w{4};(.*)<br\s/>',re.S)
#
# #<div class=”article block untagged mb15″ id=”…”>…</div>
# #pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
# #                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
items = re.findall(pattern,content)
print(items[0])
l1 = str(items[0]).split("&nbsp;&nbsp;")
for i in range(len(l1)):
    print("%d: %s" % (i,l1[i]))
    # if i == 5 or i ==6:
    #     print(l1[i])

#dump/load with File mode
with open(r'Save_json.txt','w') as fp:
    json.dump(l1[5]+l1[6],fp)

print("===========")
newlist = []
with open(r'Save_json.txt','r') as fp:
    hehe = json.load(fp)
    for sub in hehe.split('<br />\\r\\n'):
        newlist.append(sub.strip())

print("====333=======")

def check_min_max(target, slist):
    min = ''
    max = ''
    flag = 0
    for item in slist:
        flag +=1
        if flag <= 3:
            if len(item) == 4:
                min += item
            else:
                min +=item.zfill(2)
        if flag > 3:
            if len(item) == 4:
                max += item
            else:
                max +=item.zfill(2)
    return min,max,int(min)<target<int(max)


from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "ACe7eed79c6ca7bfb83ff1b50cd19c95cb"
# Your Auth Token from twilio.com/console
auth_token  = "c046c152c3dc7238e1e764a98d25bbe9"
def send_SMS(msg):
    client = Client(account_sid, auth_token)
    message = client.api.account.messages.create(
        to="+8613811077547",
        from_="+12018200958",
        body=msg)
    print(message.sid)

'''
0:(一)自2017年4月10日至2017年7月9日，星期一至星期五限行机动车车牌尾号分别为：3和8、4和9、5和0、1和6、2和7；
1:(二)自2017年7月10日至2017年10月8日，星期一至星期五限行机动车车牌尾号分别为：2和7、3和8、4和9、5和0、1和6；
'''
p = re.compile('自(\d{4})年(\d{1,2})月(\d{1,2})日至(\d{4})年(\d{1,2})月(\d{1,2})日')

ISOTIMEFORMAT = '%Y%m%d'
print(time.strftime( ISOTIMEFORMAT, time.gmtime( time.time() ) ))

targettime = 20170420
flag = False
for i in range(2):
    items = re.findall(p,newlist[i])
    if check_min_max(targettime,items[0])[2]:
        flag = True
        #send_SMS(str(check_min_max(targettime,items[0])))
        print(str(check_min_max(targettime,items[0])))

#return val is tuple list

#print(check_min_max(20180420,items[0]))
