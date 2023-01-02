from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://suninjuly.github.io/math.html"

try:
    browser.get(url)

    people_radio = browser.find_element(
        By.ID, "peopleRule")

    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked, type(people_checked))
    # assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element(
        By.ID, "robotsRule")

    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots radio: ", robots_checked, type(robots_checked))
    assert robots_checked is None

    people_checked_ = people_radio.is_selected()
    print(people_checked_, type(people_checked_))
    assert people_checked_

    robots_checked_ = robots_radio.is_selected()
    print(robots_checked_, type(robots_checked_))
    assert not robots_checked_

finally:
    time.sleep(1)
    browser.quit()

# https://stepik.org/lesson/165493/step/6?unit=140087
