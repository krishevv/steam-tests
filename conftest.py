import pytest

from utils.webdriver_singleton import WebDriverSingleton
from pages.main_page import MainPage

@pytest.fixture(scope="session")
def browser():
    driver = WebDriverSingleton().get_driver()
    yield driver
    WebDriverSingleton().close_driver()

@pytest.fixture(scope="function", autouse=True)
def setup_test(browser):
    main_page = MainPage(browser)
    main_page.open()
    assert "Welcome" in browser.title 
    yield  
