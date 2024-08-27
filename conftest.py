import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    webDriver = webdriver.Chrome()
    webDriver.maximize_window()
    yield webDriver
    webDriver.quit()