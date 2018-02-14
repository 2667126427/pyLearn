from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions

driver = webdriver.Chrome()
driver.get("https://y.qq.com")
btn = driver.find_element_by_class_name("search_input__btn")
ActionChains(driver).move_to_element(btn).perform()
search_input = driver.find_element_by_class_name("search_input__input")
search_input.clear()
search_input.send_keys("等你下课")
btn.click()
ActionChains(driver).move_to_element(driver.find_element_by_class_name("songlist__songname"))\
    .perform()
driver.find_element_by_class_name("list_menu__icon_play").click()
print("OK")
