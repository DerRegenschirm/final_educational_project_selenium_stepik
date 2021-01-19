import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла


class ProductPage(BasePage):
    def correct_success_message(self):
        self.should_be_add_button()
        self.click_add_button()
        self.solve_quiz_and_get_code()
        self.should_be_success_message()
        title=self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        assert title.text in success_message.text

    def correct_price(self):
        self.should_be_add_button()
        self.click_add_button()
        self.should_be_price_message()
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE)
        assert price.text in price_message.text

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADDTOBASKET_BTN), "Add to cart button is not presented"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "No success message"

    def should_be_price_message(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_MESSAGE)

    def click_add_button(self):
        add_but=self.browser.find_element(*ProductPageLocators.ADDTOBASKET_BTN)
        add_but.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")