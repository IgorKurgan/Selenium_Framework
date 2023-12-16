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
from conftest import set_up


def test_about_page(set_up):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    print("START TEST")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_products()
    mp.select_menu_about()

    time.sleep(10)
