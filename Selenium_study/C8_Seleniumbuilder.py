#coding=utf-8

from selenium import webdriver
import time

#Install Selenium builder from FF add-on
#Open it from FF >Tools > Web Developer , Input UrlLink and then start record.
#Add sleep time in each operation

browser = webdriver.Firefox()
browser.get("https://www.baidu.com")

browser.find_element_by_name("tj_trnews").click()
time.sleep(3)
browser.find_element_by_id("ww").click()
time.sleep(3)
browser.find_element_by_xpath("//div[@id='channel-all']//a[.='娱乐']").click()
time.sleep(3)
browser.find_elements_by_link_text("与刘嘉玲同台 关之琳：早已放下了")[0].click()

time.sleep(5)
browser.quit()
