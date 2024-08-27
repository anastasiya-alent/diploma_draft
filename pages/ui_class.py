from string_utils import StringUtils
from selenium.webdriver.common.by import By

class UiPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.chitai-gorod.ru/")

    def set_cookie_policy(self):
        cookie = {"name": "cookie_policy", "value": "1"}
        self._driver.add_cookie(cookie)

    #ввод разных значений в строку "Поиск"
    def search(self, term):

        self._driver.find_element(By.CSS_SELECTOR, ".header-search__input").send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, ".header-search__button").click()
        self._driver.implicitly_wait(10)
        
        try:
            self._driver.find_element(By.CSS_SELECTOR, ".search-page__found-message")
            self._driver.find_element(By.CSS_SELECTOR, ".header-search__clear").click()
            return True
        except:
            self._driver.find_element(By.CSS_SELECTOR, ".header-search__clear").click()
            return False
        
    def AddToCart(self):

        stringUtils = StringUtils()
        results = self._driver.find_elements(By.XPATH, '//*[@class="button action-button blue"]')
        self._driver.implicitly_wait(10)
        print(results) #для отладки результатов
        results[0].click()
        self._driver.get("https://www.chitai-gorod.ru/cart")
        goods_count_text = self._driver.find_element(By.CSS_SELECTOR, ".app-title__append").text
        goods_count = stringUtils.delete_symbol(goods_count_text, " товаров")
        goods_count = stringUtils.delete_symbol(goods_count_text, " товара")
        goods_count = stringUtils.delete_symbol(goods_count_text, " товар")
        
        self._driver.find_element(By.CSS_SELECTOR, ".delete-many").click()

        return int(goods_count)