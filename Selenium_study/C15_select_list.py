#coding=utf8
# xx not work, add issue on https://github.com/mozilla/geckodriver/issues/554

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("http://global.bing.com/")
driver.implicitly_wait(20)

mouse = driver.find_element_by_id("off_link")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(5)
#print(driver.find_element_by_id("officemenu_word_img"))
driver.find_element_by_id("officemenu_word_img").click()

