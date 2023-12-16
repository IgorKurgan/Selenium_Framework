import time

import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base
from utilities.logger import Logger


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    checkout_btn = "//button[@id='checkout']"

    # Getters

    def get_checkout_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.checkout_btn)))

    # Actions

    def click_checkout_btn(self):
        self.get_checkout_btn().click()
        print("Click checkout btn")

    # Methods
    def product_confirm(self):
        with allure.step("Product confirm"):
            Logger.add_start_step(method="product_confirm")
            self.get_current_url()
            self.click_checkout_btn()
            Logger.add_end_step(url=self.driver.current_url, method="product_confirm")



