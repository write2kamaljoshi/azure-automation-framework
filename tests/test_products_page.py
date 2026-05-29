from config.config import BASE_URL
from pages.home_page import HomePage

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from azure_utils.keyvault_helper import get_secret

email = get_secret("automation-email")
password = get_secret("automation-password")


def test_navigate_to_products_page(driver):

    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    products_page = ProductsPage(driver)

    login_page.open_login_page(BASE_URL)

    login_page.login(email, password)

    home_page.click_products()

    expected_url = "https://automationexercise.com/products"

    actual_url = products_page.get_current_url()

    assert expected_url == actual_url
