# -*- coding: UTF-8 -*-
import os
from time import sleep
#refer to https://blog.csdn.net/YLBF_DEV/article/details/51482250
#https://huilansame.github.io/huilansame.github.io/archivers/how-to-use-firebug-firepath-in-firefox

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


# 初始化配置
def initWork():
    # 初始化配置根据自己chromedriver位置做相应的修改
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    return driver


# 执行登录
def handleLogin():
    # 定义自己的用户名密码
    username = "username"
    password = "password"
    # 执行操作的页面地址
    url = 'https://uc.jdcloud.com/login?returnUrl=https%3A%2F%2Fwww.jdcloud.com%2Findex/'
    #driver.set_window_size(480, 760)
    driver.get(url)
    driver.implicitly_wait(20)
    # 获得cookie信息
    cookie1 = driver.get_cookies()
    # 将获得cookie的信息打印
    print cookie1
    # 休眠两秒钟后执行填写用户名和密码操作
    sleep(2)
    driver.switch_to.frame("login_frame")
    driver.find_element_by_name("loginname").send_keys(username)
    driver.find_element_by_name("nloginpwd").send_keys(password)
    driver.find_element_by_id("paipaiLoginSubmit").click()
    cookie2 = driver.get_cookies()
    # 将获得cookie的信息打印
    print cookie2

    # 判断是否登录成功
    if cookie1 == cookie2:
        print u' (￣y▽￣)╭login failed,will try 60s later'
        sleep(60)
    else:
        wait = WebDriverWait(driver, 30)
        wait.until(lambda driver: driver.find_elements_by_css_selector('.jc_hd_console'))


def handleNextPage():
    print u'====================================下一页======================================'
        # 点击下一页
    driver.find_element_by_css_selector('div.line-around.layout-box.mod-pagination > a.btn.box-col.line-left').click()
    sleep(2)

# 判断元素是否存在
def isPresent():
    temp =1
    try:
        elems = driver.find_elements_by_css_selector('div.line-around.layout-box.mod-pagination > a:nth-child(2) > div > select > option')
    except:
        temp =0
    return temp

# 解析信息并翻页
def perser():
    try:
        perserElements()
        sleep(10)
        handleNextPage()
    except:
        print u'=!=!=!=!=!=!=!=!=!=!=发生了意外=!=!=!=!=!=!=!=!=!=!='
    finally:
        pass

# 解析微博
def perserElements():
    elems = driver.find_elements_by_css_selector('div.card9')
    for elem in elems:
        head_img = elem.find_element_by_css_selector('header > a.mod-media.size-xs > div > img').get_attribute('src')
        print u'头像地址：' + head_img
        head_name = elem.find_element_by_css_selector('header > div > a > span').text
        head_time_from = elem.find_element_by_css_selector('header > div > div').text
        print head_name + u'    ' + head_time_from
        weibo_detail = elem.find_element_by_class_name('weibo-detail').text
        print weibo_detail
        print u'---------------------------------------'

if __name__ == '__main__':
    driver = initWork()
    try:
        handleLogin()
        cookie3 = driver.get_cookies()
        for cookie in driver.get_cookies():
            print "driver.add_cookie({\'name\':\'%s\', \'value\':\'%s\'})" % (cookie['name'], cookie['value'])
        # 将获得cookie的信息打印
        print cookie3
        # 获取信息
        print "==================================="
        print driver.find_element_by_css_selector('#userinfo').text
        print "==================================="
    finally:
        if driver._is_remote:
            driver.close()
            driver.quit()
    pass