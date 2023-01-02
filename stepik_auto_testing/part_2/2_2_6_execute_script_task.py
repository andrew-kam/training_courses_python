from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'https://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    browser.get(link)
    x_ = browser.find_element(By.ID, 'input_value').text

    y = calc(x_)
    browser.find_element(By.ID, 'answer').send_keys(y)

    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(
        By.ID, 'robotCheckbox'
    ).click()
    browser.find_element(
        By.ID, 'robotsRule'
    ).click()

    button.click()
    time.sleep(1)

    answer = browser.switch_to.alert.text
    print(answer.split()[-1])
finally:
    time.sleep(3)
    browser.quit()

# https://stepik.org/lesson/228249/step/6?unit=200781
