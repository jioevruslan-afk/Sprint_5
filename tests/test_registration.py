from helpers import generate_email, generate_password, open_registration_page
from locators import LoginPageLocators, RegisterPageLocators


def test_successful_registration_redirects_to_login_page(driver, wait):
    open_registration_page(driver, wait)

    wait.until(lambda d: d.find_element(*RegisterPageLocators.NAME_INPUT)).send_keys("Ruslan")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(generate_password())
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    assert wait.until(lambda d: d.find_element(*LoginPageLocators.LOGIN_BUTTON)).is_displayed()


def test_registration_shows_error_for_short_password(driver, wait):
    open_registration_page(driver, wait)

    wait.until(lambda d: d.find_element(*RegisterPageLocators.NAME_INPUT)).send_keys("Ruslan")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(generate_password(length=5))
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    error = wait.until(lambda d: d.find_element(*RegisterPageLocators.PASSWORD_ERROR))
    assert error.text == "Некорректный пароль"
