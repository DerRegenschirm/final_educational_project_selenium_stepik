import pytest
import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

#new language parameter
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")

    language = request.config.getoption("language")

    # languages for Chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)

    yield browser
    # time to wait for the button text
    time.sleep(2)
    print("\nquit browser..")
    browser.quit()