from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()


class TestRegistration:
    # Страница регистрации, поле 'Имя'
    REGISTRATION_NAME = [By.XPATH, "//input[@name='name']"]
    # Страница регистрации, поле 'email'
    REGISTRATION_EMAIL = [By.XPATH, "//input[@name='email']"]
    # Страница регистрации, поле 'Пароль'
    REGISTRATION_PASSWORD = [By.XPATH, "//input[@name='password']"]
    # Страница регистрации, кнопка 'Зарегистрироваться'
    REGISTRATION_BUTTON = [By.XPATH, "//button[text()='Зарегистрироваться']"]
    # Страница регистрации, сообщение об ошибке
    REGISTRATION_ERROR = [By.XPATH, "//p[contains(@class, 'input__error')]"]
    # Страница регистрации, Кнопка 'Войти'
    REGISTRATION_AUTHORIZATION_BUTTON = [By.XPATH, "//a[text()='Войти']"]

class TestAuthorization:
    # Страница Авторизации, поле 'email'
    AUTHORIZATION_EMAIL = [By.XPATH, "//input[@name='email']"]
    # Страница Авторизации, поле 'пароль'
    AUTHORIZATION_PASSWORD = [By.XPATH,  "//input[@name='password']"]
    # Страница Авторизации, кнопка 'Войти'
    AUTHORIZATION_BUTTON = [By.XPATH, "//button[text()='Войти']"]


class TestConstructor:
    # Страница Конструктор, элемент 'Булки'
    CONSTRUCTOR_BUN = [By.XPATH, "//*[contains(@class, 'text_type_main-default') and text()='Булки']"]
    # Страница Конструктор, элемент 'Соусы'
    CONSTRUCTOR_SAUCE = [By.XPATH, "//*[contains(@class, 'text_type_main - default') and text()='Соусы']"]
    # Страница Конструктор, элемент 'Начинки'
    CONSTRUCTOR_STAFFING = [By.XPATH, "//*[contains(@class, 'text_type_main - default') and text()='Начинки']"]
    # Страница Конструктор, Кнопка 'Войти в аккаунт'
    CONSTRUCTOR_BUTTON = [By.XPATH, "//button[text()='Войти']"]

class TestHeaders:
    # Заголовок, 'Лого'
    HEADERS_LOGO = [By.XPATH, "//img[@alt='Логотип Stellar Burgers']"]
    # Заголовок, кнопка 'Конструктор'
    HEADERS_CONSTRUCTOR = [By.XPATH, "//a[text()='Конструктор']"]
    #Заголовок, кнопка 'Личный кабинет'
    HEADERS_PERSONAL_ACC = [By.XPATH, "//a[text()='Личный кабинет']"]

class TestPersonalAcc:
    # Личный кабинет, кнопка 'Выйти'
    PERSONAL_ACC_LOGOUT = [By.XPATH, "//button[text()='Выход']"]

class TestResetPassword:
    # Окно восстановления пароля, кнопка 'Войти'
    RESET_PASSWORD_FORM_BUTTON = [By.XPATH, "//button[text()='Войти']"]