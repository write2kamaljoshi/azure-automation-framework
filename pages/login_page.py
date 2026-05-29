from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_input = (By.NAME, "email")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@data-qa='login-button']")

    def open_login_page(self, url):
        self.driver.get(url)

    def login(self, email, password):

        self.driver.find_element(*self.email_input).send_keys(email)

        self.driver.find_element(*self.password_input).send_keys(password)

        self.driver.find_element(*self.login_button).click()