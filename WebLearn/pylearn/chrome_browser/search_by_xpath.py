from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

chrome = Chrome()
chrome.get("https://y.qq.com")
btn = chrome.find_element_by_class_name("search_input__btn")
act = ActionChains(chrome)
ActionChains.move_to_element(act, btn).perform()
search_input = chrome.find_element_by_xpath("/html/body/div[1]/"
                                            "div/div[1]/div[1]/input")
search_input.click()
search_input.send_keys("等你下课")
btn.click()
span = chrome.find_element_by_class_name("songlist__songname")
ActionChains.move_to_element(ActionChains(chrome), span).perform()
chrome.find_element_by_class_name("list_menu__icon_play").click()
chrome.back()
chrome.close()
chrome.forward()
