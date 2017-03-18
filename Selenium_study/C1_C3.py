from selenium import webdriver
import time

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
