from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    browser.get(url)
    elements = browser.find_elements(By.CSS_SELECTOR, '[type=text]')
    for element in elements:
        element.send_keys("My_ans")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

# https://stepik.org/lesson/138920/step/7?unit=196194
