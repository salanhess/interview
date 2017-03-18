#coding=utf-8

from selenium import webdriver
import time
#refer to http://www.cnblogs.com/yoyoketang/p/6128596.html

#1.popup window simple handle: browser.switch_to.alert.accept()
#refer to http://blog.163.com/yang_jianli/blog/static/161990006201242954125169/
'''        使对象a指到该弹出框：
 a=driver.switch_to_alert()
 a.accept()   # 相当于点击确定，或者使用   driver.execute("acceptAlert")
 a.dismiss()  # 相当于点击取消，或者使用   driver.execute("dismissAlert")
 a.text           #获取弹出框里的文字  或者使用  driver.execute("getAlertText")["value"]
'''

#Need import correct username/password
u = "carol2000"
pwd = "XXX"

def login(username,password):
    browser = webdriver.Firefox()
    browser.get("https://passport.cnblogs.com/user/signin")
    #2.隐式地等待一个无素被发现或一个命令完成；这个方法每次会话只需要调用一次,比 time.sleep() 更智能，
    # 后者只能选择一个固定的时间的等待，前者可以在一个时间范围内智能的等待。鼓励
    browser.implicitly_wait(4)
    browser.find_element_by_xpath(".//*[@id='input1']").send_keys(username)
    browser.find_element_by_xpath(".//*[@id='input2']").send_keys(password)
    browser.find_element_by_xpath(".//*[@id='signin']").click()
    browser.implicitly_wait(4)
    return browser

def logout():
    #logout with popup windows handle
    browser.find_element_by_xpath(".//*[@id='header_user_right']/a[5]").click()
    time.sleep(3)
    browser.switch_to.alert.accept()
    time.sleep(3)
    browser.quit()


if __name__ == "__main__":
    browser = webdriver.Firefox()
    browser = login(u,pwd)
    t = browser.find_element_by_xpath(".//*[@id='lnk_current_user']").get_attribute('href')
    print(t)
    if "carol2000" in t:
        print("Login check Pass!!")
    else:
        print("Login failed")
    logout()
