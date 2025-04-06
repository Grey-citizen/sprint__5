from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class TestPersonalAcc:
    def test_logout(self):
        service = Service(executable_path='/Users/mistg/WebDriver/bin/chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        try:
            driver.find_element(By.XPATH, "//button[text()='Выход']").click()
            assert "Стартап" in driver.title or "Главная" in driver.title
        finally:
            driver.quit()
