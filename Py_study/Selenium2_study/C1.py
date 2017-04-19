#coding=utf-8
#初学者最佳环境：python2.7+selenium2+Firefox46以下版本
#http://www.cnblogs.com/yoyoketang/p/selenium.html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Baidu(unittest.TestCase):
     def setUp(self):
         self.driver = webdriver.Firefox()
         self.driver.implicitly_wait(30)
         self.base_url = "http://www.baidu.com/"
         self.verificationErrors = []
         self.accept_next_alert = True
     # 回到顶部
     def scroll_top(self):
         if self.driver.name == "chrome":
            js = "var q=document.body.scrollTop=0"
         else:
            js = "var q=document.documentElement.scrollTop=0"
         return self.driver.execute_script(js)

     # 拉到底部
     def scroll_foot(self):
         if self.driver.name == "chrome":
            js = "var q=document.body.scrollTop=10000"
         else:
            js = "var q=document.documentElement.scrollTop=10000"
         return self.driver.execute_script(js)

     def test_baidu(self):
         driver = self.driver
         driver.get(self.base_url + "/")
         driver.find_element_by_id("kw").send_keys("selenium webdriver")
         driver.find_element_by_id("su").click()
         self.scroll_foot()
         time.sleep(3)
         self.scroll_top()
         time.sleep(4)
         driver.close()

     def is_element_present(self, how, what):
         try: self.driver.find_element(by=how, value=what)
         except NoSuchElementException, e: return False
         return True
     def is_alert_present(self):
         try: self.driver.switch_to_alert()
         except NoAlertPresentException, e: return False
         return True
     def close_alert_and_get_its_text(self):
        try:
           alert = self.driver.switch_to_alert()
           alert_text = alert.text
           if self.accept_next_alert:
               alert.accept()
           else:
               alert.dismiss()
           return alert_text
        finally: self.accept_next_alert = True

     def tearDown(self):
          self.driver.quit()
          self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
     unittest.main()