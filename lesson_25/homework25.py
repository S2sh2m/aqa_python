from selenium.webdriver.common.by import By

#XPATH (25)

SIGNIN_EMAIL = (By.XPATH, "//input[@id='signinEmail']")
SIGNIN_PASSWORD = (By.XPATH, "//input[@id='signinPassword']")
SIGNIN_LOGIN_BUTTON = (By.XPATH, "//button[contains(@class,'btn') and text()='Login']")
SIGNIN_CLOSE_BUTTON = (By.XPATH, "//button[@aria-label='Close']")

SIGNUP_NAME = (By.XPATH, "//input[@id='signupName']")
SIGNUP_LASTNAME = (By.XPATH, "//input[@id='signupLastName']")
SIGNUP_EMAIL = (By.XPATH, "//input[@id='signupEmail']")
SIGNUP_PASSWORD = (By.XPATH, "//input[@id='signupPassword']")
SIGNUP_REPEAT_PASSWORD = (By.XPATH, "//input[@id='signupRepeatPassword']")
SIGNUP_REGISTER_BUTTON = (By.XPATH, "//button[contains(@class,'btn-primary') and text()='Register']")

SIDEBAR_GARAGE = (By.XPATH, "//a[@href='/panel/garage']")
SIDEBAR_FUEL_EXPENSES = (By.XPATH, "//a[@href='/panel/expenses']")
SIDEBAR_INSTRUCTIONS = (By.XPATH, "//a[@href='/panel/instructions']")
SIDEBAR_LOGOUT = (By.XPATH, "//a[contains(@class,'text-danger')]")

GARAGE_TITLE = (By.XPATH, "//h1")
GARAGE_ADD_CAR_BUTTON = (By.XPATH, "//button[contains(@class,'btn-primary')]")
GARAGE_EMPTY_TEXT = (By.XPATH, "//p[contains(text(),'You don’t have any cars')]")

ADD_CAR_BRAND_SELECT = (By.XPATH, "//select[@id='addCarBrand']")
ADD_CAR_MODEL_SELECT = (By.XPATH, "//select[@id='addCarModel']")
ADD_CAR_MILEAGE_INPUT = (By.XPATH, "//input[@formcontrolname='mileage']")
ADD_CAR_SAVE_BUTTON = (By.XPATH, "//button[contains(@class,'btn-primary') and text()='Add']")

INSTRUCTIONS_TITLE = (By.XPATH, "//h1")
INSTRUCTIONS_TEXT = (By.XPATH, "//div[contains(@class,'instructions')]")

FOOTER_LOGO = (By.XPATH, "//a[@class='footer_logo']")
FOOTER_COPYRIGHT = (By.XPATH, "//p[contains(text(),'©')]")

# CSS (25)

HEADER_SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button.header_signin")
HEADER_SIGN_UP_BUTTON = (By.CSS_SELECTOR, "button.hero-descriptor_btn")
HEADER_LOGO = (By.CSS_SELECTOR, "a.header_logo")
HEADER_GUEST_LOGIN = (By.CSS_SELECTOR, "button.header-link.-guest")

SIGNIN_EMAIL_CSS = (By.CSS_SELECTOR, "#signinEmail")
SIGNIN_PASSWORD_CSS = (By.CSS_SELECTOR, "#signinPassword")
SIGNIN_LOGIN_BUTTON_CSS = (By.CSS_SELECTOR, "button.btn.btn-primary")
SIGNIN_CLOSE_BUTTON_CSS = (By.CSS_SELECTOR, "button[aria-label='Close']")

SIGNUP_NAME_CSS = (By.CSS_SELECTOR, "#signupName")
SIGNUP_LASTNAME_CSS = (By.CSS_SELECTOR, "#signupLastName")
SIGNUP_EMAIL_CSS = (By.CSS_SELECTOR, "#signupEmail")
SIGNUP_PASSWORD_CSS = (By.CSS_SELECTOR, "#signupPassword")
SIGNUP_REPEAT_PASSWORD_CSS = (By.CSS_SELECTOR, "#signupRepeatPassword")
SIGNUP_REGISTER_BUTTON_CSS = (By.CSS_SELECTOR, "button.btn.btn-primary")

SIDEBAR_GARAGE_CSS = (By.CSS_SELECTOR, "a[href='/panel/garage']")
SIDEBAR_FUEL_EXPENSES_CSS = (By.CSS_SELECTOR, "a[href='/panel/expenses']")
SIDEBAR_INSTRUCTIONS_CSS = (By.CSS_SELECTOR, "a[href='/panel/instructions']")
SIDEBAR_LOGOUT_CSS = (By.CSS_SELECTOR, "a.text-danger")

GARAGE_TITLE_CSS = (By.CSS_SELECTOR, "h1")
GARAGE_ADD_CAR_BUTTON_CSS = (By.CSS_SELECTOR, "button.btn.btn-primary")

ADD_CAR_BRAND_SELECT_CSS = (By.CSS_SELECTOR, "select#addCarBrand")
ADD_CAR_MODEL_SELECT_CSS = (By.CSS_SELECTOR, "select#addCarModel")
ADD_CAR_MILEAGE_INPUT_CSS = (By.CSS_SELECTOR, "input[formcontrolname='mileage']")
ADD_CAR_SAVE_BUTTON_CSS = (By.CSS_SELECTOR, "button.btn.btn-primary")

INSTRUCTIONS_TITLE_CSS = (By.CSS_SELECTOR, "h1")
INSTRUCTIONS_TEXT_CSS = (By.CSS_SELECTOR, "div.instructions")

FOOTER_LOGO_CSS = (By.CSS_SELECTOR, "a.footer_logo")
