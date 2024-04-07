import pytest

from selenium.webdriver.common.by import By

def test_browser(browser):
    """
    Test case TLP-12: Open url testqastudio.me
    """
	# определяем адрес страницы для теста и переходим на неё
    url = "https://testqastudio.me/"
    browser.get(url=url)
    # ищем по селектору элемент меню "Бестселлеры" и кликаем по нему
    element = browser.find_element(by=By.CSS_SELECTOR, value='#page [class*="menu-item-11088"]')
    element.click()

    blocks = browser.find_elements(by=By.CSS_SELECTOR, value='[class="elementor-widget-container"]>H4')
    headers = [block.text for block in blocks]
    #headers = []
    #for block in blocks:
    #    header = block.text
    #    headers.append(header)

    assert headers == ['Заказы:', 'Доставка и возврат:', 'Оплата:'], 'Unexpected headers in FAQ'

    #assert True, ''