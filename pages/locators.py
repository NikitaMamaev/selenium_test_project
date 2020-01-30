from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators(BasePage):
    # проверка на корректный url адрес
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'Substring "login" is not in current url'

    # проверка, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(
            By.CSS_SELECTOR, "#login_form"), "Login form is not presented"

    # проверка, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(
            By.CSS_SELECTOR, "#register_form"), "Register form is not presented"
