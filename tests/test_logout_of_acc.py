from conftest import webdriver_fixture
from locators import TestPersonalAccLocators as TestPersAccLoc

class TestPersonalAcc:
    def test_logout(self, webdriver_fixture):
        driver = webdriver_fixture
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        driver.find_element(TestPersAccLoc.PERSONAL_ACC_LOGOUT).click()
        assert "Стартап" in driver.title or "Главная" in driver.title
