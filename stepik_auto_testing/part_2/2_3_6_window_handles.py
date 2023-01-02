from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'https://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_ = browser.find_element(By.ID, 'input_value').text
    y = calc(x_)
    browser.find_element(By.ID, 'answer').send_keys(y)

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    answer = browser.switch_to.alert.text
    print(answer.split()[-1])
finally:
    time.sleep(3)
    browser.quit()

# https://stepik.org/lesson/184253/step/6?unit=158843
