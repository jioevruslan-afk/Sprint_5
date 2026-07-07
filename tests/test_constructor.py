from locators import ConstructorPageLocators


def test_constructor_go_to_buns_section(driver, wait):
    driver.get(driver.base_url)
    wait.until(lambda d: d.find_element(*ConstructorPageLocators.SAUCES_TAB)).click()
    wait.until(lambda d: d.find_element(*ConstructorPageLocators.BUNS_TAB)).click()

    current_tab = wait.until(lambda d: d.find_element(*ConstructorPageLocators.BUNS_TAB_SELECTED))
    assert current_tab.is_displayed()


def test_constructor_go_to_sauces_section(driver, wait):
    driver.get(driver.base_url)
    wait.until(lambda d: d.find_element(*ConstructorPageLocators.SAUCES_TAB)).click()

    current_tab = wait.until(lambda d: d.find_element(*ConstructorPageLocators.SAUCES_TAB_SELECTED))
    assert current_tab.is_displayed()


def test_constructor_go_to_fillings_section(driver, wait):
    driver.get(driver.base_url)
    wait.until(lambda d: d.find_element(*ConstructorPageLocators.FILLINGS_TAB)).click()

    current_tab = wait.until(lambda d: d.find_element(*ConstructorPageLocators.FILLINGS_TAB_SELECTED))
    assert current_tab.is_displayed()
