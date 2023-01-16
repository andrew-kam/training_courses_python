import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"https://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"https://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print('111')

    def test_guest_should_see_navbar_element(self, browser, language):
        print(language)


if __name__ == "__main__":
    pytest.main()

    # pytest -s -v -rp stepik_auto_testing/part_3/3_6_3_example_parametrize_test.py

# https://stepik.org/lesson/237240/step/3?auth=login&next=&unit=209628
