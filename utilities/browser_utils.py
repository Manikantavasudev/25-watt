from selenium import webdriver

def launch_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver