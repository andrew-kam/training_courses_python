# browser = webdriver.Chrome()
# browser.get('https://login:password@your_site.ru')
# когда необходима аутентификация логин+пароль

# browser.switch_to.alert.dismiss()
# browser.switch_to.alert.send_keys("My answer")

# first_window = browser.window_handles[0] # 1-я из всего массива имен открытых вкладок
# new_window = browser.window_handles[1] # 2-я из всего массива имен открытых вкладок
# browser.switch_to.window(window_name)

# browser.execute_script(
#     "document.getElementsByTagName('button')[0].classList.remove('trollface');") # удаление класса на котором висит анимация


