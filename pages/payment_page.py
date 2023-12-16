import time

import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base
from utilities.logger import Logger


class PaymentPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    finish_btn = "//button[@name='finish']"

    # Getters

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.finish_btn)))

    # Actions

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish button")

    # Methods
    def payment(self):
        with allure.step("Payment"):
            Logger.add_start_step(method="payment")
            self.get_current_url()
            self.click_finish_button()
            Logger.add_end_step(url=self.driver.current_url, method="payment")
