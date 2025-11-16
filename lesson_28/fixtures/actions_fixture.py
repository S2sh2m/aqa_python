import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page_locators import MainPageLocators
from pages.register_page_locators import RegisterPageLocators

@pytest.fixture
def open_registration(driver):
    def _open():
        driver.find_element(*MainPageLocators.SIGN_UP_BUTTON).click()
    return _open


@pytest.fixture
def register_user(driver):
    def _register(name, lastname, email, password):
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.LASTNAME_INPUT).send_keys(lastname)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/panel/garage")
        )

    return _register
