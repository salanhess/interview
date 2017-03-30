#coding=utf-8
#todo read: http://www.cnblogs.com/puresoul/p/4737716.html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.wait as wait

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from contextlib import contextmanager

from selenium.common.exceptions import NoSuchElementException

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

@contextmanager
def wait_for_page_load(timeout=30):
    old_page = browser.find_element_by_tag_name('html')
    yield
    time.sleep(2)
    # try:
    #     WebDriverWait(browser, timeout).until(
    #         staleness_of(old_page)
    #     )
    # except IOError:
    #     print("IOError")
    # else:
    #     pass

#step2: Loop: Goto "dingdan guanli" > "fahuo"
def fahuo():
    #todo Add verify Max order automatically here
    with wait_for_page_load(20):
        browser.find_element_by_xpath("//div[@class='order-list']//a[.='发货']").click()
        time.sleep(3)
        browser.find_element_by_xpath("//div[@class='deliver-ope']//div[.='无需物流']").click()
        time.sleep(3)
        browser.find_element_by_xpath("//div[@class='deliver-detail']//div[.='发货']").click()
        time.sleep(2)



#step3: logout
id = 123
pwd = "test"

MaxOrders = 10
browser = login(id,pwd)

wait.WebDriverWait(browser, 10).until(lambda s: s.find_element_by_xpath(".//*[@id='hd_u_name']").is_displayed())
time.sleep(3)
browser.find_element_by_xpath("//div[@class='slider-left']//a[@data-for-gaq='订单管理']").click()
time.sleep(6)

for i in range(MaxOrders):
    print("Handle %s times" % i)
    if len(browser.window_handles) > 1:
        print("Switch window")
        for handle in browser.window_handles:  # 方法二，始终获得当前最后的窗口，所以多要多次使用
            browser.switch_to.window(browser.window_handles[1])
    fahuo()

    # except NoSuchElementException:
    #     print("Finished")