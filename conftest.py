import pytest

@pytest.fixture(scope="session")
def browser():
    from utilities.browser_utils import launch_browser
    driver = launch_browser()
    yield driver
    driver.quit()