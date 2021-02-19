from .base_page import BasePage
#from .locators import MainPageLocators
#from .login_page import LoginPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

#    def go_to_login_page(self):
#        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        # alert = self.browser.switch_to.alert
        # alert.accept()

 #   def should_be_login_link(self):
 #       assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"