from pages.locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(LoginPageLocators):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
