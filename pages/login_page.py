from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Other login link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM), "Login registration form is not presented"

    def register_new_user(self, email, password):
        reg_email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        reg_password1_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_1)
        reg_password2_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_2)
        reg_submit_btn=self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        reg_email_field.send_keys(email)
        reg_password1_field.send_keys(password)
        reg_password2_field.send_keys(password)
        reg_submit_btn.click()

