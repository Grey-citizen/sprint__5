from conftest import webdriver_fixture
from locators import TestHeadersLocators as TestHeadLoc

class TestTransition:

    def test_transition_to_personal_cabinet(self, webdriver_fixture):
        driver = webdriver_fixture
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(TestHeadLoc.HEADERS_PERSONAL_ACC).click()
        assert "Личный кабинет" in driver.title


    def test_transition_from_personal_cabinet_to_constructor(self, webdriver_fixture):
        driver = webdriver_fixture
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        driver.find_element(TestHeadLoc.HEADERS_CONSTRUCTOR).click()
        assert "Конструктор" in driver.title


    def test_transition_from_personal_cabinet_to_main_page_logo(self, webdriver_fixture):
        driver = webdriver_fixture
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        driver.find_element(TestHeadLoc.HEADERS_LOGO).click()
        assert "Стартап" in driver.title or "Главная" in driver.title

