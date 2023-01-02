from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    # _ = button.location_once_scrolled_into_view
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) # верхняя граница элемента будет выровнена по верху видимой области прокрутки
    # browser.execute_script("window.scrollBy(0, 100);") # Эта команда проскроллит страницу на 100 пикселей вниз
    button.click()
finally:
    time.sleep(3)
    browser.quit()

# https://stepik.org/lesson/228249/step/5?unit=200781

'''
// javascript
button = document.getElementsByTagName("button")[0];
button.scrollIntoView(true);
'''
