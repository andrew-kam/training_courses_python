from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# def driver():
#     driver_chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver_chrome.maximize_window()
#     driver_chrome.implicitly_wait(10)
#     yield driver_chrome
#     driver_chrome.quit()


def test_stepik_one(driver):
    driver.get('https://suninjuly.github.io/registration1.html')
