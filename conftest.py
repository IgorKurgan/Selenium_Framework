import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


@pytest.fixture()
def set_up():
    print("start test")
    yield
    print("finish test")


@pytest.fixture(scope="module")
def set_group():
    print("Enter system")
    yield
    print("exit system")