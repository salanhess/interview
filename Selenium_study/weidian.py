#coding=utf-8
#todo read: http://www.cnblogs.com/puresoul/p/4737716.html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.wait as wait
import time

#step1:login
def login(id,pwd):
    browser = webdriver.Firefox()
    browser.get("https://www.weidian.com/")
    browser.implicitly_wait(10)
    browser.find_element_by_xpath(".//*[@id='tele']").clear()
    time.sleep(2)
    browser.find_element_by_xpath(".//*[@id='tele']").send_keys(id)
    browser.find_element_by_xpath(".//*[@id='pass']").clear()
    time.sleep(2)
    browser.find_element_by_xpath(".//*[@id='pass']").send_keys(pwd)
    time.sleep(2)
    if (browser.find_element_by_css_selector(".btn-login.for_gaq").size != 0 ):
        print(browser.find_element_by_css_selector(".btn-login.for_gaq"))
        browser.find_element_by_css_selector(".btn-login.for_gaq").click()
        print("=======")
    else:
        browser.find_element_by_xpath(".//*[@id='pass']").send_keys(Keys.ENTER)
    time.sleep(4)
    return browser


#step2: Loop: Goto "dingdan guanli" > "fahuo"
def fahuo():
    browser.find_element_by_css_selector(".for_gaq").click()
    print(browser.find_elements_by_xpath(".deliver-goods.ng-scope"))

#step3: logout
id = 123
pwd = "abc"
browser = login(id,pwd)
fahuo()