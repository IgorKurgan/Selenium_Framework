import time
import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base
from utilities.logger import Logger


class LoginPage(Base):
    base_url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    user_name = "//input[@id='user-name']"
    password = "//input[@id='password']"
    login_btn = "//input[@id='login-button']"
    main_word = "//span[@class = 'title']"

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.password)))

    def get_login_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.login_btn)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.main_word)))

    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_btn(self):
        self.get_login_btn().click()
        print("Click to enter")

    # Methods
    def authorization(self):
        with allure.step("authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.base_url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_user_name("standard_user")
            self.input_password("secret_sauce")
            self.click_login_btn()
            self.assert_word(self.get_main_word(), "Products")
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
