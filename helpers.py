from random import randint
from string import ascii_letters, digits

from locators import LoginPageLocators, RegisterPageLocators


def generate_email():
    random_number = randint(100, 999)
    return f"ruslan_hvalii_47_{random_number}@yandex.ru"


def generate_password(length=8):
    symbols = ascii_letters + digits
    return "".join(symbols[randint(0, len(symbols) - 1)] for _ in range(length))


def open_registration_page(driver, wait):
    driver.get(f"{driver.base_url}/register")
    wait.until(lambda d: d.find_element(*RegisterPageLocators.REGISTER_BUTTON))


def register_user(driver, wait):
    email = generate_email()
    password = generate_password()

    open_registration_page(driver, wait)
    wait.until(lambda d: d.find_element(*RegisterPageLocators.NAME_INPUT)).send_keys("Ruslan")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    wait.until(lambda d: d.find_element(*LoginPageLocators.LOGIN_BUTTON))

    return email, password


def login_user(driver, wait, email, password):
    wait.until(lambda d: d.find_element(*LoginPageLocators.EMAIL_INPUT)).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
