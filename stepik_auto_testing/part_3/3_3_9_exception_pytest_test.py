import pytest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_exception1():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        browser.get("https://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(
                By.CSS_SELECTOR, "button.btn")
            pytest.fail("No should be button send")
    finally:
        browser.quit()


def test_exception2():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        browser.get("https://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(
                By.CSS_SELECTOR, "no_such_button.btn")
            pytest.fail("No should be button send")
    finally:
        browser.quit()

# https://stepik.org/lesson/193188/step/9?auth=login&unit=167629
