import pytest
from selene import browser


@pytest.fixture(scope='function')
def setting_browser():
    browser.config.window_height = 1366
    browser.config.window_width = 1024
    yield
    browser.quit()
