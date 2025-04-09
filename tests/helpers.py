import random
import string
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class TestHelping:

    @pytest.fixture(scope="function")
    def webdriver_fixture(self):
        service = Service(executable_path='/Users/mistg/WebDriver/bin/chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        yield driver
        driver.quit()

    @staticmethod
    def generate_unique_email(first_name, last_name, cohort_number, domain="yandex.ru"):
        random_digits = ''.join(random.choices('0123456789', k=3))
        email = f"{first_name.lower()}{last_name.lower()}{cohort_number}{random_digits}@{domain}"
        return email

    @staticmethod
    def generate_password(length=8):
        if length < 6:
            raise ValueError("Пароль должен содержать не менее 6 символов.")
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation
        all_characters = lowercase + uppercase + digits + special_characters
        password = ''.join(random.choices(all_characters, k=length))
        return password
