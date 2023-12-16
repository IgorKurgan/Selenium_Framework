import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import CartPage
from pages.client_information_page import ClientInformationPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage
from conftest import set_up, set_group


# @pytest.mark.run(order=2)
@allure.description("Test buy product 1")
def test_buy_product_1(set_up, set_group):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome()
    print("START TEST 1")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_products()

    cp = CartPage(driver)
    cp.click_checkout_btn()

    print("Finish test 1")
    # time.sleep(10)

    cip = ClientInformationPage(driver)
    cip.input_client_form()

    pp = PaymentPage(driver)
    pp.click_finish_button()

    fp = FinishPage(driver)
    fp.finish()


@pytest.mark.run(order=3)
def test_buy_product_2(set_up, set_group):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome()
    print("START TEST 2")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_products_2()

    cp = CartPage(driver)
    cp.click_checkout_btn()

    print("Finish test 2")
    time.sleep(10)


#
#
@pytest.mark.run(order=1)
def test_buy_product_3(set_up, set_group):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome()
    print("START TEST 3")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_products_3()

    cp = CartPage(driver)
    cp.click_checkout_btn()

    print("Finish test 3")
    time.sleep(10)
