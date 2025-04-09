from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import TestHelping as Helping
from locators import TestConstructorLocators as TestConstLoc

class TestConstructor:
    def test_constructor_sections(self):
        driver = Helping.webdriver_fixture()
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestConstLoc.CONSTRUCTOR_BUN)).click()
        assert "Булки" in driver.page_source
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestConstLoc.CONSTRUCTOR_SAUCE)).click()
        assert "Соусы" in driver.page_source
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestConstLoc.CONSTRUCTOR_STAFFING)).click()
        assert "Начинки" in driver.page_source