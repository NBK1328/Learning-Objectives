import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_main:
    


    def test_add_to_cart_button(self, browser):
        
        link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        browser.get(link)
        btnAdd = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        assert btnAdd is not None, "Элемент не найден"
        
        time.sleep(2)


