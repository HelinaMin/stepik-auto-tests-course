import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/wait1.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    #time.sleep(1)
    browser.implicitly_wait(1)
    button = browser.find_element(By.CSS_SELECTOR, 'button#verify')
    button.click()

    message = browser.find_element(By.CSS_SELECTOR, '#verify_message')

    assert 'successful' in message.text, 'It\'s not working'


finally:
    time.sleep(5)
    browser.quit()