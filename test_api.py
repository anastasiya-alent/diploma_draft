from pages.api_class import apiClass

api = apiClass("https://web-gate.chitai-gorod.ru/api/v2/search/facet-search?phrase=")

#Поиск по полному названию книги
def test_search_full_description():
    auth_headers = api.get_token()
    response = api.get('Мятная сказка', auth_headers)
    assert response.status_code == 200

#Поиск по названию книги с опечаткой
def test_search_description_mistake():
    auth_headers = api.get_token()
    response = api.get('Дочь капитана', auth_headers)
    assert response.status_code == 200

#Ошибка в фамилии автора
def test_search_author_mistake():
    auth_headers = api.get_token()
    response = api.get('Шалахав', auth_headers)
    assert response.status_code == 200

#Обработка спецсимволов в запросе
def test_search_symbols():
    auth_headers = api.get_token()
    response = api.get('1984', auth_headers)
    assert response.status_code == 200

# негативный Метод POST вместо GET
def test_search_post_NEG():
    auth_headers = api.get_token()
    response = api.post('1984', auth_headers)
    assert response.status_code == 405

# Негативный Поиск по пустому полю
def test_search_blank_NEG():
    auth_headers = api.get_token()
    response = api.post('', auth_headers)
    assert response.status_code == 405