import pytest
from selenium.webdriver.common.by import By
from pages.connection_page import ConnectionPage

@pytest.fixture
def browser():
    from utilities.browser_utils import launch_browser
    driver = launch_browser()
    yield driver
    driver.quit()

def test_ui_page_landed(browser):
    connection_page = ConnectionPage(browser)
    connection_page.open_browser_app()
    assert connection_page.is_connection_setup_page(), "Not on Connection Setup Page"

def test_ui_browser_title(browser):
    connection_page = ConnectionPage(browser)
    connection_page.open_browser_app()
    assert "GRL-C3-TPT" in browser.title, "Browser title does not match"

def test_scan_network_button(browser):
    connection_page = ConnectionPage(browser)
    connection_page.open_browser_app()
    assert connection_page.is_scan_network_button_present(), "Scan Network button not present"
    assert connection_page.is_scan_network_button_clickable(), "Scan Network button not clickable"