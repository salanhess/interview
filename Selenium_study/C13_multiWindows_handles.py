#coding=utf-8

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
for a in s:
    print(driver.title)
    a.click()
    driver.switch_to.active_element
    print(driver.title)
    print(a.text)
    all_h = driver.window_handles
    print(all_h)
#
# print(driver.title)
# s[3].click()
# time.sleep(2)
# driver.switch_to.active_element
# print(driver.title)
#
# for a in s:
#     a.click()
#     time.sleep(4)
#
#     text = a.text
#     all_h = driver.window_handles
#     print(all_h)