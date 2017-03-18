#coding=utf-8

from selenium import webdriver
import time
#refer to http://www.cnblogs.com/yoyoketang/p/6128580.html for more info

#Use Firebug > FirePath to help check

browser = webdriver.Firefox()
browser.get("https://www.baidu.com")
#search according css multi properties
browser.find_element_by_css_selector('.mnav[name="tj_trmap"]').click()
time.sleep(5)
browser.quit()
