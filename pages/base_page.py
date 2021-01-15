from selenium.common.exceptions import имя_исключения

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    # неявное ожидание
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # перехват исключения
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (имя_исключения):
            return False
        return True