from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://suninjuly.github.io/selects2.html'
# url = 'https://suninjuly.github.io/selects2.html'

try:
    browser.get(url)
    num_1 = browser.find_element(
        By.ID, 'num1').text
    num_2 = browser.find_element(
        By.ID, 'num2').text
    result = int(num_1) + int(num_2)
    print(result)

    select = Select(browser.find_element(
       By.ID, 'dropdown'))
    select.select_by_value(str(result))
    # select.select_by_visible_text(str(result))
    # select.select_by_index(index) # find by index from 0

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(10)
    browser.quit()

# https://stepik.org/lesson/228249/step/3?unit=200781

'''
    browser.find_element(
        By.ID, 'dropdown').click()
    browser.find_element(
        By.CSS_SELECTOR, f'[value="{str(result)}"]').click()
'''
