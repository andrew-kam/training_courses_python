from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# https://stepik.org/lesson/138920/step/4?unit=196194
'''
    input1 = browser.find_element(by='tag name',value='value1')
    print(input1)
    input1.send_keys("Ivan")
    input2 = browser.find_element(by='name', value='value2')
    print(input2)
    input2.send_keys("Petrov")
    input3 = browser.find_element(by='class name', value='value3')
    print(input3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element(by='id',value='value4')
    print(input4)
    input4.send_keys("Russia")
    button = browser.find_element(by='css selector', value="button.btn")
    button.click()
'''
