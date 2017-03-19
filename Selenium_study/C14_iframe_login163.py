#coding=utf8

#login 163: <iframe id="x-URS-iframe" name="" scrolling="no" style="width: 100%; height: 100%;
# border: medium none; background: transparent none repeat scroll 0% 0%;"
## src="https://passport.126.com/webzj/m126_1.0.1/pub/index_dl.html?wdaId=" frameborder="0">
#use firepath to indentify iframe

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://mail.126.com/")

driver.implicitly_wait(20)
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_name("email").send_keys("salanhess")
driver.find_element_by_name("password").send_keys("xxx")
driver.find_element_by_id("dologin").click()