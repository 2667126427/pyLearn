from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
elem = browser.find_element_by_name("wd")
elem.send_keys("baidu")
elem.send_keys(Keys.RETURN)
# browser.close()