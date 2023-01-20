import pytest
from selenium.webdriver.common.by import By


link = "https://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


# @pytest.mark.flaky(reruns=2)
def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")


if __name__ == "__main__":
    pytest.main()

# pytest -s -v --tb=line -rpf --reruns 1 stepik_auto_testing/part_3/3_6_8_reruns_test.py

# https://stepik.org/lesson/237240/step/8?auth=login&next=&unit=209628
