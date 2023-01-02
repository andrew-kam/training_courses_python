import time
import math

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'https://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    browser.get(link)

    WebDriverWait(browser, 15).until(
        ec.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    browser.find_element(By.ID, 'book').click()

    x_ = browser.find_element(By.ID, 'input_value').text
    y = calc(x_)
    browser.find_element(By.ID, 'answer').send_keys(y)

    browser.find_element(By.ID, 'solve').click()

    answer = browser.switch_to.alert.text
    print(answer.split()[-1])
finally:
    time.sleep(3)
    browser.quit()

# https://stepik.org/lesson/181384/step/8?unit=156009
