import pytest
from pages.connection_page import ConnectionPage
import logging
@pytest.fixture
def browser():
    from utilities.browser_utils import launch_browser
    driver = launch_browser()
    driver.maximize_window()
    yield driver
    driver.quit()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_scan_network_button(browser):
    logger.info("Starting test_scan_network_button")
    connection_page = ConnectionPage(browser)
    logger.info("ConnectionPage initialized")

    # Open the browser application
    logger.info("Opening the browser application")
    connection_page.open_browser_app()

    # Check if the Scan Network button is present
    logger.info("Checking if the Scan Network button is present")
    assert connection_page.is_scan_network_button_present(), "Scan Network button not present"

    # Check if the Scan Network button is clickable
    logger.info("Checking if the Scan Network button is clickable")
    assert connection_page.is_scan_network_button_clickable(), "Scan Network button not clickable"

    logger.info("test_scan_network_button completed successfully")

def test_device_details(browser):
    connection_page = ConnectionPage(browser)
    connection_page.open_browser_app()
    assert connection_page.are_device_details_present(), "Device details are not present"

def test_address_text(browser):
    connection_page = ConnectionPage(browser)
    connection_page.open_browser_app()
    assert "GRL-C3-MP-TPT IP Address:" in connection_page.get_address_text(), "Address text not found"