#coding=utf-8
#refer to http://www.cnblogs.com/yoyoketang/p/6128607.html
#send_keys(Keys.ENTER), .text to get content
#TBD: drag_and_drop not work ,todo

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.implicitly_wait(5)
driver.find_element_by_xpath(".//*[@id='kw']").send_keys("test")
driver.find_element_by_xpath(".//*[@id='su']").send_keys(Keys.ENTER)
driver.implicitly_wait(5)
print(driver.find_element_by_xpath(".//*[@id='1']/div[1]/div[1]/table[1]/tbody/tr/td[2]/span").text)
driver.implicitly_wait(5)

mouse = driver.find_element_by_xpath(".//*[@id='1']/h3/a")
target = driver.find_element_by_xpath(".//*[@id='kw']")
print(mouse)
ActionChains(driver).drag_and_drop(mouse,target).perform()
driver.implicitly_wait(5)

time.sleep(50)
driver.quit()
