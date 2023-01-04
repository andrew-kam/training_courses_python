import time
import unittest

from selenium.webdriver.common.by import By
from functions import browser


class TestReg(unittest.TestCase):
    def test_reg_form_1(self):
        browser.get("https://suninjuly.github.io/registration1.html")

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
        self.assertEqual(welcome_text_elt.text, 'Congratulations! You have successfully registered!',
                         'No Equal')
        print('OK!')

    def test_reg_form_2(self):
        browser.get("https://suninjuly.github.io/registration2.html")

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
        self.assertEqual(welcome_text_elt.text, 'Congratulations! You have successfully registered!',
                         '!!!!! No Equal !!!!!')
        print('OK!')


if __name__ == "__main__":
    unittest.main()

# https://stepik.org/lesson/36285/step/13?auth=login&unit=162401
