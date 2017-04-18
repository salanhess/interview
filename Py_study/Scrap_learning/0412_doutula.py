coding='utf-8'
#Target: multi-thread to scap doutu websit
import urllib2
from lxml import etree
from bs4 import BeautifulSoup
import requests
import threading
import os
# [Line23]Use soup.find_all('a',class_='list-group-item') to get item,then use 'href'index to get link
# [Line34]Use soup xpath to get box, then xpath to the target, use @ if want get properties

url = r'https://www.doutula.com/article/list/?page=1'
def get_Html(url):
    header = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'}
    request = urllib2.Request(url)  #init user request with url and headers: ,headers=header
    response = urllib2.urlopen(request)            #open url
    text = response.read()
    return text

#get url from source page
def get_img_html(html):
    soup = BeautifulSoup(html,'lxml')
    all_a = soup.find_all('a',class_='list-group-item')
    href_list = []
    for i in all_a:
        href_list.append(i['href'])
    return href_list

#get pic,call multi-thread method to download pics
def get_img(html):
    soup = etree.HTML(html) #Init print source code, fix tag issue
    items = soup.xpath('//div[@class="artile_des"]')  #parse page, get the property box
    for item in items:
        imgurl_list = item.xpath('table/tbody/tr/td/a/img/@onerror')  # get box, then xpath to the target, use @ if want get properties
        #return imgurl_list
        start_save_img(imgurl_list)

def save_img(img_url):
    img_url = img_url.split('=')[1][1:-2].replace('jp','jpg')
    print u'Downloading http://'+ img_url
    imgName = img_url.split('/')[-1]
    img_content = requests.get('http:'+img_url).content
    with open('doutu/%s.jpg' % imgName,'wb') as f:
        f.write(img_content)

#Use multi-thread to download
def start_save_img(imgurl_list):
    for i in imgurl_list:
        th = threading.Thread(target=save_img,args=(i,))  # Don't forget , in i !!
        th.start()

def main():
    start_url = 'https://www.doutula.com/article/list/?page='
    if os.path.getsize('doutu') == 0:
        print "=================Not download yet,start multithread downloading================="
        for i in range(1,3):
            start_html = get_Html(start_url+str(i))
            print "processing " + start_url+str(i)
            href_list = get_img_html(start_html)
            for href in href_list:
                img_html = get_Html(href)
                get_img(img_html)
                #save_img(img_url[-1])
    else:
        print "===========Already download before,pls check C:\Tools\interview\Py_study\Scrap_learning\doutu========"


if __name__ == '__main__':
    main()