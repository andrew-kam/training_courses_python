from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def check_reg_form(url):
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        browser.get(url)

        browser.find_element(
            By.CLASS_NAME, 'first_block .first'
        ).send_keys("Ivan")

        browser.find_element(
            By.CLASS_NAME, 'first_block .second'
        ).send_keys("Petrov")

        browser.find_element(
            By.CLASS_NAME, 'first_block .third'
        ).send_keys("name@mail.com")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        assert welcome_text_elt.text == "Congratulations! You have successfully registered!"
        print('OK!')
    finally:
        time.sleep(5)
        browser.quit()


link_1 = "http://suninjuly.github.io/registration1.html"
link_2 = "http://suninjuly.github.io/registration2.html"

check_reg_form(link_1)
check_reg_form(link_2)

# https://stepik.org/lesson/138920/step/10?unit=196194
