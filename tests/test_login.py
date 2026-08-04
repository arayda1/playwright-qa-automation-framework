import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from utils.data_reader import load_test_data
from utils.logger import logger
from utils.screenshot import take_screenshot


def test_successful_login(page):

    logger.info("Starting successful login test")

    data = load_test_data()

    login_page = LoginPage(page)

    try:
        logger.info("Opening login page")

        login_page.login(
            data["valid_user"]["username"],
            data["valid_user"]["password"]
        )

        logger.info("Checking successful login")

        expect(page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )

        logger.info("Login test passed successfully")

    except Exception as error:

        logger.error(
            f"Login test failed: {error}"
        )

        take_screenshot(
            page,
            "login_failure"
        )

        raise error