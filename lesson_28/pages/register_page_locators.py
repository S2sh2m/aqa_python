from selenium.webdriver.common.by import By

class RegisterPageLocators:
    NAME_INPUT = (By.ID, "signupName")
    LASTNAME_INPUT = (By.ID, "signupLastName")
    EMAIL_INPUT = (By.ID, "signupEmail")
    PASSWORD_INPUT = (By.ID, "signupPassword")
    CONFIRM_PASSWORD_INPUT = (By.ID, "signupRepeatPassword")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Register']")
