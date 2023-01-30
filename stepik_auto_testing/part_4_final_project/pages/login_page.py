from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            "Current page isn`t login page"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form is not presented"

    def register_new_user(self, email, password):
        email_entry_field = self.browser.find_element(
            *LoginPageLocators.REGISTER_EMAIL)
        email_entry_field.send_keys(email)

        password_entry_field = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD)
        password_entry_field.send_keys(password)

        password_confirm_entry_field = self.browser.find_element(
            *LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        password_confirm_entry_field.send_keys(password)

        button_register = WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(
                LoginPageLocators.REGISTER_BUTTON))
        button_register.click()
