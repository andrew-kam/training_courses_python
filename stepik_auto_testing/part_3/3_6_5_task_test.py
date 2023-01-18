import time
import math

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


@pytest.mark.parametrize('link', [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
])
def test_login(browser, link):
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

    try:
        # check 'solve again'
        WebDriverWait(browser, 10).until(
            ec.element_to_be_clickable((
                By.CSS_SELECTOR, "button.again-btn"
            ))).click()
        print('pressed solve again')
    except TimeoutException:
        print('not found solve again')
    finally:
        # waiting for disappearing "disabled"
        WebDriverWait(browser, 10).until_not(
            ec.element_attribute_to_include((
                By.CSS_SELECTOR, "textarea.ember-text-area"), 'disabled'))

        WebDriverWait(browser, 10).until(
            ec.visibility_of_element_located((
                By.CSS_SELECTOR, 'textarea.ember-text-area'
            ))).send_keys(str(math.log(int(time.time()))))

        WebDriverWait(browser, 10).until(
            ec.element_to_be_clickable((
                By.CSS_SELECTOR, 'button.submit-submission'
            ))).click()

        answer = WebDriverWait(browser, 10).until(
            ec.presence_of_element_located((
                By.CLASS_NAME, 'smart-hints__hint'
            ))).text

        assert answer == 'Correct!', answer


with open(r'stepik_auto_testing\part_3\rega_step.txt', 'r') as f:
# with open('rega_step.txt', 'r') as f:
    log, pas = [line.strip() for line in f.readlines()]

if __name__ == "__main__":
    pytest.main()

# https://stepik.org/lesson/237240/step/5?auth=login&next=&unit=209628

# pytest -s -v --tb=line -rpf stepik_auto_testing/part_3/3_6_5_task_test.py


# The owls are not what they seem! OvO
