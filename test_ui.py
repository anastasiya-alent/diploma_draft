from pages.ui_class import UiPage

def test_search(driver):

    uipage = UiPage(driver)
    uipage.set_cookie_policy()

    #ввод разных значений в строку "Поиск"
    # isFound = uipage.search('Анна Каренина')
    # assert isFound == True

    # isFound = uipage.search('Three Men in a Boat')
    # assert isFound == True

    # isFound = uipage.search('ПУШКИН')
    # assert isFound == True

    # isFound = uipage.search('марина цветаева')
    # assert isFound == True

    # isFound = uipage.search('2019')
    # assert isFound == True

    # isFound = uipage.search('отцы и дети  }{*?,/')
    # assert isFound == True

    #добавление в корзину
    uipage.search('кролики и удавы')
    count_in_cart = uipage.AddToCart()
    assert count_in_cart == 1
