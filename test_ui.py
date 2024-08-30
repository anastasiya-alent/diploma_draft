from selenium.webdriver.chrome.webdriver import WebDriver
from pages.ui_class import UiPage
import allure
import pytest

driver = WebDriver()
uipage = UiPage(driver)
uipage.set_cookie_policy()

#ввод разных значений в строку "Поиск"

@allure.title("Поиск книги на кириллице") 
@allure.description("Проверка получения книг на кириллице") 
@allure.feature("UI")
@allure.severity("blocker") 
@allure.story("Позитивные проверки")
@pytest.mark.positive_test
@pytest.mark.ui_test
def test_search_kyrilic():
    isFound = uipage.search('Анна Каренина')
    assert isFound == True

@allure.title("Поиск книги на латинице") 
@allure.description("Проверка получения книг на латинице") 
@allure.feature("UI")
@allure.severity("blocker") 
@allure.story("Позитивные проверки")
@pytest.mark.positive_test
@pytest.mark.ui_test
def test_search_latin():
    isFound = uipage.search('Three Men in a Boat')
    assert isFound == True

@allure.title("Поиск книги в верхнем регистре") 
@allure.description("Тест проверяет поиск книги в верхнем регистре") 
@allure.feature("UI")
@allure.severity("blocker") 
@allure.story("Позитивные проверки")
@pytest.mark.positive_test
@pytest.mark.ui_test
def test_search_uppercase():
    isFound = uipage.search('ПУШКИН')
    assert isFound == True

@allure.title("Поиск книги в нижнем регистре") 
@allure.description("Тест проверяет поиск книги в нижнем регистре") 
@allure.feature("UI")
@allure.severity("blocker") 
@allure.story("Позитивные проверки")
@pytest.mark.positive_test
@pytest.mark.ui_test
def test_search_lowercase():
    isFound = uipage.search('марина цветаева')
    assert isFound == True

@allure.title("Поиск книги с названием из цифр") 
@allure.description("Тест проверяет поиск книги с названием из цифр") 
@allure.feature("UI")
@allure.severity("blocker") 
@allure.story("Позитивные проверки")
@pytest.mark.positive_test
@pytest.mark.ui_test
def test_search_numeric():
    isFound = uipage.search('1984')
    assert isFound == True

@allure.title("Поиск книги с спецсимволами в названии") 
@allure.description("Тест проверяет поиск книги с спецсимволами в названии") 
@allure.feature("UI")
@allure.severity("blocker") 
@allure.story("Позитивные проверки")
@pytest.mark.positive_test
@pytest.mark.ui_test 
def test_search_symbol():
    isFound = uipage.search('отцы и дети  }{*?,/')
    assert isFound == True

@allure.title("Поиск по символам юникода") 
@allure.description("Проверка поиска по символам") 
@allure.feature("UI")
@allure.severity("normal") 
@allure.story("Негативные проверки")
@pytest.mark.negative_test
@pytest.mark.ui_test
def test_search_unicode():
    isFound = uipage.search('˙·٠•●♥ Ƹ̵̡Ӝ̵̨̄Ʒ ♥●•٠·˙')
    assert isFound == False


#Проверка пустой кор

@allure.title("Проверка пустой корзины") 
@allure.description("Тест проверяет, что в пустой корзине появляется сообщение 'В корзине ничего нет'")
@allure.feature("UI")
@allure.severity("normal") 
@allure.story("Позитивные проверки")
@pytest.mark.positive_test
@pytest.mark.ui_test
def test_empty_bin():
    isFound = uipage.get_empty_result_message()
    assert isFound == True
