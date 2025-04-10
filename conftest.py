import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def webdriver_fixture():
    service = Service(executable_path='/Users/mistg/WebDriver/bin/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()