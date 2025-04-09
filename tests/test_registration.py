from helpers import TestHelping as Helping
from locators import TestRegistrationLocators as TestRegLoc

class TestRegistration:

    def test_successful_registration(self):
        driver = Helping.webdriver_fixture()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        first_name = "Сергей"
        last_name = "Матросов"
        cohort_number = "20123"
        unique_email = Helping.generate_unique_email(first_name, last_name, cohort_number)
        password = Helping.generate_password(12)
        driver.find_element(TestRegLoc.REGISTRATION_NAME).send_keys(f"{first_name} {last_name}")
        driver.find_element(TestRegLoc.REGISTRATION_EMAIL).send_keys(unique_email)
        driver.find_element(TestRegLoc.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(TestRegLoc.REGISTRATION_BUTTON).click()
        assert driver.find_element(TestRegLoc.REGISTRATION_AUTHORIZATION_BUTTON), "Регистрация не удалась"

    def test_incorrect_password_registration(self):
        driver = Helping.webdriver_fixture()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        first_name = "Сергей"
        last_name = "Матросов"
        cohort_number = "20123"
        unique_email = Helping.generate_unique_email(first_name, last_name, cohort_number)
        password = Helping.generate_password(3)
        driver.find_element(TestRegLoc.REGISTRATION_NAME).send_keys(f"{first_name} {last_name}")
        driver.find_element(TestRegLoc.REGISTRATION_EMAIL).send_keys(unique_email)
        driver.find_element(TestRegLoc.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(TestRegLoc.REGISTRATION_BUTTON).click()
        error_message = driver.find_element(TestRegLoc.REGISTRATION_ERROR)
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"