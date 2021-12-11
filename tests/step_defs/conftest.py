"""
This module contains shared fixtures, steps, and hooks.
"""
import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import logging


# Fixtures

logger = logging.getLogger()

@pytest.fixture
def driver():
    logger.error("Inside driver function")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


# Highlight

def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                            element, s)
    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(3)
    apply_style(original_style)

# Shared background given steps

