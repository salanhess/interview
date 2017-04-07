#coding=utf-8
#Study Scrap
#suggest:
# 2. Ask question with QQ:2603044582  ，锁威老师2号
'''
下载python中文社区教程:从网页采集数据
1. 获取页面源码
2. 找到标题内容所对应的标签
3. 把标题所对应的内容放一起
4. 如何打印文章内容
5. 打印标题
6. 写入文件：标题为名字
'''

from urllib import request
from bs4 import BeautifulSoup

url = "http://www.pythontab.com/html/pythonhexinbiancheng/index.html"
url_list = [url] #link to multi-pages
url_list.extend(["http://www.pythontab.com/html/pythonhexinbiancheng/" + str(i) + ".html" for i in range(2,3)])  #2,19

source_list = [] #title and context
#print(url_list)
for j in url_list:
    html = request.urlopen(j).read()  # open and get page source code
    soup = BeautifulSoup(html,'html.parser') # html.parser is internal
    titles = soup.select('#catlist > li > a') #css selector , '#' means id tag
    #get context, get tag a and href link (This way is only for static page)
    links = soup.select('#catlist > li > a')
    for title,link in zip(titles,links):  #Use zip func to generate dictionary
        data = {
            "title": title.get_text(),  #get title text
            "link": link.get('href')    #get href link
        }
        source_list.append(data)

#Get context
for l in source_list:
    html = request.urlopen(l["link"]).read()
    #soup = BeautifulSoup(html, 'lxml')
    soup = BeautifulSoup(html, 'html.parser')
    text_p = soup.select('div.content > p') # get text from tag p: class use . ; id use #
    text = []
    for t in text_p:
        text.append(t.get_text().encode('utf-8')) # Or write with UTF format: outfile.write(bytes(plaintext, 'UTF-8'))
    title_text = l['title'].replace('*','').replace('/','or').replace('"',' ').replace('?','wenhao').replace(':',' ')
    #print(title_text)
    with open('study/%s.txt' % title_text, 'wb') as f:
        for a in text:
            f.write(a)