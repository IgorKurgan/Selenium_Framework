import time

import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_product_1 = "//button[@id = 'add-to-cart-sauce-labs-backpack']"
    select_product_2 = "//button[@id = 'add-to-cart-sauce-labs-bolt-t-shirt']"
    select_product_3 = "//button[@id = 'add-to-cart-sauce-labs-bike-light']"
    cart = "//div[@id='shopping_cart_container']"
    burger_button = "//button[@id='react-burger-menu-btn']"
    about_link = "//a[@id='about_sidebar_link']"

    # Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.select_product_2)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.cart)))

    def get_burger_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.burger_button)))

    def get_about_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.about_link)))

    # Actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click to select product 1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click to select product 2")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("Click to select product 2")

    def click_get_cart(self):
        self.get_cart().click()
        print("Enter to cart")

    def click_burger_menu(self):
        self.get_burger_btn().click()
        print("Click burger menu")

    def click_about_link(self):
        self.get_about_link().click()
        print("Click about page")

    # Methods
    def select_products(self):
        with allure.step("Select products"):
            Logger.add_start_step(method="select_products")
            self.get_current_url()
            self.click_select_product_1()
            self.click_get_cart()
            Logger.add_end_step(url=self.driver.current_url, method="select_products")

    def select_products_2(self):
        Logger.add_start_step(method="select_products_2")
        self.get_current_url()
        self.click_select_product_2()
        self.click_get_cart()
        Logger.add_end_step(url=self.driver.current_url, method="select_products_2")

    def select_products_3(self):
        Logger.add_start_step(method="select_products_3")
        self.get_current_url()
        self.click_select_product_3()
        self.click_get_cart()
        Logger.add_end_step(url=self.driver.current_url, method="select_products_3")

    def select_menu_about(self):
        self.get_current_url()
        self.click_burger_menu()
        self.click_about_link()
