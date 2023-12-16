import time

import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base
from utilities.logger import Logger


class ClientInformationPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    continue_btn = "//input[@id='continue']"

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.postal_code)))

    def get_continue_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.continue_btn)))

    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("Input postal code")

    def click_continue_btn(self):
        self.get_continue_btn().click()

    # Methods
    def input_client_form(self):
        with allure.step("Input client form"):
            Logger.add_start_step(method="input_client_form")
            self.get_current_url()
            self.input_first_name("Ivan")
            self.input_last_name("Ivanov")
            self.input_postal_code("Kurgan")
            self.click_continue_btn()
            Logger.add_end_step(url=self.driver.current_url, method="input_client_form")
