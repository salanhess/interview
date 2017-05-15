#coding=utf-8
from selenium import webdriver
import time

'''selenium的webdriver提供了八种基本的元素定位方法，前面六种是通过元素的属性来直接定位的，后面的xpath和css定位更加灵活，需要重点掌握其中一个。
1.通过id定位：find_element_by_id()
2.通过name定位：find_element_by_name()
3.通过class定位：find_element_by_class_name()
4.通过tag定位：find_element_by_tag_name()
5.通过link定位：find_element_by_link_text()
6.通过partial_link定位：find_element_by_partial_link_text()
7.通过xpath定位：find_element_by_xpath()
8.通过css定位：find_element_by_css_selector()
'''
#Basic click/sed_keys operation: open baidu,search xxx,open the second searched result.
browser = webdriver.Firefox()
browser.get("https://www.baidu.com")
#<input id="kw" class="s_ipt" name="wd" maxlength="100" autocomplete="off" type="text">
browser.find_element_by_class_name('s_ipt').send_keys('hello python')
#<input id="su" class="btn self-btn bg s_btn" value="百度一下" type="submit">
browser.find_element_by_id('su').click()
#<a data-click="{ 'F':'778317EA', 'F1':'9D73F1C4', 'F2':'4CA6DE6B', 'F3':'54E5343F', 'T':'1489766546', 'y':'FDBEDFE1' }" \
# href="http://www.baidu.com/link?url=i3ynyyw6rDZsGCUvq-cvde7Uc0dGj7X71InZxUv4qZGVJjfOmisNOuuRVpdodjAwPgtXz53keASagM1AWnsRSRHgi4Eov6V18Z_fHVwdJ9W" target="_blank">
time.sleep(3)
browser.find_element_by_xpath(".//*[@id='2']/h3/a").click()
time.sleep(3)
browser.quit()
