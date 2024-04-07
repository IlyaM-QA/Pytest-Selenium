import pytest
import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_browser():
    """
    Test case TLP-12: Open url testqastudio.me
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--headless")

    service = Service()
    browser = webdriver.Chrome(service=service, options=chrome_options)
    
    browser.get(url='https://testqastudio.me/')
    element = browser.find_element(by=By.CSS_SELECTOR, value='#page [class*="meny-item-11088"]')
    element.click()
    
    blocks = browser.find_elements(by=By.CSS_SELECTOR, value='[class="elementor-widget-container"] >h4')

    headers = []
    for block in blocks:
        header = block.text
        headers.append(header)

    assert headers ==['Заказы:','Доставка и возврат:', 'Оплата:'], 'Unexpected headers in FAQ'