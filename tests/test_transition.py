from helpers import TestHelping as Helping
from locators import TestHeadersLocators as TestHeadLoc

class TestTransition:

    def test_transition_to_personal_cabinet(self):
        driver = Helping.webdriver_fixture()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(TestHeadLoc.HEADERS_PERSONAL_ACC).click()
        assert "Личный кабинет" in driver.title


    def test_transition_from_personal_cabinet_to_constructor(self):
        driver = Helping.webdriver_fixture()
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        driver.find_element(TestHeadLoc.HEADERS_CONSTRUCTOR).click()
        assert "Конструктор" in driver.title


    def test_transition_from_personal_cabinet_to_main_page_logo(self):
        driver = Helping.webdriver_fixture()
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        driver.find_element(TestHeadLoc.HEADERS_LOGO).click()
        assert "Стартап" in driver.title or "Главная" in driver.title

