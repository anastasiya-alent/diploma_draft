from string_utils import StringUtils
from selenium.webdriver.common.by import By
import allure

class UiPage:
    
    #Открытие Chrome и переход на страницу сайта Читай Город
    def __init__(self, driver):
            
        self._driver = driver
        self._driver.get("https://www.chitai-gorod.ru/")

    #Политика куки
    def set_cookie_policy(self):
            
        cookie = {"name": "cookie_policy", "value": "1"}
        self._driver.add_cookie(cookie)

    def search(self, term):
        with allure.step ("Ввод разных значений в строку Поиск"):

            self._driver.find_element(By.CSS_SELECTOR, ".header-search__input").send_keys(term)
            self._driver.find_element(By.CSS_SELECTOR, ".header-search__button").click()
            self._driver.implicitly_wait(10)
        try:
            found_message = self._driver.find_element(By.CSS_SELECTOR, ".search-page__found-message")
            self._driver.find_element(By.CSS_SELECTOR, ".header-search__clear").click()
            if found_message is None:
                return False
            else:
                return True
        except:
            self._driver.find_element(By.CSS_SELECTOR, ".header-search__clear").click()
            return False
            
    def get_empty_result_message(self):
        with allure.step ("Проверка пустой корзины"):

            self._driver.get("https://www.chitai-gorod.ru/cart")
            txt = self._driver.find_element(By.CSS_SELECTOR, '.empty-title').text
            result = (txt == 'В корзине ничего нет')
            return result
        


        
    