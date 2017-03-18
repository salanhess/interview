#coding=utf-8

from selenium import webdriver
import time

#
browser = webdriver.Firefox()
browser.get("https://www.baidu.com")
browser.find_elements_by_xpath("//*[@class='mnav' and @href='http://www.hao123.com']")[0].click()

time.sleep(5)
browser.quit()