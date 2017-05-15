#coding=utf-8
#TBD: 1. refer to http://www.cnblogs.com/lovebread/archive/2010/11/09/1872747.html  add encrpt key in local disk
from selenium import webdriver
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#Need import correct username/password
u = "username"
pwd = "password"

def login(username,password):
    browser.get("http://erp.jd.com/")
    browser.implicitly_wait(4)
    browser.find_element_by_xpath(".//*[@id='username']").send_keys(username)
    browser.find_element_by_xpath(".//*[@id='password']").send_keys(password)
    browser.find_element_by_css_selector(".formsubmit_btn").click()
    browser.implicitly_wait(4)
    return browser

def logout():
    #logout with popup windows handle
    browser.get("http://erp.jd.com/logout")
    time.sleep(3)
    browser.quit()


if __name__ == "__main__":
    browser = webdriver.Firefox()
    browser = login(u,pwd)
    browser.find_element_by_css_selector("#clockLink>button").click()
    time.sleep(3)
    t = browser.find_element_by_css_selector(".check-long").text
    time.sleep(3)
    print r'已上班' + t[4:5] + r'小时'
    if t[4:5] < 8:
        print("Warning!Pls go back & continue work!!")
    else:
        print("Bingo!Good bye & see you tomorrow~")
    logout()
