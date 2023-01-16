import pytest
from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


if __name__ == "__main__":
    pytest.main()

    # pytest -s -v -rp stepik_auto_testing/part_3/3_6_2_example_with_conftest_test.py

# https://stepik.org/lesson/237240/step/2?auth=login&next=&unit=209628
