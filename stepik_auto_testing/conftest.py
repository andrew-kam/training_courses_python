import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default="en",
                     help="Choose language: es/fr/ru ...")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = OptionsChrome()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})

        browser = webdriver.Chrome(options=options,
                                   service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", user_language)

        browser = webdriver.Firefox(options=options_firefox,
                                    service=FirefoxService(GeckoDriverManager().install()))
    # else:
    #     raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     browser.implicitly_wait(20)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
@pytest.fixture(scope="function")
def browser_f():
    print("\nstart browser for test..")
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    browser.implicitly_wait(20)
    yield browser
    print("\nquit browser..")
    browser.quit()
