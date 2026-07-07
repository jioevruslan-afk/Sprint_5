from helpers import login_user, register_user
from locators import (
    ConstructorPageLocators,
    ForgotPasswordPageLocators,
    HeaderLocators,
    LoginPageLocators,
    RegisterPageLocators,
)


def test_login_from_main_page_login_button(driver, wait):
    email, password = register_user(driver, wait)

    driver.get(driver.base_url)
    wait.until(lambda d: d.find_element(*ConstructorPageLocators.LOGIN_TO_ACCOUNT_BUTTON)).click()
    login_user(driver, wait, email, password)

    assert wait.until(lambda d: d.find_element(*ConstructorPageLocators.ORDER_BUTTON)).is_displayed()


def test_login_from_personal_account_button(driver, wait):
    email, password = register_user(driver, wait)

    driver.get(driver.base_url)
    wait.until(lambda d: d.find_element(*HeaderLocators.PERSONAL_ACCOUNT_LINK)).click()
    login_user(driver, wait, email, password)

    assert wait.until(lambda d: d.find_element(*ConstructorPageLocators.ORDER_BUTTON)).is_displayed()


def test_login_from_registration_form(driver, wait):
    email, password = register_user(driver, wait)

    driver.get(f"{driver.base_url}/register")
    wait.until(lambda d: d.find_element(*RegisterPageLocators.LOGIN_LINK)).click()
    login_user(driver, wait, email, password)

    assert wait.until(lambda d: d.find_element(*ConstructorPageLocators.ORDER_BUTTON)).is_displayed()


def test_login_from_forgot_password_form(driver, wait):
    email, password = register_user(driver, wait)

    driver.get(f"{driver.base_url}/forgot-password")
    wait.until(lambda d: d.find_element(*ForgotPasswordPageLocators.LOGIN_LINK)).click()
    login_user(driver, wait, email, password)

    assert wait.until(lambda d: d.find_element(*ConstructorPageLocators.ORDER_BUTTON)).is_displayed()
