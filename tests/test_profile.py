from helpers import login_user, register_user
from locators import ConstructorPageLocators, HeaderLocators, LoginPageLocators, ProfilePageLocators


def test_go_to_personal_account(driver, wait):
    email, password = register_user(driver, wait)
    driver.get(driver.base_url)
    wait.until(lambda d: d.find_element(*HeaderLocators.PERSONAL_ACCOUNT_LINK)).click()
    login_user(driver, wait, email, password)

    wait.until(lambda d: d.find_element(*HeaderLocators.PERSONAL_ACCOUNT_LINK)).click()

    assert wait.until(lambda d: d.find_element(*ProfilePageLocators.PROFILE_LINK)).is_displayed()


def test_go_to_constructor_from_profile_by_constructor_link(driver, wait):
    email, password = register_user(driver, wait)
    driver.get(f"{driver.base_url}/login")
    login_user(driver, wait, email, password)
    wait.until(lambda d: d.find_element(*HeaderLocators.PERSONAL_ACCOUNT_LINK)).click()
    wait.until(lambda d: d.find_element(*ProfilePageLocators.PROFILE_LINK))

    driver.find_element(*HeaderLocators.CONSTRUCTOR_LINK).click()

    assert wait.until(lambda d: d.find_element(*ConstructorPageLocators.CONSTRUCTOR_TITLE)).is_displayed()


def test_go_to_constructor_from_profile_by_logo(driver, wait):
    email, password = register_user(driver, wait)
    driver.get(f"{driver.base_url}/login")
    login_user(driver, wait, email, password)
    wait.until(lambda d: d.find_element(*HeaderLocators.PERSONAL_ACCOUNT_LINK)).click()
    wait.until(lambda d: d.find_element(*ProfilePageLocators.PROFILE_LINK))

    driver.find_element(*HeaderLocators.LOGO_LINK).click()

    assert wait.until(lambda d: d.find_element(*ConstructorPageLocators.CONSTRUCTOR_TITLE)).is_displayed()


def test_logout_from_personal_account(driver, wait):
    email, password = register_user(driver, wait)
    driver.get(f"{driver.base_url}/login")
    login_user(driver, wait, email, password)
    wait.until(lambda d: d.find_element(*HeaderLocators.PERSONAL_ACCOUNT_LINK)).click()
    wait.until(lambda d: d.find_element(*ProfilePageLocators.LOGOUT_BUTTON)).click()

    assert wait.until(lambda d: d.find_element(*LoginPageLocators.LOGIN_BUTTON)).is_displayed()
