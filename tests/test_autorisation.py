from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class TestAuthorisation:
    def test_login_in_acc_main_button(self):
        service = Service(executable_path='/Users/mistg/WebDriver/bin/chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.get("https://stellarburgers.nomoreparties.site/")
        try:
            driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
            assert "Вход" in driver.title
        finally:
            driver.quit()

    def test_login_in_acc_personal_cabinet_button(self):
        service = Service(executable_path='/Users/mistg/WebDriver/bin/chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.get("https://stellarburgers.nomoreparties.site/")
        try:
            driver.find_element(By.XPATH, "//a[text()='Личный кабинет']").click()
            assert "Вход" in driver.title
        finally:
            driver.quit()

    def test_login_in_acc_registration_form_button(self):
        service = Service(executable_path='/Users/mistg/WebDriver/bin/chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.get("https://stellarburgers.nomoreparties.site/register")
        try:
            driver.find_element(By.XPATH, "//button[text()='Войти']").click()
            assert "Вход" in driver.title
        finally:
            driver.quit()

    def test_login_in_acc_password_recovery_form_button(self):
        service = Service(executable_path='/Users/mistg/WebDriver/bin/chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        try:
            driver.find_element(By.XPATH, "//button[text()='Войти']").click()
            assert "Вход" in driver.title
        finally:
            driver.quit()