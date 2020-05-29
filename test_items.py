import pytest
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_existence(browser):
    browser.get(link)
    #time.sleep(30)
    browser.implicitly_wait(5)

    try:
        browser.find_element_by_class_name("btn-add-to-basket")
        find = True

    except:
        find = False

    assert find, "'Add to basket' button does not exist on this page!"