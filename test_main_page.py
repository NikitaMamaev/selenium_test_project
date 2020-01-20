from .pages.main_page import MainPage
from .pages.login_page import LoginPage


main_url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
login_url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, main_url)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, main_url)
    page.open()
    page.should_be_login_link()


def test_guest_is_in_login_page(browser):
    page = LoginPage(browser, login_url)
    page.open()
    page.should_be_login_page()
