from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[text()='Конструктор']/parent::*")  # Ссылка «Конструктор» в шапке
    LOGO_LINK = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]")  # Логотип Stellar Burgers
    PERSONAL_ACCOUNT_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']/parent::*")  # Ссылка «Личный кабинет»


class ConstructorPageLocators:
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Заголовок конструктора
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт»
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # Кнопка «Оформить заказ»
    BUNS_TAB = (By.XPATH, ".//span[text()='Булки']/parent::*")  # Вкладка «Булки»
    SAUCES_TAB = (By.XPATH, ".//span[text()='Соусы']/parent::*")  # Вкладка «Соусы»
    FILLINGS_TAB = (By.XPATH, ".//span[text()='Начинки']/parent::*")  # Вкладка «Начинки»
    BUNS_TAB_SELECTED = (
        By.XPATH,
        ".//span[text()='Булки']/parent::*[contains(@class, 'tab_tab_type_current')]",
    )  # Активная вкладка «Булки»
    SAUCES_TAB_SELECTED = (
        By.XPATH,
        ".//span[text()='Соусы']/parent::*[contains(@class, 'tab_tab_type_current')]",
    )  # Активная вкладка «Соусы»
    FILLINGS_TAB_SELECTED = (
        By.XPATH,
        ".//span[text()='Начинки']/parent::*[contains(@class, 'tab_tab_type_current')]",
    )  # Активная вкладка «Начинки»


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # Поле Email на форме входа
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")  # Поле пароля на форме входа
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопка «Войти»


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")  # Поле имени на форме регистрации
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # Поле Email на форме регистрации
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")  # Поле пароля на форме регистрации
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка «Зарегистрироваться»
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")  # Ссылка «Войти» на форме регистрации
    PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")  # Ошибка для короткого пароля


class ForgotPasswordPageLocators:
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")  # Ссылка «Войти» на форме восстановления пароля


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, ".//a[text()='Профиль']")  # Ссылка «Профиль» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка «Выход»
