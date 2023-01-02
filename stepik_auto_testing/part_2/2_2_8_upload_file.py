from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import os

link = 'https://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    browser.get(link)
    browser.find_element(By.NAME, 'firstname').send_keys('Ivan')
    browser.find_element(By.NAME, 'lastname').send_keys('Ivanov')
    browser.find_element(By.NAME, 'email').send_keys('mail@mail')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.NAME, 'file').send_keys(file_path)

    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(1)

    answer = browser.switch_to.alert.text
    print(answer)
    print(answer.split()[-1])
    browser.switch_to.alert.accept()
finally:
    time.sleep(3)
    browser.quit()

# https://stepik.org/lesson/228249/step/8?unit=200781
