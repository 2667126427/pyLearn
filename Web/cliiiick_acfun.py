import time

from selenium.webdriver import Chrome, ChromeOptions

try:
    url = 'http://www.acfun.cn/'
    options = ChromeOptions()
    options.set_headless(False)
    chrome = Chrome(options=options)
    chrome.get(url)
    js = 'window.scrollTo(0, document.body.scrollHeight)'
    chrome.execute_script(js)
    avatar = chrome.find_element_by_css_selector(
        '#footer > div > div.clearfix.footer-top > '
        'div.fr.no-select.footer-avatar-ac > img')
    while True:
        avatar.click()
except KeyboardInterrupt as e:
    pass
    # print(e)
print("End.")
