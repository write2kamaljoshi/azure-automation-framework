from config.config import BASE_URL

from pages.login_page import LoginPage
from pages.home_page import HomePage
from azure_utils.keyvault_helper import get_secret


def test_verify_home_page_title(driver):
    email = get_secret("automation-email")
    password = get_secret("automation-password")

    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.open_login_page(BASE_URL)

    login_page.login(email, password)

    expected_title = "Automation Exercise"

    actual_title = home_page.get_page_title()

    assert expected_title in actual_title