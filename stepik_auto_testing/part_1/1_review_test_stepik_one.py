import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture(scope='function')
def driver():
    driver_chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver_chrome.maximize_window()
    driver_chrome.implicitly_wait(10)
    yield driver_chrome
    driver_chrome.quit()


def test_stepik_one(driver):
    driver.get('http://suninjuly.github.io/registration1.html')
    '''
    driver.find_element(
        By.CSS_SELECTOR, '[placeholder="Input your first name"]'
    ).send_keys('Vasia')
    '''
    driver.find_element(
        By.CLASS_NAME, 'first_block .first'
    ).send_keys("Ivan")

    driver.find_element(
        By.CSS_SELECTOR, '[placeholder="Input your last name"]'
    ).send_keys('Pupkin')
    driver.find_element(
        By.CSS_SELECTOR, '.form-control.third'
    ).send_keys('hrenov@email.com')
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
    text_site = driver.find_element(By.CSS_SELECTOR, '.container h1')
    assert text_site.text == 'Congratulations! You have successfully registered!'
