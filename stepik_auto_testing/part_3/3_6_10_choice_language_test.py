import time

import pytest
from selenium.webdriver.common.by import By


def test_presence_button_add_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"), \
        '!!! button was not found !!!'


if __name__ == "__main__":
    pytest.main()

    # pytest -s -v -rp --language=es stepik_auto_testing/part_3/3_6_10_choice_language_test.py
    # pytest -s -v -rpf stepik_auto_testing/part_3/3_6_10_choice_language_test.py

# https://stepik.org/lesson/237240/step/10?auth=login&next=&unit=209628
