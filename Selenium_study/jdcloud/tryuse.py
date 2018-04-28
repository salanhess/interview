import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)
driver.get("http://mail.126.com/")
assert "126" in driver.title
driver.implicitly_wait(20)
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_name("email").send_keys("salanhess")
driver.find_element_by_name("password").send_keys("xxx")
driver.find_element_by_id("dologin").click()