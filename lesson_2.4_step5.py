import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/cats.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(10)

    #time.sleep(1)
    button = browser.find_element_by_id("button")
    button.click()


finally:
    time.sleep(5)
    browser.quit()