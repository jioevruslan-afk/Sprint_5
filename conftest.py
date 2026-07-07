import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.base_url = "https://stellarburgers.education-services.ru"
    browser.maximize_window()
    try:
        yield browser
    finally:
        browser.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)
