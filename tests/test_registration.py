import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Registration:
    def generate_unique_email(self, first_name, last_name, cohort_number, domain="yandex.ru"):
        random_digits = ''.join(random.choices('0123456789', k=3))
        email = f"{first_name.lower()}{last_name.lower()}{cohort_number}{random_digits}@{domain}"
        return email

    def generate_password(self, length=8):
        if length < 6:
            raise ValueError("Пароль должен содержать не менее 6 символов.")
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation
        all_characters = lowercase + uppercase + digits + special_characters
        password = ''.join(random.choices(all_characters, k=length))
        return password

    def test_successful_registration(self):
        service = Service(executable_path='/Users/mistg/WebDriver/bin/chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.get("https://stellarburgers.nomoreparties.site/register")
        first_name = "Сергей"
        last_name = "Матросов"
        cohort_number = "20123"
        unique_email = self.generate_unique_email(first_name, last_name, cohort_number)
        password = self.generate_password(12)
        driver.find_element(By.NAME, "name").send_keys(f"{first_name} {last_name}")
        driver.find_element(By.NAME, "email").send_keys(unique_email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        assert driver.find_element(By.XPATH, "//button[text()='Войти']"), "Регистрация не удалась"
        driver.quit()

    def test_incorrect_password_registration(self):
        service = Service(executable_path='/Users/mistg/WebDriver/bin/chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.get("https://stellarburgers.nomoreparties.site/register")
        first_name = "Сергей"
        last_name = "Матросов"
        cohort_number = "20123"
        unique_email = self.generate_unique_email(first_name, last_name, cohort_number)
        password = self.generate_password(3)
        driver.find_element(By.NAME, "name").send_keys(f"{first_name} {last_name}")
        driver.find_element(By.NAME, "email").send_keys(unique_email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        error_message = driver.find_element(By.XPATH, "//p[contains(@class, 'input__error')]")
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
        driver.quit()