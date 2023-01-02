from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://suninjuly.github.io/get_attribute.html"

try:
    browser.get(url)

    x_element = browser.find_element(
        By.ID, 'treasure')
    x_str = x_element.get_attribute('valuex')
    y = calc(x_str)

    browser.find_element(
        By.ID, 'answer'
    ).send_keys(str(y))

    browser.find_element(
        By.ID, 'robotCheckbox'
    ).click()

    browser.find_element(
        By.ID, 'robotsRule'
    ).click()

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(10)
    browser.quit()

# https://stepik.org/lesson/165493/step/7?unit=140087
