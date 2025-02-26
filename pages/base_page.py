from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def is_element_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    def get_element_text(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).text