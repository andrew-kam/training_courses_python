import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_login(browser):
    link = 'https://stepik.org/lesson/236895/step/1'
    browser.get(link)

    WebDriverWait(browser, 10).until(
        ec.element_to_be_clickable((
            By.CLASS_NAME, 'navbar__auth_login'
        ))).click()
    browser.find_element(
        By.ID, 'id_login_email'
    ).send_keys(log)
    browser.find_element(
        By.ID, 'id_login_password'
    ).send_keys(pas)
    # don't press the button quickly
    time.sleep(2)

    WebDriverWait(browser, 10).until(
        ec.element_to_be_clickable((
            By.CLASS_NAME, 'sign-form__btn.button_with-loader'
        ))).click()


with open(r'stepik_auto_testing\part_3\rega_step.txt', 'r') as f:
# with open('rega_step.txt', 'r') as f:
    log, pas = [line.strip() for line in f.readlines()]

if __name__ == "__main__":
    pytest.main()

# https://stepik.org/lesson/237240/step/4?auth=login&next=&unit=209628

# pytest -s -v -rp stepik_auto_testing/part_3/3_6_4_task_log_in_test.py
