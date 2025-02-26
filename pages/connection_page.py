import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ConnectionPage(BasePage):
    SCAN_NETWORK_BUTTON = (By.XPATH, "//button[@id='connectionsetup_AutoDiscoverIP_button']")
    CONNECT_BUTTON = (By.XPATH, "//button[@id='connectionsetup_connect_button']")
    DEVICE_DETAILS_TABLE = (By.ID, "device_details_table")
    ADDRESS_TEXT = (By.XPATH, "//div[@id='ip-address-textbox-parent']")

    def open_browser_app(self):
        logger.info("Opening the browser application")
        self.driver.get("http://localhost:2004/")
        logger.info(f"Current page title: {self.driver.title}")
        WebDriverWait(self.driver, 30).until(
            lambda driver: "GRL-C3-TPT" in driver.title  # Update this to match the actual title
        )
        logger.info("Browser application opened successfully")

    def is_connection_setup_page(self):
        return "Connection Setup" in self.driver.title

    def is_scan_network_button_present(self):
        logger.info("Checking if the Scan Network button is present")
        return self.is_element_present(self.SCAN_NETWORK_BUTTON)

    def is_scan_network_button_clickable(self):
        logger.info("Checking if the Scan Network button is clickable")
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SCAN_NETWORK_BUTTON)
        ).is_enabled()

    def click_scan_network(self):
        logger.info("Clicking the Scan Network button")
        self.click(self.SCAN_NETWORK_BUTTON)

    def is_connect_button_disabled(self):
        logger.info("Checking if the Connect button is disabled")
        return "disabled" in self.driver.find_element(*self.CONNECT_BUTTON).get_attribute("class")

    def is_connect_button_enabled(self):
        logger.info("Checking if the Connect button is enabled")
        return "disabled" not in self.driver.find_element(*self.CONNECT_BUTTON).get_attribute("class")

    def wait_for_scan_to_complete(self):
        logger.info("Waiting for the scan to complete")
        WebDriverWait(self.driver, 30).until(
            lambda driver: "disabled" not in driver.find_element(*self.CONNECT_BUTTON).get_attribute("class")
        )

    def are_device_details_present(self):
        logger.info("Checking if device details are present")
        return self.is_element_present(self.DEVICE_DETAILS_TABLE)

    def get_address_text(self):
        logger.info("Getting address text")
        return self.get_element_text(self.ADDRESS_TEXT)