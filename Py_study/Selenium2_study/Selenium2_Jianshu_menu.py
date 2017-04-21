#coding=utf-8

#refer to http://www.cnblogs.com/haigege/p/5492177.html
#Step1: scroll and generate Markdown format Menu
#Todo Step2:Use selelium login Jiansh and updated Menu automatically

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import urllib2,os,time

def scroll_top(driver):
    if driver.name == "chrome":
        js = "var q=document.body.scrollTop=0"
    else:
        js = "var q=document.documentElement.scrollTop=0"
    return driver.execute_script(js)

# 拉到底部
def scroll_foot(driver):
    if driver.name == "chrome":
        js = "var q=document.body.scrollTop=100000"
    else:
        js = "var q=document.documentElement.scrollTop=100000"
    return driver.execute_script(js)

def write_text(filename, info):
    """
    :param info: 要写入txt的文本内容
    :return: none
    """
    # 创建/打开info.txt文件，并写入内容
    with open(filename, 'a+') as fp:
        fp.write(info.encode('utf-8'))
        fp.write('\n'.encode('utf-8'))
        fp.write('\n'.encode('utf-8'))

def sroll_multi(driver,times=5,loopsleep=2):
    #40 titles about 3 times
    for i in range(times):
        time.sleep(loopsleep)
        print "Scroll foot %s time..." % i
        scroll_foot(driver)
    time.sleep(loopsleep)

#Note: titles is titles_WebElement type object
def write_menu(filename,titles):
    with open(filename, 'w') as fp:
        pass
    for title in titles:
        if r'目录' not in title.text:
            print "[" + title.text + "](" + title.get_attribute("href") + ")"
            t = title.text.encode('utf-8')
            t = title.text.replace(":", "：")
            t = title.text.replace("|", "丨")
            t = title.text.decode('utf-8')
            write_text(filename, "[" + t + "](" + title.get_attribute("href") + ")")
            #assert type(title) == "WebElement"
            #print type(title)

def main(url):
    # eg. <a class="title" href="/p/6f543f43aaec" target="_blank">《往事难如烟8》曾经的俱乐部（三）开大会</a>
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    # driver.maximize_window()
    driver.get(url)
    sroll_multi(driver)
    titles = driver.find_elements_by_xpath('.//a[@class="title"]|.//a[target="_blank"]')
    write_menu(filename, titles)

if __name__ == '__main__':
    # HengHeng's link
    # url = 'http://www.jianshu.com/u/c0238b72b6f9'
    # UncleFan's link
    url = 'http://www.jianshu.com/u/73632348f37a'
    filename = r'info.txt'
    main(url)