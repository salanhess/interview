#coding=utf-8

from selenium import webdriver
import time

#
browser = webdriver.Firefox()
browser.get("https://www.baidu.com")
print(browser.find_element_by_xpath("//*[contains(text(),'hao123')]"))
print(browser.find_elements_by_xpath("//*[@class='mnav' and @href='hao123']"))
time.sleep(5)
browser.quit()