import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.implicitly_wait(20)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def browser_f():
    print("\nstart browser_f for test..")
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    browser.implicitly_wait(20)
    yield browser
    print("\nquit browser_f..")
    browser.quit()
