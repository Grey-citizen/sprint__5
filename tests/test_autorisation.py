from helpers import TestHelping as Helping
from locators import TestAuthorizationLocators as TestAuthoLoc

class TestAuthorisation:

    def test_login_in_acc_main_button(self):
        driver = Helping.webdriver_fixture()
        driver.get("https://stellarburgers.nomoreparties.site/")
        login_button = driver.find_element(TestAuthoLoc.MAIN_BUTTON)
        login_button.click()
        assert "Вход" in driver.title

    def test_login_in_acc_personal_cabinet_button(self):
        driver = Helping.webdriver_fixture()
        driver.get("https://stellarburgers.nomoreparties.site/")
        personal_cabinet_button = driver.find_element(TestAuthoLoc.HEADERS_PERSONAL_ACC)
        personal_cabinet_button.click()
        assert "Вход" in driver.title

    def test_login_in_acc_registration_form_button(self):
        driver = Helping.webdriver_fixture()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_button = driver.find_element(TestAuthoLoc.REGISTRATION_AUTHORIZATION_BUTTON)
        registration_button.click()
        assert "Вход" in driver.title


    def test_login_in_acc_password_recovery_form_button(self):
        driver = Helping.webdriver_fixture()
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        login_recovery_button = driver.find_element(TestAuthoLoc.RESET_PASSWORD_FORM_BUTTON)
        login_recovery_button.click()
        assert "Вход" in driver.title
