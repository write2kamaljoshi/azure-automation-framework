from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def click_products(self):
        self.driver.find_element(By.XPATH, "//a[@href='/products']").click()

