import time

import pytest
from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


if __name__ == "__main__":
    pytest.main()

# pytest -s -v --tb=line -rpf stepik_auto_testing/part_3/3_6_7_multi_browser_test.py
# * default chrome

# pytest -s -v --tb=line -rpf --browser_name=chrome stepik_auto_testing/part_3/3_6_7_multi_browser_test.py
# pytest -s -v --tb=line -rpf --browser_name=firefox stepik_auto_testing/part_3/3_6_7_multi_browser_test.py

# https://stepik.org/lesson/237240/step/7?auth=login&next=&unit=209628
