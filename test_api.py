from pages.api_class import apiClass
import pytest
import allure


api = apiClass("https://web-gate.chitai-gorod.ru/api/v2/search/facet-search?phrase=")

@allure.feature("API")
@allure.title("Поиск по полному названию книги")
@allure.description("Тест проверяет ответ на корректные данные в запросе ")
@allure.severity("blocker")
@allure.story("Позитивные проверки")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_search_full_description():
    auth_headers = api.get_token()
    response = api.get('Мятная сказка', auth_headers)
    assert response.status_code == 200


@allure.feature("API")
@allure.title("Поиск по названию книги с опечаткой")
@allure.description("Тест проверяет ответ на некорректные данные в запросе ")
@allure.severity("normal")
@allure.story("Позитивные проверки")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_search_description_mistake():
    auth_headers = api.get_token()
    response = api.get('Дочь капитана', auth_headers)
    assert response.status_code == 200


#Ошибка в фамилии автора
@allure.feature("API")
@allure.title("Поиск книги, если в фамилии автора ошибка")
@allure.description("Тест проверяет ответ некорректно введенных данных в запросе ")
@allure.severity("normal")
@allure.story("Позитивные проверки")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_search_author_mistake():
    auth_headers = api.get_token()
    response = api.get('Шалахав', auth_headers)
    assert response.status_code == 200


#Обработка спецсимволов в запросе
@allure.feature("API")
@allure.title("Обработка спецсимвола в запросе")
@allure.description("Тест проверяет ответ на обработку спецсимвола в запросе ")
@allure.severity("normal")
@allure.story("Позитивные проверки")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_search_symbols():
    auth_headers = api.get_token()
    response = api.get('1984', auth_headers)
    assert response.status_code == 200


# негативный Метод POST вместо GET
@allure.feature("API")
@allure.title("Обработка запроса с неверно выбранным методом")
@allure.description("Тест проверяет ответ на неверно указанный метод ") 
@allure.severity("blocker")
@allure.story("Негативные проверки")
@pytest.mark.api_test
@pytest.mark.negative_test
def test_search_post_NEG():
    auth_headers = api.get_token()
    response = api.post('Тихий дон', auth_headers)
    assert response.status_code == 405


# Негативный Поиск по пустому полю
@allure.feature("API")
@allure.title("Поиск по пустому полю")
@allure.description("Тест проверяет ответ на отправленное пустое поле в запросе ") 
@allure.severity("blocker")
@allure.story("Негативные проверки")
@pytest.mark.api_test
@pytest.mark.negative_test
def test_search_blank_NEG():
    auth_headers = api.get_token()
    response = api.get('', auth_headers)
    assert response.status_code == 400
