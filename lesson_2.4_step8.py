import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)


    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100'))
    button = browser.find_element(By.CSS_SELECTOR, '#book')
    button.click()

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x)

    answer_space = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer_space.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, '#solve')
    button.click()


finally:
    time.sleep(10)
    browser.quit()