from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators(BasePage):
    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, 'Substring "login" is not in current url'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            By.CSS_SELECTOR, "#login_form"), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            By.CSS_SELECTOR, "#register_form"), "Register form is not presented"