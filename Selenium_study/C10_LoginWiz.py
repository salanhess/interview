#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.wait as wait

import time
#refer to http://www.cnblogs.com/yoyoketang/p/6128596.html
#wait refer to https://blog.mozilla.org/webqa/2012/07/12/how-to-webdriverwait/
#Need import correct username/password
u = "test"
pwd = "123"

#Keypoints:
#1. Wrap login/logout
#2. Switch windows according handles
#3. clear contents before sendkeys
#4. wait.WebDriverWait.until method to wait for windows
#5. Use .text to verify page

def login(username,password):
    browser = webdriver.Firefox()
    browser.get("https://note.wiz.cn/login")
    browser.implicitly_wait(10)
    h = browser.current_window_handle
    browser.find_element_by_xpath(".//*[@id='openid-login']/div/div[2]/a/i").click()
    browser.implicitly_wait(4)
    browser.find_element_by_xpath(".//*[@id='login-wizID']").send_keys("test~~~")
    #print(browser.get_window_position("应用授权 - 为知笔记"))
    #Switch to the window which handle not the same as before(That's new window)
    for i in browser.window_handles:
        if i != h:
            browser.switch_to.window(i)
    time.sleep(8)

    #Firebug > console > window.name
    browser.find_element_by_xpath(".//*[@id='userId']").clear()
    time.sleep(2)
    browser.find_element_by_xpath(".//*[@id='userId']").clear()
    browser.find_element_by_xpath(".//*[@id='userId']").send_keys(u)
    browser.find_element_by_xpath(".//*[@id='passwd']").clear()
    time.sleep(2)
    browser.find_element_by_xpath(".//*[@id='passwd']").send_keys(pwd)
    time.sleep(5)
    browser.find_element_by_xpath(".//*[@id='passwd']").send_keys(Keys.ENTER)
    #print(browser.find_element_by_css_selector(".WB_btn_login.formbtn_01"))
    #browser.find_element_by_css_selector(".WB_btn_login.formbtn_01").click()
    time.sleep(2)
    return browser

def logout():
    #logout with popup windows handle
    browser.find_element_by_xpath(".//*[@id='pop-user-icon']").click()
    time.sleep(3)
    browser.find_element_by_xpath(".//*[@id='pop-user-setting']/ul/li[6]/span").click()
    time.sleep(3)
    t = browser.find_element_by_xpath(".//*[@id='login-tip']").text
    print(t)
    #browser.quit()


if __name__ == "__main__":
    browser = login(u,pwd)
    browser.switch_to.window(browser.window_handles[0])
    wait.WebDriverWait(browser,10).until(lambda s: s.find_element_by_xpath(".//*[@id='kbname']").is_displayed())
    time.sleep(3)
    if "Message" in browser.find_element_by_css_selector("#user-msg-btn>span").text:
        print("Login check Pass!!")
    else:
        print("Login failed")
    logout()
