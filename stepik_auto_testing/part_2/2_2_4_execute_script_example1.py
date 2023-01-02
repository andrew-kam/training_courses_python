from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
time.sleep(2)
# browser.execute_script("alert('Robots at work');")
# browser.execute_script("document.title='Script executing';")
# browser.execute_script('document.title="Script executing";')
browser.execute_script("document.title='Script executing';alert('Robots at work');")

time.sleep(3)
browser.quit()

# https://stepik.org/lesson/228249/step/4?unit=200781
