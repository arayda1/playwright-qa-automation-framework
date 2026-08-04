from pages.login_page import LoginPage
from playwright.sync_api import expect
from utils.logger import get_logger
from utils.screenshot import take_screenshot


logger = get_logger()


def test_successful_login(page):

    logger.info("Starting login test")

    login_page = LoginPage(page)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    logger.info("User logged in successfully")

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    take_screenshot(
        page,
        "successful_login"
    )

    logger.info("Login test completed")