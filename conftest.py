import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    webDriver = webdriver.Chrome()
    webDriver.maximize_window()
    yield webDriver
    webDriver.quit()