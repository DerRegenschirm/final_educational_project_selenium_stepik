from .base_page import BasePage
from .locators import MainPageLocators

class LoginPage(BasePage):

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url == MainPageLocators.LOGIN_URL, "Other login link"

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_REGISTER_FORM), "Login registration form is not presented"
