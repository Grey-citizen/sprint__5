from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import webdriver_fixture
from locators import TestConstructorLocators as TestConstLoc

class TestConstructor:
    def test_constructor_sections(self, webdriver_fixture):
        driver = webdriver_fixture
        driver.get("https://stellarburgers.nomoreparties.site/")
        bun = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestConstLoc.CONSTRUCTOR_BUN))
        bun.click()
        assert "Булки" in driver.page_source
        assert 'active' in bun.get_attribute('class'), "Раздел 'Булки' не выбран"
        sauce = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestConstLoc.CONSTRUCTOR_SAUCE))
        sauce.click()
        assert "Соусы" in driver.page_source
        assert 'active' in sauce.get_attribute('class'), "Раздел 'Соусы' не выбран"
        staffing = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestConstLoc.CONSTRUCTOR_STAFFING))
        staffing.click()
        assert "Начинки" in driver.page_source
        assert 'active' in staffing.get_attribute('class'), "Раздел 'Начинки' не выбран"