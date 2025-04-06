from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class TestTransition:

    def test_transition_to_personal_cabinet(self):
        service = Service(executable_path='/Users/mistg/WebDriver/bin/chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.get("https://stellarburgers.nomoreparties.site/")
        try:
            driver.find_element(By.XPATH, "//a[text()='Личный кабинет']").click()
            assert "Личный кабинет" in driver.title
        finally:
            driver.quit()

    def test_transition_from_personal_cabinet_to_constructor(self):
        service = Service(executable_path='/Users/mistg/WebDriver/bin/chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        try:
            driver.find_element(By.XPATH, "//a[text()='Конструктор']").click()
            assert "Конструктор" in driver.title
        finally:
            driver.quit()

    def test_transition_from_personal_cabinet_to_main_page_logo(self):
        service = Service(executable_path='/Users/mistg/WebDriver/bin/chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        try:
            driver.find_element(By.XPATH, "//img[@alt='Логотип Stellar Burgers']").click()
            assert "Стартап" in driver.title or "Главная" in driver.title
        finally:
            driver.quit()
