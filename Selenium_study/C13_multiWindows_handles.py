#coding=utf-8
# refer to http://www.cnblogs.com/yoyoketang/p/6128611.html
#todo loop with error :    raise exception_class(message, screen, stacktrace)
#selenium.common.exceptions.StaleElementReferenceException: Message: The element reference is stale. Either the element is no longer attached to the DOM or the page has been refreshed.
#About error because in current version of FF, new link opened in previous window,so can't switch back

from selenium import webdriver
import time

a = [1,2,3,4]
b = ['a','b','c']
for i,j in zip(a,b):
    print(i,j)

# coding:utf-8

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://news.baidu.com/")
driver.implicitly_wait(10)

# 获取当前窗口句柄
h = driver.current_window_handle
# 定位网页、贴吧等链接
s = driver.find_elements_by_xpath(".//*[@id='header-link-wrapper']/li")
r = [u"网页", u"新闻",u"贴吧", u"知道",  u"音乐", u"图片", u"视频", u"地图", u"文库"]

for a, b in zip(s, r):
    a.click()
    #text = a.text
    time.sleep(2)
    all_h = driver.window_handles
    # 循环判断是否与首页句柄相等
    for i in all_h:
        if i != h:
            driver.switch_to.window(i)
            time.sleep(1)
    print(driver.title)
    if b in driver.title:
        print(u"页面打开正常")
    else:
        print(u"页面测试失败")
    driver.close()                       # 关闭当前页面
    driver.switch_to.window(h)           # 切回句柄到首页
driver.quit()