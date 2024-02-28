import pytest

from selene import browser


LOGIN = "m.daydream@mail.ru"
PASSWORD = "123456"
BASE_URL = "https://demowebshop.tricentis.com/"
@pytest.fixture(autouse=True)
def open_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open(BASE_URL)
    yield browser
    browser.quit()


